#include <stdio.h>
#include <string.h>

int a[20][20];
int m, n;

int calcX(int x)
{
    int i, sum=0;
    for(i=0;i<m;i++)
        sum+=a[x][i];
    return sum;
}

int calcY(int y)
{
    int i, sum=0;
    for(i=0;i<n;i++)
        sum+=a[i][y];
    return sum;
}

int judge()
{
    int i, j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i][j]==1)
            {
                if(calcX(i)==m) continue;
                if(calcY(j)==n) continue;
                return 0;
            }
        }
    }
    return 1;
}

int main()
{
    int t, test, i, j;
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for(test=1;test<=t;test++)
    {
        scanf("%d%d",&n, &m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
                scanf("%d",&a[i][j]);
        }
        printf("Case #%d: ", test);
        if(judge()==0) printf("NO\n");
        else printf("YES\n");


    }
    return 0;
}
