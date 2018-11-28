#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int mul[5], L;
char ansC[25], ansJ[25];
int c = 0, j = 1000000000;
char outC[25], outJ[25];
char C[25], J[25];

void rec2(int len){
    //printf("2 %d %d %d\n", len, now1, now2);
    if(len >= L){
        //printf("%s %s\n", outC, outJ);
        outJ[len] = NULL;
        int now1 = 0, now2 = 0;
        int mul = 1;
        for(int i = L-1; i >= 0; --i){
            now1+=(outC[i]-'0')*mul;
            mul*=10;
        }
        mul = 1;
        for(int i = L-1; i >= 0; --i){
            now2+=(outJ[i]-'0')*mul;
            mul*=10;
        }
        if(abs(now1-now2) < abs(c-j)){
            strcpy(ansC, outC);
            strcpy(ansJ, outJ);
            c = now1;
            j = now2;
        }
        else if(abs(now1-now2) == abs(c-j)){
            if(now1 < c){
                strcpy(ansC, outC);
                strcpy(ansJ, outJ);
                c = now1;
                j = now2;
            }
            else if(now1 == c && now2 < j){
                strcpy(ansC, outC);
                strcpy(ansJ, outJ);
                c = now1;
                j = now2;
            }
        }
        return;
    }
    if(J[len] != '?'){
        outJ[len] = J[len];
        rec2(len+1);
    }
    else{
        for(int i = 0; i <= 9; ++i){
            outJ[len] = i+'0';
            rec2(len+1);
        }
    }
}

void rec(int len){
    if(len >= L){
        outC[len] = NULL;
        rec2(0);
        return;
    }
    if(C[len] != '?'){
        outC[len] = C[len];
        rec(len+1);
    }
    else{
        for(int i = 0; i <= 9; ++i){
            outC[len] = i+'0';
            rec(len+1);
        }
    }
}

int main(){
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt1.out", "w", stdout);
    int totalCase;
    mul[0] = 1;
    for(int i = 1; i < 5; ++i)
        mul[i] = mul[i-1]*10;
    scanf("%d", &totalCase);
    for(int T = 1; T <= totalCase; ++T){
        c = 0;
        j = 1000000;
        scanf("%s%s", C, J);
        L = strlen(C);
        rec(0);
        printf("Case #%d: %s %s\n", T, ansC, ansJ);
    }
    return 0;
}
/*
4
1? 2?
?2? ??3
? ?
?5 ?0

??2??5??
??2??4??
*/
