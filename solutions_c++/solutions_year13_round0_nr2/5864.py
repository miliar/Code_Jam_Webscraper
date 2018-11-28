#include <iostream>
#include <cstdio>
using namespace std;

int n,m,a[111][111];

bool col(int x,int y,int mode)
{
    int i;
    if(mode==0)
    {
        for(i=1;i<=n;i++)
        if(a[i][y]>a[x][y])
            return false;
        return true;
    }
    else
    {
        for(i=1;i<=m;i++)
        if(a[x][i]>a[x][y])
            return false;
        return true;
    }
}

bool ok()
{
    int i,j;
    for(i=1;i<=n;i++)
    for(j=1;j<=m;j++)
    if(col(i,j,0)==false && col(i,j,1)==false)
        return false;
    return true;
}

int main()
{
    int cases,o,i,j;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&cases);
    for(o=1;o<=cases;o++)
    {
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)
            scanf("%d",&a[i][j]);
        printf("Case #%d: ",o);
        if(ok())
            printf("YES\n");
        else
            printf("NO\n");

    }
    return 0;
}
