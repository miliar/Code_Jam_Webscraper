#include<stdio.h>
#include<string.h>
#include<algorithm>
#define SIZ 1010
using namespace std;
int n, a[SIZ];
int main(){
    int test;
    scanf("%d", &test);
    for(int tt=1; tt<=test; tt++){
        int i, j ,k;
        memset(a,0,sizeof(a));
        scanf("%d", &n);
        for(i=0; i<n; i++){
            scanf("%d", &j);
            a[j]++;
        }
        int re=1000000;
        for(i=1; i<=1000; i++){
            int ss=0;
            for(j=1000; j>i; j--){
                ss+=(j/i+((j%i==0)?-1:0))*a[j];
            }
            re=min(re,ss+i);
        }
        printf("Case #%d: %d\n", tt, re);
    }
    return 0;
}
