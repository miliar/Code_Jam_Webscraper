#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int mp[110][110];
int n,m;
int mk[110][110];
int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",cas++);
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                scanf("%d",&mp[i][j]);
                mk[i][j]=100;
            }
        int MX = 0;
        for(int i=0;i<n;i++)
        {
            MX = 0;
            for(int j=0;j<m;j++)
                MX = MX > mp[i][j] ? MX : mp[i][j] ;
            for(int j=0;j<m;j++)
                mk[i][j] = mk[i][j] > MX ? MX : mk[i][j];
        }
        for(int j=0;j<m;j++)
        {
            MX = 0;
            for(int i=0;i<n;i++)
                MX = MX > mp[i][j] ? MX : mp[i][j];
            for(int i=0;i<n;i++)
                mk[i][j] = mk[i][j] > MX ? MX : mk[i][j];
        }
        bool fg = true;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(mp[i][j] != mk[i][j]) fg = false;
        if(fg) puts("YES");
        else puts("NO");
    }

    return 0;
}
