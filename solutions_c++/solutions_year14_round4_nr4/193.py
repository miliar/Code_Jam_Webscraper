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

int n, m;
char s[8][11];

void init() {
}

void input() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%s", s[i]);
    }
}

int id[8];
vector<int> v[4];
int res, cnt;

int gao(const vector<int>& v) {
    set<string> st;
    for (auto i : v) {
        string str = s[i];
        for (int j = 0; j <= (int)str.length(); ++j) {
            st.insert(str.substr(0, j));
        }
    }
    return (int)st.size();
}

void dfs(int depth) {
    if (depth == n) {
        int cur = 0;
        for (int i = 0; i < m; ++i) {
            cur += gao(v[i]);
        }
        if (cur > res) {
            res = cur;
            cnt = 1;
        } else if (cur == res) {
            ++cnt;
        }
    } else {
        for (int i = 0; i < m; ++i) {
            id[depth] = i;
            v[i].push_back(depth);
            dfs(depth + 1);
            v[i].pop_back();
        }
    }
}

void solve() {
    res = 0;
    cnt = 0;
    dfs(0);
}


int main(int argc, char** argv) {
    int totalCaseNumber = 1;

    init();

    scanf("%d", &totalCaseNumber);
    for (int caseNum = 1; caseNum <= totalCaseNumber; ++caseNum) {
        input();
        solve();
        printf("Case #%d: %d %d\n", caseNum, res, cnt);
    }

    return 0;
}
