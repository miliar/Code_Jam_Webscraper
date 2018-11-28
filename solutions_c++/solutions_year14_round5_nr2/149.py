#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <ext/rope>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <ratio>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<double, int> pdi;

const int INF = 0x3f3f3f3f;
const int MAXN = 100;
const int MAXM = 100;
const int MOD = 1000000007;
const ll INFLL = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-8;
const double PI = acos(-1.0);

#define DEBUG(args...) fprintf(stderr, args)
#define all(c) (c).begin(), (c).end()
#define pb push_back

template<typename U, typename V> void add(U& ret, const V& val) { ret = (ll)(ret + val) % MOD; }
template<typename U, typename V> void chkmax(U& ret, const V& val) { if (ret < val) { ret = val; } }
template<typename U, typename V> void chkmin(U& ret, const V& val) { if (val < ret) { ret = val; } }
template<typename T> T gcd(T a, T b) { return a == 0 ? b : gcd(b % a, a); }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

int P, Q, n;
int h[MAXN], g[MAXN];
ll res;

void init() {
}

void input() {
    scanf("%d%d%d", &P, &Q, &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", &h[i], &g[i]);
    }
}

void solve() {
    const int LIMIT = 30000;
    vector<ll> dp(LIMIT, -1LL);
    dp[1] = 0;
    for (int i = 0; i < n; ++i) {
        int nq = (h[i] - 1) / Q;
        int np = (h[i] - nq * Q + P - 1) / P;
        int d = nq - np;
        int t = nq + 1;
        vector<ll> tmp(LIMIT, -1LL);
        for (int j = 0; j < LIMIT; ++j) {
            if (dp[j] == -1) {
                continue;
            }
            if (j + d >= 0 && j + d < LIMIT) {
                chkmax(tmp[j + d], dp[j] + g[i]);
            }
            if (j + t < LIMIT) {
                chkmax(tmp[j + t], dp[j]);
            }
        }
        dp.swap(tmp);
    }

    res = 0;
    for (int i = 0; i < LIMIT; ++i) {
        chkmax(res, dp[i]);
    }
}


int main(int argc, char** argv) {
    int totalCaseNumber = 1;

    init();

    scanf("%d", &totalCaseNumber);
    for (int caseNum = 1; caseNum <= totalCaseNumber; ++caseNum) {
        input();
        solve();
        printf("Case #%d: %lld\n", caseNum, res);
    }

    return 0;
}
