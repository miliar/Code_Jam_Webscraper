#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int n,m;
    int T;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("test.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        cin>>n>>m;
        int a[200][200],b[200][200];
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                cin>>a[i][j];
            }
        }
        for(int i=1;i<=n;i++)
        {
            int max=0;
            for(int j=1;j<=m;j++)
            {
                max=max>a[i][j]?max:a[i][j];
            }

            for(int j=1;j<=m;j++)
            b[i][j]=max;

        }
        for(int i=1;i<=m;i++)
        {
            int max=0;
            for(int j=1;j<=n;j++)
            {
                max=max>a[j][i]?max:a[j][i];
            }
            for(int j=1;j<=n;j++)
            b[j][i]=max>b[j][i]?b[j][i]:max;
        }
        int bo=1;
        for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++)
        {

            if(a[i][j]!=b[i][j])
            bo=0;
        }
       }
        if(bo==1)
        {
            printf("Case #%d: YES\n",cas);
        }
        else
        printf("Case #%d: NO\n",cas);

    }
    return 0;
}
