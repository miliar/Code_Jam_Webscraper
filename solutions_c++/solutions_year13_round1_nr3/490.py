#include <stdio.h>
#include <algorithm>
#define MAX 13

using namespace std;

bool sol;
int r,n,m,k,val[MAX],inp[MAX],ans[MAX],min1;

void btrack(int x)
{
    int i,j,max1,pro,cnt,k;
    bool d;
    if (x==n)
    {
        max1=0;
        for (i=0;i<k;i++)
        {
            d=0;
            for (j=0;j<(1<<n);j++)
            {
                pro=1;
                cnt=0;
                for (k=0;k<n;k++)
                {
                    if (j&(1<<k))
                    {
                        pro*=val[k];
                        cnt++;
                    }
                }
                if (pro==inp[i])
                {
                    max1=max(max1,cnt);
                    d=1;
                }
            }
            if (!d) break;
        }
        if (i<k) return ;
        if (!sol)
        {
            min1=max1;
            for (i=0;i<n;i++) ans[i]=val[i];
            sol=1;
        }
        else if (max1<min1)
        {
            min1=max1;
            for (i=0;i<n;i++) ans[i]=val[i];
        }
        return ;
    }
    for (i=2;i<=m;i++)
    {
        val[x]=i;
        btrack(x+1);
    }
}

int main()
{
    freopen("cin.txt","r",stdin);
    freopen("cout.txt","w",stdout);
    int test,i,cas;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d%d%d%d",&r,&n,&m,&k);
        printf("Case #1:\n");
        while (r--)
        {
            for (i=0;i<k;i++) scanf("%d",&inp[i]);
            sol=0;
            for (i=0;i<n;i++) ans[i]=2;
            btrack(0);
            for (i=0;i<n;i++) printf("%d",ans[i]);
            printf("\n");
        }
    }
    return 0;
}
