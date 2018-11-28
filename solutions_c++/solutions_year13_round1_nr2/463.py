#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
int Ans;
int r,E,n;
int v[100];
void dfs(int now,int end,int e,int val)
{
    if (now==end)
    {
        Ans=max(Ans,val);
        return;
    }
    for (int i=0;i<=e;i++)
    {
        dfs(now+1,end,min(E,e-i+r),val+v[now]*i);
    }
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        scanf("%d%d%d",&E,&r,&n);
        for (int i=0;i<n;i++)
            scanf("%d",&v[i]);
        Ans=0;
        dfs(0,n,E,0);
        printf("Case #%d: %d\n",ii,Ans);
    }
    return 0;
}

