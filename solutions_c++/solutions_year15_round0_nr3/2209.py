#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<cstring>
FILE *in = fopen("c.in", "r");
FILE *out = fopen("c.out", "w");
using namespace std;
int quatToIndex(char x) {
    return (x == '1' ? 0 : (x == 'i' ? 1 : (x == 'j' ? 2 : 3)));
}
int indexToQuat(char m){
    return (m == 0 ? '1' : (m == 1 ? 'i' : (m == 2 ? 'j' : 'k')));
}
int sig[16] = {1,1,1,1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1};
char quatprod[16] = {'1','i','j','k','i','1','k','j','j','k','1','i','k','j','i','1'};
typedef struct quat{
    int sign;
    char num;
}quat;
quat quatop(quat a, quat b){
    quat c;
    int quatindex = 4 * quatToIndex(a.num) + quatToIndex(b.num);
    c.sign = a.sign * b.sign * sig[quatindex];
    c.num = quatprod[quatindex];
    return c;
}
quat quatInv(quat a){
    quat c;
    if(a.num == '1') c = a;
    else{
        quat c;
        c.sign = -1 * a.sign;
        c.num = a.num;
    }
    return c;
}
bool quateqv(quat a, quat b){
    return (a.sign == b.sign) && (a.num == b.num);
}
int T=0;
int t;
quat leftProd[11111], rightProd[11111], fullProd;
int main(){
    int len;
    char L[11111];
    long long int X;
    fscanf(in, "%d", &T);
    t = T;
    quat quati, quatj, quatk;
    quati.sign = quatj.sign = quatk.sign = 1;
    quati.num = 'i'; quatj.num = 'j'; quatk.num = 'k';
    while(T--){
        fscanf(in, "%d %lld", &len, &X);
        fscanf(in, "%s", L);
        long long int leftIndex=99999; long long int rightIndex=99999;
        quat left, right;
        left.sign = right.sign = 1;
        left.num = right.num = '1';
        int i;
        for(i=0; i<len; i++){
            leftProd[i].sign = 1;
            leftProd[i].num = L[i];
            left = leftProd[i] = quatop(left, leftProd[i]);
            if(quateqv(leftProd[i], quati))
                leftIndex = (leftIndex > i ? i : leftIndex);
        }
        fullProd = leftProd[len-1];
        if(leftIndex == 99999){
            quat leftTemp;
            leftTemp.sign = 1; leftTemp.num = '1';
            for(i=1; (i<4) && (i<X); i++){
                leftTemp = quatop(leftTemp, fullProd);
                for(int j=0; j<len; j++){
                    if(leftIndex != 99999) break;
                    if(quateqv(quatop(leftTemp, leftProd[j]), quati)){
                        leftIndex = len * i + j; break;
                    }
                }
                if(leftIndex != 99999) break;
            }
            if(i == 4 || i == X) {fprintf(out, "Case #%d: NO\n", t - T); continue; }
        }
        for(i=0; i<len; i++){
            rightProd[i].sign = 1;
            rightProd[i].num = L[len - 1 - i];
            right = rightProd[i] = quatop(rightProd[i], right);
            if(quateqv(right, quatk))
                rightIndex = (rightIndex > i ? i : rightIndex);
        }
        if(rightIndex == 99999){
            quat rightTemp;
            rightTemp.sign = 1; rightTemp.num = '1';
            for(i=1; (i<4) && (i<X); i++){
                rightTemp = quatop(fullProd, rightTemp);
                for(int j=0; j<len; j++){
                    if(rightIndex != 99999) break;
                    if(quateqv(quatop(rightProd[j], rightTemp), quatk)){
                        rightIndex = len * i + j; break;
                    }
                }
                if(rightIndex != 99999) break;
            }
            if(i == 4 || i == X) {fprintf(out, "Case #%d: NO\n", t - T); continue; }
        }
        if(leftIndex + 1 + rightIndex + 1 >= (long long int) len * X) {fprintf(out, "Case #%d: NO\n", t - T); continue;}
        int centerChunk = X % 4;
        quat quat1;
        quat1.sign = 1; quat1.num = '1';
        for(int i=0; i<centerChunk; i++)
            quat1 = quatop(quat1, fullProd);
        if(quat1.sign == -1 && quat1.num == '1') fprintf(out, "Case #%d: YES\n", t - T);
        else fprintf(out, "Case #%d: NO\n", t - T);
    }
    return 0;
}
