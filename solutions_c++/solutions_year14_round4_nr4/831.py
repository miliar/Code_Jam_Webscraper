#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;
#define inf  1000000000
struct trie
{
    int go[26];
    void init()
    {
        memset(go,0,sizeof(go));
    }
}node[1000010];
int tot;
void init()
{
    node[0].init();
    tot=0;
}
void insert(char *str)
{
    int p=0;
    int len=strlen(str);
    for(int i=0;i<len;i++)
    {
        int index=str[i]-'A';
        if(node[p].go[index]==0)
        {
            node[++tot].init();
            node[p].go[index]=tot;
        }
        p=node[p].go[index];
    }
}
char str[10][110];
int vis[10];
int sum[1<<17];
int m,n,ans=0,num=0;
void solve()
{
    int tmp=0;
    for(int i=1;i<=n;i++)
    {
        init();
        int tru=0;
        for(int j=1;j<=m;j++)
        {
             if(vis[j]==i)
             {
                 tru=1;
                 insert(str[j]);
             }
        }
        tmp+=tot+tru;
    }
    sum[num++]=tmp;
    ans=max(ans,tmp);
}
void dfs(int now)
{
    if(now>m)
    {
         solve();
         return;
    }
    for(int i=1;i<=n;i++)
    {
        vis[now]=i;
        dfs(now+1);
        vis[now]=-1;
    }
}
int main()
{
    freopen("dd2.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int ncase,T=0;
    scanf("%d",&ncase);
    while(ncase--)
    {
        num=0;
        printf("Case #%d: ",++T);
        scanf("%d%d",&m,&n);
        for(int i=1;i<=m;i++)
        {
            scanf("%s",str[i]);
        }
        ans=0;
        dfs(1);
        int S=0;
        printf("%d ",ans);
        for(int i=0;i<num;i++)
        if(sum[i]==ans)
        S++;
        printf("%d\n",S);
    }
	return 0;
}
