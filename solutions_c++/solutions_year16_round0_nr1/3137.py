#include<stdio.h>
#define LL long long
LL chk[15],ans[1000005],n;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    LL x,y,z,k,i;
    scanf("%lld",&n);
    for(i=1;i<=1000000;i++){
        x=i;
        y=k=0;
        while(y<10){
            z=i*(++k);
            while(z>0){
                if(chk[z%10]!=i){
                    chk[z%10]=i;
                    y++;
                }
                z/=10;
            }
        }
        ans[i]=k*i;
    }
    for(i=1;i<=n;i++){
        scanf("%lld",&x);
        if(x==0)    printf("Case #%lld: INSOMNIA\n",i);
        else    printf("Case #%lld: %lld\n",i,ans[x]);
    }
    return 0;
}
