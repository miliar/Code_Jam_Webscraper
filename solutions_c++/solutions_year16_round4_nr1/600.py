#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

const int Maxn = 12;

int f[Maxn + 1][3];
string line[Maxn + 1][3];

int main()
{
    f[0][0] = 1;
    f[0][1] = 0;
    f[0][2] = 0;
    line[0][0] = "P";
    line[0][1] = "R";
    line[0][2] = "S";
    for (int i = 1; i <= Maxn; ++i)
    {
        f[i][0] = f[i - 1][0] + f[i - 1][2];
        f[i][1] = f[i - 1][0] + f[i - 1][1];
        f[i][2] = f[i - 1][1] + f[i - 1][2];
        line[i][0] = min(line[i - 1][0] + line[i - 1][1], line[i - 1][1] + line[i - 1][0]);
        line[i][1] = min(line[i - 1][1] + line[i - 1][2], line[i - 1][2] + line[i - 1][1]);
        line[i][2] = min(line[i - 1][0] + line[i - 1][2], line[i - 1][2] + line[i - 1][0]);
    }
    
    int T, n, r, p, s;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt)
    {
        cin >> n >> r >> p >> s;
        string ans = "Z";
        if (p == f[n][0] && r == f[n][1] && s == f[n][2])
            ans = line[n][0];
        if (r == f[n][0] && s == f[n][1] && p == f[n][2])
            ans = min(ans, line[n][1]);
        if (s == f[n][0] && p == f[n][1] && r == f[n][2])
            ans = min(ans, line[n][2]);
        if (ans == "Z")
            ans = "IMPOSSIBLE";
        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}

