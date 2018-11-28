#include <cstdio>
#include <cstring>
using namespace std;
char s[20000];
int a[20000];
int l, x, n;
int calc(int a, int b){
    int minus = 1;
    if (a < 0){
        a = -a; minus = -minus;
    }
    if (b < 0){
        b = -b; minus = -minus;
    }
    int ret;
    if (a == b) ret = (a==1?1:-1); else
    if (a == 1) ret = b; else
    if (b == 1) ret = a; else
    if (a+b == 5) ret = (a<b?4:-4); else
    if (a+b == 6) ret = (a<b?-3:3); else
    if (a+b == 7) ret = (a<b?2:-2);
//    printf("#### %d %d %d %d\n", a, b, ret, minus);
    ret = ret * minus;
    return ret;
}
int main(){
freopen("C.in", "r", stdin);
freopen("C.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int T=1; T<=test; T++){
        scanf("%d %d", &l, &x);
        scanf("%s", s+1);
        n = strlen(s+1);
        for (int i=1; i<x; i++){
            for (int j=1; j<=l; j++)
                s[i*l+j] = s[j];
        }
        int len = l*x;
        for (int i=1; i<=len; i++){
            a[i] = s[i]-'i'+2;
        }
        int ipos = -1, kpos = -1;
        int rlt = 1;
        for (int i=1; i<=len; i++){
            rlt = calc(rlt, a[i]);
            if (ipos == -1 && rlt == 2){
                ipos = i;
            }
        }
        printf("Case #%d: ", T);
        if (rlt != -1){
            puts("NO"); continue;
        }
        rlt = 1;
        for (int i=len; i; i--){
            rlt = calc(a[i], rlt);
            if (rlt == 4){
                kpos = i; break;
            }
        }
        if (ipos!=-1 && kpos!=-1 && ipos < kpos-1){
            puts("YES");
        } else{
            puts("NO");
        }
    }
    return 0;
}
