#include <iostream>
#include <algorithm>
#include <cstring>
#include <stdio.h>
using namespace std;
char mp[301][301];
int row[301];
int col[301];
bool imp(int n,int m)
{
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
        {
            if (mp[i][j]!='.')
            {
                if (row[i]==1 && col[j]==1)
                    return 1;
            }
        }
    }
    return 0;
}
int main()
{
    freopen("out.txt","w",stdout);
    int oOo;
    cin>>oOo;
    for (int Oo=1;Oo<=oOo;Oo++)
    {
        int n,m;
        cin>>n>>m;
        for (int i=0;i<100;i++)
        {
            row[i]=col[i]=0;
        }
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                cin>>mp[i][j];
                if (mp[i][j]!='.')
                    row[i]++,col[j]++;
            }
        }
        cout<<"Case #"<<Oo<<": ";
        if (imp(n,m))
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        int ans=0;
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                if (mp[i][j]=='>')
                {
                    int x=j+1;
                    while(x<m && mp[i][x]=='.')
                        x++;
                    if (x==m)
                        ans++;
                }
                if (mp[i][j]=='<')
                {
                    int x=j-1;
                    while(x>=0 && mp[i][x]=='.')
                        x--;
                    if (x==-1)
                        ans++;
                }
                if (mp[i][j]=='^')
                {
                    int x=i-1;
                    while(x>=0 && mp[x][j]=='.')
                        x--;
                    if (x==-1)
                        ans++;
                }
                if (mp[i][j]=='v')
                {
                    int x=i+1;
                    while(x<n && mp[x][j]=='.')
                        x++;
                    if (x==n)
                        ans++;
                }
            }
        }
        cout<<ans<<endl;
    }
}

