#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("A-large.in","r",stdin);
    freopen("outA","w",stdout);
    int T,c=1;
    scanf("%d",&T);
    while(T--){
        long long n;
        scanf("%lld",&n);
        long long now=n;
        if(n==0){
            printf("Case #%d: INSOMNIA\n",c++);
            continue;
        }
        int i,suc=0,vis[10]={0},left=10;
        for(i=1;i<=1000000;i++){
            long long j=now;
            while(j!=0){
                if(!vis[j%10])vis[j%10]=1,left--;
                j/=10;
            }
            if(left==0){
                suc=1;
                printf("Case #%d: %lld\n",c++,now);
                break;
            }
            now+=n;
        }
        if(!suc)printf("!!!!\n");
    }
    return 0;
}
