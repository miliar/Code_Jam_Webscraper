#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,m,t;
bool map[120][120];
int data[120][120];
void solve()
{
    for(int i=0; i<n; i++)
    {
        int f=1;
        for(int j=0; j<m; j++)
            if(data[i][j]==2)
            {
                f=0;
                break;
            }
        if(f)
            for(int j=0; j<m; j++)
                map[i][j]=1;
    }
    for(int i=0; i<m; i++)
    {
        int f=1;
        for(int j=0; j<n; j++)
            if(data[j][i]==2)
            {
                f=0;
                break;
            }
        if(f)
            for(int j=0; j<n; j++)
                map[j][i]=1;
    }
}
bool judge()
{
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            if(data[i][j]==1&&!map[i][j])
                return 0;
    return 1;
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int s=0;
    cin>>t;
    while(t--)
    {
        memset(map,0,sizeof(map));
        cin>>n>>m;
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                cin>>data[i][j];
        solve();
        printf("Case #%d: ",++s);
        /*if(s==54)
        {for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            cout<<data[i][j]<<" ";
            cout<<endl;
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            if(map[i][j])
            cout<<1<<" ";
            else
            cout<<0<<" ";
            cout<<endl;
        }
        }*/
        if(judge())
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}
