#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

const int N = 12;
string f[N + 1][3];

int main()
{
    f[0][0] = "R", f[0][1] = "P", f[0][2] = "S";
    for (int i = 1; i <= N; ++i) {
        for (int j = 0; j < 3; ++j) {
            f[i][j] = min(f[i - 1][j] + f[i - 1][(j + 2) % 3],
                          f[i - 1][(j + 2) % 3] + f[i - 1][j]);
        }
    }
    int dat;
    scanf("%d", &dat);
    for (int cas = 1; cas <= dat; ++cas) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        string ans = "Z";
        for (int i = 0; i < 3; ++i) {
            int R = 0, P = 0, S = 0;
            for (char c: f[n][i]) {
                switch (c) {
                    case 'R': ++R; break;
                    case 'P': ++P; break;
                    case 'S': ++S; break;
                }
            }
            if (R == r && P == p && S == s) {
                ans = min(ans, f[n][i]);
            }
        }
        if (ans == "Z") ans = "IMPOSSIBLE";
        printf("Case #%d: %s\n", cas, ans.c_str());
    }
}
