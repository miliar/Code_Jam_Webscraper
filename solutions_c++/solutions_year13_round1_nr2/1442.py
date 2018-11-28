#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

int v[11];
int dp[50][50][50];

void solve(){
    
    int e,r,n;
    cin >> e >> r >> n;
    for (int i=0;i<n;i++)
        cin >> v[i];

    r = min(r,e);
    int glo = 0;

    for (int x=0;x<e;x++)
        for (int y=0;y<=x;y++)
            dp[1][x][y] = -100000;//-10000000;

    for (int y=0;y<=e;y++)
    {
        dp[1][e][y] = y*v[0];
        glo = max(glo, dp[1][e][y]);
    }


    for (int i=2;i<=n;i++)
        for (int x=r;x<=e;x++)
            for (int y=0;y<=x;y++)
            {
                int best = dp[i-1][max(x-r,r)][r-x+max(x-r,r)];
                for (int j=max(x-r,r);j<=e;j++)
                    best = max(best,dp[i-1][j][j-x+r]);
                dp[i][x][y] = best + y *v[i-1];
                glo = max(dp[i][x][y] , glo);
            }

    cout << glo << '\n';

};

int main(){
    int t;
    cin >> t;
    for (int i=1;i<=t;i++)
    {
        cout << "Case #" << i << ": " ;
        solve();
    }
    return 0;
}
