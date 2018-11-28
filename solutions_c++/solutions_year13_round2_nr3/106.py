#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <set>
#include <vector>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

vector<string> w;
string s;
int n;

int dp[5][10010];
int fr[5][10010];

int k, new_q;

bool calc(int q, int i, int j) {
    k = 0;
    new_q = q;
    if (i + int(w[j].length()) > n)
        return 0;
    forn(z, w[j].length())
        if (w[j][z] == s[i + z]) {
            new_q = max(0, new_q - 1);
        } else {
            if (new_q != 0)
                return 0;
            new_q = 4;
            k++;
        }
    return 1;
}

int main()
{
    freopen("input2.txt", "r", stdin);
    w.clear();
    while (cin >> s)
        w.push_back(s);
    fclose(stdin);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin.clear();
    cin >> T;
    forn(t, T) {
        printf("Case #%d: ", t + 1);

        cin >> s;
        n = s.length();
        forn(q, 5)
            forn(i, n + 1)
                dp[q][i] = -1;
        dp[0][0] = 0;

        forn(i, n)
            forn(q, 5)
                if (dp[q][i] != -1) {
                    forn(j, w.size()) {
                        if (!calc(q, i, j))
                            continue;
                        if (dp[new_q][i + w[j].length()] == -1 || dp[new_q][i + w[j].length()] > dp[q][i] + k) {
                            dp[new_q][i + w[j].length()] = dp[q][i] + k;
                            fr[new_q][i + w[j].length()] = j;
                        }
                    }
                }

        int ans = 100500;
        forn(q, 5)
            if (dp[q][n] != -1)
                ans = min(ans, dp[q][n]);
        printf("%d\n", ans);
    }
    return 0;
}
