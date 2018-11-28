#include<cstdio>
#include<cstring>
#include<algorithm>
#define mem(name,value) memset(name,value,sizeof(name))
#define FOR(i,n) for(int i=1;i<=n;i++)
using namespace std;

const int maxn = 1000+10;
int num[maxn],sumv[maxn];
char s[maxn];
int main(){
   // freopen("A-small-attempt3.in","r",stdin);
   // freopen("out.txt","w",stdout);
    int T,kase = 0,n;
    scanf("%d",&T);
    while(T--){
        scanf("%d%s",&n,s);
        for(int i=0;i<=n;i++) num[i] = s[i] - '0';

        int ans = 0;
        sumv[0] = num[0];
        for(int i=1;i<=n;i++){
            ans = max(ans,max(i-sumv[i-1],0));
            sumv[i] = sumv[i-1] + num[i];
        }
        printf("Case #%d: %d\n",++kase,ans);
    }
    return 0;
}
