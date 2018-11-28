#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

int T;
int n;
string a[100100];
vector <pii> v;
int dp[110][110];

int dfs(int peoples, int machines) {
    if (peoples == (1 << n) - 1) {
        return 1;
    }
    int &res = dp[peoples][machines];
    if (res != -1) return res;
    res = 1;
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (!((1 << i)&peoples)) {
            for (int j = 0; j < n; j++) {
                if (!((1 << j)&machines)) {
                    if (a[i][j] == '1') {
                        cnt++;
                        res &= dfs(peoples^(1 << i), machines^(1 << j));
                    }
                }
            }
        }
    }
    if (cnt == 0) return res = 0;
    return res;
}

bool ok() {
    memset(dp, -1, sizeof dp);
    return dfs(0, 0);
}

void solve(int num) {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    v.clear();
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (a[i][j] == '0') v.pb(mp(i, j));
        }
    int ans = v.size();
    for (int mask = 0; mask < (1 << sz(v)); mask++) {
        for (int i = 0; i < sz(v); i++) {
            if ((1 << i)&mask) {
                pii p = v[i];
                a[p.f][p.s] = '1';
            }
        }
        if (ok()) ans = min(ans, __builtin_popcount(mask));
        for (int i = 0; i < sz(v); i++) {
            if ((1 << i)&mask) {
                pii p = v[i];
                a[p.f][p.s] = '0';
            }
        }
    }
    printf("Case #%d: %d\n", num, ans);
}

int main(){
    cin >> T;

    for (int i = 1; i <= T; i++)
        solve(i);

    return 0;
}
