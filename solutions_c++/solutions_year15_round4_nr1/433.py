#include <bits/stdc++.h>

using namespace std;

#define lol long long
#define fi first
#define se second
#define pb push_back
#define sz(s) (lol)s.size()
#define must ios_base::sync_with_stdio(0)

#define inp(s) freopen(s, "r", stdin)
#define out(s) freopen(s, "w", stdout)

char d[110][110];
int s[110][110];
int a[10000];
int ss[10000];

int getsum(int i, int j, int ii, int jj) {
    return s[i][j] - s[ii - 1][j] - s[i][jj - 1] + s[ii - 1][jj - 1];
}

int main() {
    inp("input.txt");
    out("output.txt");
    int tt, t;
    cin >> t;
    a['<'] = 1;
    a['>'] = 2;
    a['^'] = 3;
    a['v'] = 4;
    for(tt = 1; tt <= t; tt++) {
        int r, c, i, j;
        cin >> r >> c;
        cout << "Case #" << tt << ": ";
        memset(s, 0, sizeof(s));
        for(i = 1; i <= r; i++)
            for(j = 1; j <= c; j++) {
                cin >> d[i][j];
                s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1];
                if(d[i][j] != '.')
                    s[i][j]++;
            }
//        for(i = 1; i <= r; i++, cout << "\n")
//            for(j = 1; j <= c; j++)
//                cout << s[i][j] << ' ';
        int ans = 0;
        for(i = 1; i <= r; i++) {
            for(j = 1; j <= c; j++) {
                if(d[i][j] == '.')
                    continue;
//                cout << i << ' ' << j << "\n";
                ss[1] = getsum(i, j, i, 1) - 1;
                ss[2] = getsum(i, c, i, j) - 1;
                ss[3] = getsum(i, j, 1, j) - 1;
                ss[4] = getsum(r, j, i, j) - 1;
//                cout << "\t" << ss[1] << ' ' << ss[2] << ' ' << ss[3] << " " << ss[4] << "\n";
                if(ss[a[d[i][j]]] > 0)
                    continue;
                if(ss[1] + ss[2] + ss[3] + ss[4] == 0) {
                    if(ans >= 0)
                        cout << "IMPOSSIBLE\n";
                    ans = -100000000000;
                    break;
                }
                ans++;

            }
        }
        if(ans >= 0)
            cout << ans << "\n";
    }
}
