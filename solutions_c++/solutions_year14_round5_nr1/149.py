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
const int MAXN = 1000000;
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

int n, p, q, r, s;
ll a[MAXN];
ll b[MAXN + 1];
double res;

void init() {
}

void input() {
    scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
}

void solve() {
    b[0] = 0;
    for (int i = 0; i < n; ++i) {
        a[i] = ((ll)i * p + q) % r + s;
        b[i + 1] = b[i] + a[i];
    }

    //printf("a: "); for (int i = 0; i < n; ++i) { printf("%d%c", a[i], i + 1 == n ? '\n' : ' '); }
    //printf("b: "); for (int i = 0; i <= n; ++i) { printf("%d%c", a[i], i == n ? '\n' : ' '); }

    ll sum = INFLL;
    for (int i = 0, j = n - 1; i <= j; ) {
        ll s1 = b[i];
        ll s2 = b[j + 1] - b[i];
        ll s3 = b[n] - b[j + 1];
        sum = min(sum, max({s1, s2, s3}));
        if (s1 + a[i] < s3 + a[j]) {
            ++i;
        } else {
            --j;
        }
    }
    res = 1.0 - (double)sum / b[n];
}


int main(int argc, char** argv) {
    int totalCaseNumber = 1;

    init();

    scanf("%d", &totalCaseNumber);
    for (int caseNum = 1; caseNum <= totalCaseNumber; ++caseNum) {
        input();
        solve();
        printf("Case #%d: %.13f\n", caseNum, res);
    }

    return 0;
}
