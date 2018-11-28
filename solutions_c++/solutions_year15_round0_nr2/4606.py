#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <stdio.h>
#include <stack>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <set>
#include <iterator>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>
#include <iomanip>
#include <ctime>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define mp(a, b) make_pair(a, b)
#define sqr(x) ( (x) * (x) )
#define all(a) a.begin(), a.end()
#define ft first
#define sc second

typedef long long ll; 
typedef double ld;
typedef vector<int> vi; 
typedef vector<vi> vii; 
typedef pair<int, int> pii;

const int INF = 1e9;
const ll INF64 = 1e18;
const ld PI = acos(-1.0);
const int MOD = 1000000007;
const int N = 11;

int n;
int a[N];
int dp[N][N];
int ans;

int calc(int i, int j) {
    if (dp[i][j] != -1)
        return dp[i][j];

    int res = INF;
    for (int t = 1; t <= i; t++) {
        forn(g, j) {
            res = min(res, max(calc(i - t, j - g - 1), calc(t, g)));
        }
    }

    return dp[i][j] = res;
}

int cur1, cur2;

void rec(int pos) {
    if (cur1 + cur2 > ans) return;
    if (pos == n) {
        ans = cur1 + cur2;
    } else {
        forn(i, a[pos] + 1) {
            cur1 += i;
            int save = cur2;
            cur2 = max(cur2, dp[ a[pos] ][i]);
            rec(pos + 1);
            cur2 = save;
            cur1 -= i;
        }
    }
}

int main() {
//ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);   
//#endif

    memset(dp, -1, sizeof(dp));

    forn(i, N)
        dp[i][0] = i;

    forn(i, N) 
        forn(j, N)
            calc(i, j);

    int T;
    cin >> T;
    forn(t, T) {
        cin >> n;
        forn(i, n) 
            cin >> a[i];

        ans = INF;
        cur1 = 0;
        cur2 = 0;

        rec(0);

        cout << "Case #" << t + 1 << ": " << ans << endl;
    }

    return 0;
}