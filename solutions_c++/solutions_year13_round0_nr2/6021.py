#include <stdio.h>

int main()
{
    
    //----------------------
    FILE *fp1, *fp2;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("result_2.txt","w",stdout);
    //----------------------
        
    
    int ii,nn;
    scanf("%d\n", &nn);
    for (ii=1;ii<=nn;ii++)
    {
        int i,j;
        int n,m;
        int a[101][101]={0};
        int b[101][101]={0};
        scanf("%d%d\n", &n, &m);
        for (i=1;i<=n;i++)
            for (j=1;j<=m;j++)
                scanf("%d", &a[i][j]);
        for (i=1;i<=n;i++)
        {
            int p=0;
            for (j=1;j<=m;j++)
                if (a[i][j]==1) p++;
            if (p==m) 
               for (j=1;j<=m;j++) b[i][j]=1;
        }
        for (j=1;j<=m;j++)
        {
            int p=0;
            for (i=1;i<=n;i++)
                if (a[i][j]==1) p++;
            if (p==n) 
               for (i=1;i<=n;i++) b[i][j]=1;
        }
        int f=0;
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=m;j++)
                if ((a[i][j]==1)&&(b[i][j]==0)){
                                                f=1;
                                                break;
                                                }
            if (f==1) break;
        }
        if (f==1) printf("Case #%d: NO\n", ii);
           else printf("Case #%d: YES\n", ii);
    }
    return 0;
}
