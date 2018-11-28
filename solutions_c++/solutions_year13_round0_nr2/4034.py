#include <iostream>
int a[110][110];
bool f[110][110];
int main()
{
    FILE *fp_in = fopen("B-large.in","r");
    FILE *fp_out = fopen("2out.txt","w");
    int t;
    fscanf(fp_in,"%d",&t);
    int m,n;
    for (int tt = 1; tt <= t ;tt++)
    {
        memset(a,0,sizeof(a));
        int s = 0;
        fscanf(fp_in,"%d%d",&m,&n);
        for (int i = 1 ;i <= m ;i++)
        {
            for (int j =1 ;j <=n ;j++)
            {
                fscanf(fp_in,"%d",&a[i][j]);
            }
        }
        memset(f,false,sizeof(f));
        for (int i = 1 ;i <= m ;i++)
        {
            int x = 0;
            for (int j =1 ;j <=n ;j++)
            {
                if (a[i][j] > x)
                {
                            x = a[i][j];
                }
            }
            for (int j = 1;j <=n ;j++)
            {
                if (a[i][j] == x)
                   f[i][j] = true;
            }
        }
        for (int j = 1 ;j<=n ;j++)
        {
            int x = 0;
            for (int i =1 ;i <=m ;i++)
            {
                if (a[i][j] > x)
                {
                            x = a[i][j];
                }
            }
            for (int i =1 ;i <=m ;i++)
            {
                if (a[i][j] == x)
                   f[i][j] = true;
            }
        }
        bool flag = true;
        for (int i = 1 ;i <=m ;i++)
            for (int j =1 ; j <= n;j++)
                if (!f[i][j])
                {
                             flag = false;
                }

                
        if (!flag)
        {
                 fprintf(fp_out,"Case #%d: NO\n",tt);
        }
        else
        {
            fprintf(fp_out,"Case #%d: YES\n",tt);
        }
    }
    fclose(fp_out);
}
