#include <map>
#include <set>
#include <queue>
#include <ctime>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define LL long long
#define N 10
using namespace std;
int cnt,num,rt[N],n,m,ans=0,gp[N];
int son[100][26];
void add(int &x,char *s)
{
    if (x==0)
        x=++cnt;
    if (*s==0) return;
    add(son[x][(*s)-'A'],s+1);
}
char str[N][11];
void dfs(int d)
{
    if (d==n)
    {
        cnt=0;
        memset(rt,0,sizeof rt);
        memset(son,0,sizeof son);
        for (int i=0;i<d;i++)
            add(rt[gp[i]],str[i]);
        if (cnt>ans)
        {
            ans=cnt;
            num=1;
        }
        else if (cnt==ans)
            num++;
        return;
    }
    for (int i=0;i<m;i++)
    {
        gp[d]=i;
        dfs(d+1);
    }
}
int main()
{
    freopen("D.in","r",stdin);
    freopen("D.txt","w",stdout);
    int run;
    scanf("%d",&run);
    for (int cas=1;cas<=run;cas++)
    {
        scanf("%d%d",&n,&m);
        getchar();
        for (int i=0;i<n;i++)
            scanf("%s",str[i]);
        ans=0;
        dfs(0);
        printf("Case #%d: %d %d\n",cas,ans,num);
    }
    return 0;
}

