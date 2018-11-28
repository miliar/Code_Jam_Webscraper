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
int mp[2010];
double mp2[2010];
int p[200],ansp[200];
int r,m,n,k;
double ans;
void dfs(int now,int end)
{
    if (now==end)
    {
        for (int i=0;i<2010;i++)
            mp2[i]=0;
        for (int i=0;i<(1<<end);i++)
        {
            int mul=1;
            for (int j=0;j<end;j++)
                if (i&(1<<j)) mul*=p[j];
            mp2[mul]++;
        }
        for (int i=0;i<2010;i++)
        {
            mp2[i]*=1.0*k;
            mp2[i]/=(1<<end);
        }
        double tdis=0;
        for (int i=0;i<2010;i++)
            tdis+=fabs(mp2[i]-mp[i]);
        if (tdis<ans||ans<-100)
        {
            ans=tdis;
            for (int i=0;i<end;i++)
                ansp[i]=p[i];
        }
        return;
    }
    for (int i=2;i<=m;i++)
    {
        p[now]=i;
        dfs(now+1,end);
    }
    return;
}
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-1-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        printf("Case #%d:\n",ii);
        scanf("%d%d%d%d",&r,&n,&m,&k);
        while (r--)
        {
            ans=-2000;
            memset(mp,0,sizeof(mp));
            for (int i=0;i<k;i++)
            {
                int val;
                scanf("%d",&val);
                mp[val]++;
            }
            dfs(0,n);
            for (int i=0;i<n;i++)
                printf("%d",ansp[i]);
            puts("");
        }
    }
    return 0;
}

