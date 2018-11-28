#include <cstdio>
#include <vector>
#include <bitset>
#include <cstring>
#include <algorithm>
using namespace std;

int main(){
    int cs,no=0,n;
    scanf("%d",&cs);
    while(cs--){
        long long m,lhs=0,rhs=0;
        scanf("%d%I64d",&n,&m);
        if(--m==(1ll<<n)-1){
            lhs=rhs=(1ll<<n)-1;
        }else if(!m){
            lhs=rhs=0;
        }else{
            long long p=m,q=m;
            for(int i=1;i<n;i++){
                if(p<(1ll<<(n-i))) break;
                p-=1ll<<(n-i);
                lhs+=1ll<<i;
            }
            for(int i=1;i<n;i++){
                if(q<(1ll<<(i-1))) break;
                q-=1ll<<(i-1);
                rhs+=1ll<<(n-i);
            }
        }
        printf("Case #%d: %I64d %I64d\n",++no,lhs,rhs);
        /*
        int n,a[128],b[128],c[128];
        bitset<128>  u[128],v[128];
        scanf("%d",&n);
        for(int i=0;i<n;i++) u[i].set();
        for(int i=0;i<n;i++) a[i]=i;
        for(int all=0;all<10000000;all++){
            random_shuffle(a,a+n);
            for(int i=0;i<n;i++) b[i]=a[i];
            for(int l=n;l>1;l>>=1){
                for(int i=0;i<n;i+=l){
                    int lhs=i,rhs=i+l/2;
                    for(int j=0;j<l;j+=2){
                        int x=b[i+j],y=b[i+j+1];
                        if(x<y){
                            c[lhs++]=x;
                            c[rhs++]=y;
                        }else{
                            c[lhs++]=y;
                            c[rhs++]=x;
                        }
                    }
                }
                for(int i=0;i<n;i++) b[i]=c[i];
            }
            bitset<128>  s;
            for(int i=0;i<n;i++){
                s.set(b[i]);
                u[i]&=s;
                v[i]|=s;
            }
        }
        for(int i=0;i<n;i++){
            int ans=0;
            for(int x=0;x<n;x++) if(u[i].test(x)) ans=x;
            printf("%d ",ans);
        }
        puts("");
        for(int i=0;i<n;i++){
            int ans=0;
            for(int x=0;x<n;x++) if(v[i].test(x)) ans=x;
            printf("%d ",ans);
        }
        puts("");
        */
    }
}
