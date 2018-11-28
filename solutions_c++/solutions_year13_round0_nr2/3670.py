#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int map[200][200];
int maxl[200][200];
int maxr[200][200];
int maxu[200][200];
int maxd[200][200];

int main()
{
    //freopen("D:\\in.txt","r",stdin);
    //freopen("D:\\out.txt","w",stdout);
    int t,n,m;
    scanf("%d",&t);
    for(int cas=1; t--; cas++)
    {

        memset(map,0,sizeof(map));
        memset(maxl,0,sizeof(maxl));
        memset(maxr,0,sizeof(maxr));
        memset(maxu,0,sizeof(maxu));
        memset(maxd,0,sizeof(maxd));

        scanf("%d%d",&n,&m);
        for(int i=1; i<=n; i++)
            for(int j=1; j<=m; j++)
                scanf("%d",&map[i][j]);


        for(int i=1; i<=n; i++)
            for(int j=1; j<=m; j++)
            {
                maxl[i][j]=max(maxl[i][j-1],map[i][j-1]);
            }

        for(int i=1; i<=n; i++)
            for(int j=m; j>=1; j--)
            {
                maxr[i][j]=max(maxr[i][j+1],map[i][j+1]);
            }

        for(int i=1; i<=m; i++)
            for(int j=1; j<=n; j++)
            {
                maxu[j][i]=max(maxu[j-1][i],map[j-1][i]);
            }

        for(int i=1; i<=m; i++)
            for(int j=n; j>=1; j--)
            {
                maxd[j][i]=max(maxd[j+1][i],map[j+1][i]);
            }


        bool flag=true;
        for(int i=1; i<=n && flag; i++)
            for(int j=1; j<=m && flag; j++)
            {
                if((map[i][j]<max(maxl[i][j],maxr[i][j])) && (map[i][j]<max(maxu[i][j],maxd[i][j])))
                {
                    flag=false;
                    break;
                }
            }
        /*
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                cout<<map[i][j]<<"";
            }
            cout<<endl;
        }
        */

        if(flag) printf("Case #%d: YES\n",cas);
        else printf("Case #%d: NO\n",cas);
    }
}
