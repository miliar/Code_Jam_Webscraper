#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
int is[15];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    LL n,t,i,C=0;;
    scanf("%lld",&t);
    while(t--){
        scanf("%lld",&n);
        if(n==0){
            printf("Case #%lld: INSOMNIA\n",++C);
            continue;
        }
        for(i=0;i<10;i++) is[i]=0;
        int tmp=0;
        for(i=1;i<=1000000;i++){
            LL k=n*i;
            while(k){
                if(is[k%10]==0){
                    is[k%10]=1;
                    tmp++;
                }
                k/=10;
            }
            if(tmp==10) break;
        }
        if(tmp==10) printf("Case #%lld: %lld\n",++C,n*i);
        else printf("Case #%lld: INSOMNIA\n",++C);
    }
}
