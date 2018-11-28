#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
const int inf=1e6+10;
typedef __int64 LL;
int vis[20];
int ans[inf];
int fun(int i){
    int cnt=10,j;memset(vis,0,sizeof(vis));
    for(j=i;;j+=i){
        int k=j;
        while(k){
            if(!vis[k%10]){
                cnt--;vis[k%10]=1;
            }
            k/=10;
        }
        if(cnt==0)break;
    }
    return j;
}
int main(){
    #ifdef DouBi
    freopen("in.cpp","r",stdin);
    freopen("out.cpp","w",stdout);
    #endif // DouBi
    int T=1;scanf("%d",&T);int cas=1;
    while(T--){
        printf("Case #%d: ",cas++);
        int n;scanf("%d",&n);
        if(n==0){
            printf("INSOMNIA\n");continue;
        }
        printf("%d\n",fun(n));
    }
    return 0;
}
