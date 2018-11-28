#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

struct node
{
    int next[30];
}tree[100010];

void init(int x)
{
    for(int i=0;i<26;i++)
        tree[x].next[i]=0;
}

char str[10][20];

int temp,cnt,m,num[10],bel[10],n,ans1,ans2;

void add(int k)
{
    int l=strlen(str[k]);
    int p=0,i;
    for(i=0;i<l;i++)
    {
        if(tree[p].next[str[k][i]-'A']==0)
        {
            temp++;
            tree[p].next[str[k][i]-'A']=++cnt;
            init(cnt);
            p=tree[p].next[str[k][i]-'A'];
        }
        else
            p=tree[p].next[str[k][i]-'A'];
    }
}

void dfs(int now)
{
    if(now==m+1)
    {
        memset(num,0,sizeof(num));
        int i,j;
        for(i=1;i<=m;i++)
        {
            num[bel[i]]++;
        }
        for(i=1;i<=n;i++)
        {
            if(num[i]==0)
                return;
        }
        temp=0;
        for(i=1;i<=n;i++)
        {
            temp++;
            cnt=0;
            init(0);
            for(j=1;j<=m;j++)
            {
                if(bel[j]==i)
                    add(j);
            }
        }
        if(temp>ans1)
        {
            ans1=temp;
            ans2=1;
        }
        else if(temp==ans1)
            ans2++;
        return;
    }
    for(int i=1;i<=n;i++)
    {
        bel[now]=i;
        dfs(now+1);
    }
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&m,&n);
        int i;
        ans1=0;
        for(i=1;i<=m;i++)
            scanf("%s",&str[i]);
        dfs(1);
        printf("Case #%d: %d %d\n",++cas,ans1,ans2);
    }
    return 0;
}
