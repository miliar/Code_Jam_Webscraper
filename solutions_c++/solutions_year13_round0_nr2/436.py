#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>

#define N 100009
#define ll long long

using namespace std;

int n,m,a[109][109];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    cin>>T;
    while(T--)
    {
        cin>>n>>m;
        for(int i=1;i<=n;i++) a[i][0]=0;
        for(int j=1;j<=m;j++) a[0][j]=0;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
            {
                cin>>a[i][j];
                a[i][0]=max(a[i][0],a[i][j]);
                a[0][j]=max(a[0][j],a[i][j]);
            }
        int flag=0;
        for(int i=1;!flag&&i<=n;i++)
            for(int j=1;!flag&&j<=m;j++)
            {
                int t=min(a[i][0],a[0][j]);
                if(t!=a[i][j])
                    flag=1;
            }
        printf("Case #%d: ",++cas);
        flag?puts("NO"):puts("YES");
    }

    fclose(stdout);
    return 0;
}
