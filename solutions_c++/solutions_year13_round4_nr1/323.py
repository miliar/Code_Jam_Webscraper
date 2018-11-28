#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;
const long long mod=1000002013;
struct aa{
    long long p,w;
}a[2010];
struct bb{
    long long e,o,p;
}b[2010];
struct ss{
    long long sum,w;
}s[2010];
int tot;
int n,m;
long long s1,s2,d,ans;
int cmp(aa x,aa y){
    if (x.w!=y.w) return x.w<y.w;
    return x.p>y.p;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int ca,cc=0;
    int i;
    scanf("%d",&ca);
    while (ca--){
        scanf("%d%d",&n,&m);
        s1=s2=0;
        for (i=0;i<m;i++){
            scanf("%lld%lld%lld",&b[i].e,&b[i].o,&b[i].p);
            a[i*2].p=b[i].p;a[i*2].w=b[i].e;
            a[i*2+1].p=-b[i].p;a[i*2+1].w=b[i].o;
            d=b[i].o-b[i].e;
            s1=s1+(d*(d-1)/2)%mod*b[i].p%mod;
            s1%=mod;
        }
        sort(a,a+2*m,cmp);
        tot=0;
        for (i=0;i<2*m;i++){
            //printf("i w p %d %lld %lld\n",i,a[i].w,a[i].p);
            if (a[i].p>0){
                tot++;
                s[tot].sum=a[i].p;
                s[tot].w=a[i].w;
            }else if (a[i].p<0){
                long long tp=a[i].p;
                //printf("tp %lld %lld\n",tp,s[tot].sum);
                while (tp+s[tot].sum<0){
                    tp+=s[tot].sum;
                    d=a[i].w-s[tot].w;
                    //printf("d %lld\n",d);
                    s2=s2+(d*(d-1)/2)%mod*s[tot].sum%mod;
                    s2%=mod;
                    tot--;
                   // printf("d %lld\n",d);
                }
                if (tp<0){
                    s[tot].sum+=tp;
                    d=a[i].w-s[tot].w;
                    //printf("d %lld\n",d);
                    s2=s2+(d*(d-1)/2)%mod*(-1*tp)%mod;
                    s2%=mod;
                }
                //printf("s2 %lld\n",s2);
            }
        }
        //printf("%lld %lld\n",s1,s2);
        ans=(s2-s1)%mod;
        if (ans<0) ans+=mod;
        printf("Case #%d: ",++cc);
        cout<<ans<<endl;
    }
    //while (1);
    return 0;
}
        
                    
            
