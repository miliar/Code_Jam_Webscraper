#include <cstdio>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

const int X = 1010, INF = 1e3;
short int lst[X], ct[X], d[X], n;
int gans = INF;
int ts;

short int dp[X][X], gp[X][X + 10];

void build_gp()
{
    for (int i = 1; i < X; i++)
    {
        for (int j = 1; j <= X; j++)
        {
            gp[i][j] = i / j;
            if(i % j) gp[i][j]++;
        }
    }
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    build_gp();
    cin >> t;
    for (int test = 1; test <= t; test++)
    {
        int ans = INF;
        cin >> n;

        for (int i = 0; i < n; i++) cin >> lst[i];

        for (int cnt = 1; cnt < X; cnt++)
        {
            int gans = 0;
            for (int i = 0; i < n; i++)
            {
                gans += (lst[i] + cnt - 1) / cnt - 1;
            }
            ans = min(ans, cnt + gans);
            //cout << cnt << ' ' <<  gans << endl;
        }
        cout << "Case #" << test << ": " << ans << "\n";
    }
    return 0;
}
