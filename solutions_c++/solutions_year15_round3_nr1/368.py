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

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int N = 1e5 + 200;
const int INF = int(1e9);
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test, it;
int r, c, w, ans;
int dp[55][2];

int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    cin >> test;
    for (it = 1; it <= test; it++) {
        cin >> r >> c >> w;
        dp[c][0] = c / w;
        dp[c][1] = c / w + w - 1;
        if (c % w) dp[c][1]++;
        ans = (r - 1) * dp[c][0] + dp[c][1];
        printf("Case #%d: ", it);
        printf("%d\n", ans);
    }
    return 0;
}
