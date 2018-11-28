#include<stdio.h>
#include<string.h>
int a[200][200];
int n,m;
int main()
{
    freopen("bb.in","r",stdin);
    freopen("bb.out","w",stdout);
    int T,aa,can,i,j,k,f1,f2;
    scanf("%d",&T);
    for (aa=1; aa<=T; aa++)
    {
        scanf("%d%d",&n,&m);
        for (i=1; i<=n; i++)
            for (j=1; j<=m; j++) scanf("%d",&a[i][j]);
        can=1;
        for (i=1; i<=n; i++)
        {
            for (j=1; j<=m; j++)
            {
                f1=f2=0;
                for (k=1; k<=m; k++)
                    if (a[i][j]<a[i][k]) f1=1;
                for (k=1; k<=n; k++)
                    if (a[i][j]<a[k][j]) f2=1;
                if (f1&&f2) can=0;
            }
        }
        if (can) printf("Case #%d: YES\n",aa);
        else printf("Case #%d: NO\n",aa);
    }
    return 0;
}
