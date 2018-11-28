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
long double dp[222][222];
int n, k, m;
long double p[2020], b[2020];
bool was[222][222];

long double calc(int x, int y) {
    int ind = m - x - y;
    if (x < 0 || y < 0) return 0.0;
    if (ind == m) {
        if (x || y) return 0.0;
        return 1.0;
    }
    long double &res = dp[x][y];
    if (was[x][y]) return res;
    was[x][y] = 1;
    res = b[ind] * calc(x - 1, y) + (1.0 - b[ind]) * calc(x, y - 1);
    return res;
}

void clear() {
    for (int i = 0; i <= k; i++)
        for (int j = 0; j <= k / 2; j++)
            was[i][j] = 0;
}

long double calc(int pos) {
    if (pos + k > n) return 0.0;
    m = 0;
    for (int i = pos; i < pos + k; i++)
        b[m++] = p[i];
    clear();
    return calc(k / 2, k / 2);
}

void solve(int num) {
    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> p[i];
    sort(p, p + n);
    long double ans = 0.0;
    for (int i = 0; i < n; i++)
        ans = max(ans, calc(i));
    for (int i = 0; i < n; i++) {
        if (i > k) continue;
        m = 0;
        for (int j = 0; j < i; j++) b[m++] = p[j];
        for (int j = n - (k - i); j < n; j++) b[m++] = p[j];
        clear();
        ans = max(ans, calc(k / 2, k / 2));
    }
    /*
    for (int i = 0; i <= n; i++) {
        if (i > k) continue;
        for (int j = i; j < n; j++) {
            for (int jj = j; jj < n; jj++) {
                if (jj - j + 1 + i > k) continue;
                int rest = k - (jj - j + 1) - i;
                if (n - rest > jj) {
                    m = 0;
                    for (int r = 0; r < i; r++) b[m++] = p[r];
                    for (int r = j; r <= jj; r++) b[m++] = p[r];
                    for (int r = n - rest; r < n; r++) b[m++] = p[r];
                    clear();
                    assert(m == k);
                    ans = max(ans, calc(k / 2, k / 2));
                }
            }
        }
    }
    */
    printf("Case #%d: %.9f\n", num, double(ans));
}

int main(){
    
    cin >> T;
    
    for (int i = 1; i <= T; i++) {
        solve(i);
    }
    
    return 0;
}
