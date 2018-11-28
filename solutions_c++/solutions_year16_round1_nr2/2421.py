#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define N 100
struct NODE
{
    int a[N];
}b[2*N],ans;
int n,flag;
bool cmp(NODE a,NODE b)
{
    return a.a[1]<b.a[1];
}
int c[N][N],vis[N],vis1[N];
int judge(int x)
{
    int i,j;
    int tmp=0;
    for(i=1;i<=2*n-1;i++)
    {
        tmp=1;
        if(vis1[i]==1)
            continue;
        for(j=1;j<=n;j++)
        {
            if(b[i].a[j]!=c[j][x])
            {
                tmp=0;
                break;
            }
        }
        if(!tmp)
            continue;
        vis1[i]=1;
        return 1;
    }
    for(j=1;j<=n;j++)
    {
        ans.a[j]=c[j][x];
    }
    return 0;
}
void dfs(int x,int len)
{
    int i,tmp=0;
    if(flag==1)
        return;
    if(len==n+1)
    {
        for(i=0;i<=2*n;i++)
            vis1[i]=vis[i];
        for(i=1;i<=n;i++)
        {
            if(!judge(i))
            {
                tmp++;
            }
            if(tmp>1)
                break;
        }
        if(tmp==1)
            flag=1;
        return;
    }
    if(x>2*n-1)
        return;
    dfs(x+1,len);
    vis[x]=1;
    for(i=1;i<=n;i++)
        c[len][i]=b[x].a[i];
    dfs(x+1,len+1);
    vis[x]=0;
}
int main()
{
    int T,i1=1;
    int i,j;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);flag=0;
        for(i=1;i<=2*n-1;i++)
        {
            for(j=1;j<=n;j++)
            {
                scanf("%d",&b[i].a[j]);
            }
        }
        sort(b+1,b+2*n,cmp);
        dfs(0,1);
        printf("Case #%d:",i1++);
        for(i=1;i<=n;i++)
        {
            printf(" %d",ans.a[i]);
        }
        printf("\n");
    }
    return 0;
}
