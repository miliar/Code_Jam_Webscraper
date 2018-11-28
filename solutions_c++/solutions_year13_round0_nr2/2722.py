#include<cstdio>
#include<cstring>

int a[100][100];
int b[100][100];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                scanf("%d",&a[i][j]);
        int ans=1;
        for (int k=1;k<=100;k++)
        {
            memset(b,0,sizeof(b));
            for (int i=0;i<n;i++)
                for (int j=0;j<m;j++)
                    if (a[i][j]<=k) b[i][j]=1;
            for (int i=0;i<n;i++)
            {
                int flag=1;
                for (int j=0;j<m;j++)
                    if (a[i][j]>k) flag=0;
                if (flag)
                    for (int j=0;j<m;j++)
                        b[i][j]=0;
            }
            for (int j=0;j<m;j++)
            {
                int flag=1;
                for (int i=0;i<n;i++)
                    if (a[i][j]>k) flag=0;
                if (flag)
                    for (int i=0;i<n;i++)
                        b[i][j]=0;
            }
            for (int i=0;i<n;i++)
                for (int j=0;j<m;j++)
                    if (b[i][j]) ans=0;
        }
        if (ans) printf("Case #%d: YES\n",t);
        else printf("Case #%d: NO\n",t);
    }
    
}
