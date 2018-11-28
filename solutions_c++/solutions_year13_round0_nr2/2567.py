#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <queue>

#define X first
#define Y second
#define ll long long

using namespace std;

int mas[110][110], n, m, h[110], v[110];
void solve(int tt)
{
     cin>>n>>m;
     for (int i=1; i<=n; i++)
         for (int j=1; j<=m; j++)
             cin>>mas[i][j];
     printf("Case #%d: ", tt);
     if ( n==1 || m==1 )
     {
        cout<<"YES"<<endl;     
        return ;
     }
     for (int i=1; i<=n; i++)
         h[i]=mas[i][1];
     for (int i=1; i<=m; i++)
         v[i]=mas[1][i];
     for (int i=1; i<=n; i++)
         for (int j=1; j<=m; j++)
             h[i]=max( h[i], mas[i][j] ), v[j]=max(v[j], mas[i][j]);
     for (int i=1; i<=n; i++)
     {
         for (int j=1; j<=m; j++)    
         {
             if ( mas[i][j]<h[i] && mas[i][j]<v[j] )
             {
                cout<<"NO"<<endl;
                return ;     
             }    
         }
     }
     cout<<"YES"<<endl;
}
int main ()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int test;
    cin>>test;
    for (int i=1; i<=test; i++)
    {
        solve(i);    
    }
    return 0;
}
