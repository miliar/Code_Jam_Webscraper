#include<cstdio>
#include<cmath>
#define MAX 2000000000000000010LL
typedef long long u64;
u64 gao(u64 r,u64 k){
    u64 ans=k*(-1+2*r+2*k);
  //  printf("k=%20lld ans=%lld %lld\n",k,ans,2*k*k);
    return ans;
}
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int tt,T;
    u64 r,t,l,h,m;
 //   printf("%lld\n",gao(1LL,7472632214LL));
 //   printf("%lld\n",gao(1LL,707106780LL));
    scanf("%d",&T);
    for(tt=1;tt<=T;++tt){
        scanf("%lld%lld",&r,&t);
        l=1;
        h=(u64)(sqrt(t*0.5)+1);
        while(l+1<h){
            m=(l+h)>>1;
            if(gao(r,m)<=t)
                l=m;
            else
                h=m;
        }
        printf("Case #%d: %lld\n",tt,l);
    }
    return 0;
}