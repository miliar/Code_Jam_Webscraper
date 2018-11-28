#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (800000007)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
int n,k;
int ans;
bool flag;
int s[110],t;
struct Node
{
    int v[110],tot;
    char str[110],str1[110];
}node[110];
void work(int id)
{
    node[id].tot=0;
    int o=strlen(node[id].str);
    for(int i=0;i<o;i++)
    {
        if(i==0||node[id].str[i]!=node[id].str[i-1])
        {
            node[id].tot++;
            node[id].str1[node[id].tot]=node[id].str[i];
            node[id].v[node[id].tot]=1;
        }else node[id].v[node[id].tot]++;
    }
}
void check(int id)
{
    if(node[id].tot!=node[1].tot) flag=false;//printf("%d %d..\n",node[id].tot,node[1].tot);}
    else
    {
        for(int i=1;i<=node[1].tot;i++)
        if(node[id].str1[i]!=node[1].str1[i]) flag=false;//printf("%d %c %c..\n",i,node[id].str1[i],node[1].str1[i]);}
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    int cas=0;
    scanf("%d",&T);
    while(T--)
    {
        ans=0;flag=true;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        scanf("%s",&node[i].str);
        for(int i=1;i<=n;i++)
        work(i);//printf("%d :%d***\n",i,node[i].tot);}
        for(int i=2;i<=n;i++)
        check(i);
        k=node[1].tot;
        for(int i=1;i<=k;i++)
        {
            for(int j=1;j<=n;j++)
            s[j]=node[j].v[i];
            sort(s+1,s+1+n);
            t=s[(n+1)/2];
            for(int j=1;j<=n;j++)
            ans+=max(s[j]-t,t-s[j]);
        }
        if(!flag) printf("Case #%d: Fegla Won\n",++cas);
        else printf("Case #%d: %d\n",++cas,ans);
    }

    return 0;
}
