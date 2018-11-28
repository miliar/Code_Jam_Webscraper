#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        int bd[111][111];
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&bd[i][j]);
        int f=0;
        for(int i=1;i<=100&&!f;i++)
        {
            int vis[111][111]={0};
            for(int j=0;j<n;j++)
            {
                int cnt=0;
                for(int k=0;k<m;k++)
                    if(bd[j][k]<=i)
                        cnt++;
                if(cnt==m)
                    for(int k=0;k<m;k++)
                        vis[j][k]=1;

            }

            for(int j=0;j<m;j++)
            {
                int cnt=0;
                for(int k=0;k<n;k++)
                    if(bd[k][j]<=i)
                        cnt++;
                if(cnt==n)
                    for(int k=0;k<n;k++)
                        vis[k][j]=1;
            }

            for(int j=0;j<n;j++)
                for(int k=0;k<m;k++)
                    if(bd[j][k]==i&&!vis[j][k])
                        f=1;
        }

        if(!f)
            printf("Case #%d: YES\n",c);
        else
            printf("Case #%d: NO\n",c);
    }
    return 0;
}
