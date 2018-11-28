#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ull;
#define A first
#define B second
#define MP make_pair
#define PB push_back
deque<int> q;
const int maxn=20;
int bf[maxn];
bool vis[maxn];
int tmp[maxn],ans,n;
int judge(int cur)
{
    for(int i=0;i<cur;i++)
    {
        int p=(i+1)%cur;
        int l=(i-1+cur)%cur;
        if(bf[tmp[i]]!=tmp[l]&&bf[tmp[i]]!=tmp[p])
            return 0;
    }
    return cur;
}
void dfs(int cur)
{
    if(cur)
        ans=max(ans,judge(cur));
    if(cur>=n)    return;
    for(int i=1;i<=n;i++)
        if(!vis[i])
        {
            tmp[cur]=i;
            vis[i]=1;
            dfs(cur+1);
            vis[i]=0;
        }
}
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%d",&bf[i]);
        ans=0;
        memset(vis,0,sizeof(vis));
        dfs(0);
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
