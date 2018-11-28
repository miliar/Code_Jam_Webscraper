#include<stdio.h>
#define ll long long
int main(void){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%i", &T);
    int l;
    for(l=0;l<T;l++){
        ll N;
        scanf("%lld", &N);
        if(N==0) {
            printf("Case #%i: INSOMNIA\n", l+1); continue;
        }
        int cifry[10];
        int i, j;
        for(i=0;i<10;i++){
            cifry[i]=0;
        }
        ll M;
        int res=0;
        for(i=1;i<500;i++){
            M=i*N;
            while(M>0){
                cifry[M%10]++;
                M/=10;
            }
            for(j=0;j<10;j++){
                if(cifry[j]==0) break;
                if(j==9){
                    res=i;
                }
            }
            if(res>0){printf("Case #%i: %lld\n",l+1, N*res); break;}
        }
    }
}
