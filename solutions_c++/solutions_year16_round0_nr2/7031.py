#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include <ctime>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<iomanip>
#include<cmath>
#define mst(ss,b) memset((ss),(b),sizeof(ss))
#define maxn 0x3f3f3f3f
#define MAX 1000100
///#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long ll;
typedef unsigned long long ull;
#define INF (1ll<<60)-1
using namespace std;
string s;
int vis[10010];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        mst(vis,0);
        cin>>s;
        int n=s.size();
        for(int i=n-1;i>=0;i--){
            if(s[i]=='-') vis[i]=-1;
            else vis[i]=1;
        }
        int t=n-1,ans=0;
        for(int i=t;i>=0;i--){
            if(vis[i]==1) continue;
            for(int j=0;j<=i;j++) vis[j]=-vis[j];
            ans++;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
