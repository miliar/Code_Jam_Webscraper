#include<algorithm>
#include<cstdio>
#include<cmath>
#include<iostream>
#include<string.h>
#include<queue>
using namespace std;
const int N=1e6+10;
int main()
{
#ifdef gh546
freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
#endif // gh546
    int TAT; scanf("%d",&TAT);
    for(int cas=1;cas<=TAT;cas++){
        int n,vis[10],ans=0,cnt=0; scanf("%d",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",cas);continue;
        }
        memset(vis,0,sizeof(vis));
        for(int i=1;;i++){
            int x=n*i;
            while(x){
                int mod=x%10; x/=10;
                if(!vis[mod]){
                    vis[mod]=1; cnt++;
                    if(cnt==10){
                        ans=i; break;
                    }
                }
            }
            if(ans) break;
        }
        printf("Case #%d: %d\n",cas,ans*n);
    }
    return 0;
}
