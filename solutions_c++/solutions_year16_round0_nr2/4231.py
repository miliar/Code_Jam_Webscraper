#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
const int inf=1e6+10;
typedef __int64 LL;
int vis[20];
LL ans[inf];
LL fun(LL i){
    memset(vis,0,sizeof(vis));LL cnt=10,j;
    for(j=i;;j+=i){
        LL k=j;
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
    int T=1;//scanf("%d",&T);int cas=1;
    memset(ans,-1,sizeof(ans));
    while(T--){
//        printf("Case #%d: ",cas++);
//        int n;scanf("%d",&n);
//        if(ans[n]!=-1){
//            printf("%I64d\n",ans[n]);continue;
//        }
//        if(n==0){
//            printf("INSOMNIA\n");continue;
//        }
//        printf("%I64d\n",ans[n]=fun(n));
        for(int i=1;i<=inf;i++){
            int j=fun(i);
            if(j/i>1000)printf("%d\n",i);
        }
    }
    return 0;
}
