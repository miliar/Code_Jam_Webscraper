#pragma comment (linker, "/STACK:128000000")
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

//typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int N = 1e3 + 200;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test, it;
int n, ans, mx;
int p[N];
int dp[N][N];

int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    scanf("%d", &test);
    for (int i = 1; i < N; i++)
        for (int j = 1; j < N; j++) {
            if (j >= i) {
                dp[i][j] = 0;
                continue;
            }
            dp[i][j] = INF;
            for (int k = 1; k < i; k++) dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j] + 1);
        }

    for (it = 1; it <= test; it++) {
        scanf("%d", &n);
        mx = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &p[i]);
            mx = max(mx, p[i]);
        }
        ans = INF;
        for (int border = 1; border <= mx; border++) {
            int cur = 0;
            for (int i = 0; i < n; i++) cur += dp[p[i]][border];
            ans = min(ans, cur + border);
        }
        printf("Case #%d: ", it);
        printf("%d\n", ans);
    }
    return 0;
}
