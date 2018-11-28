#include<algorithm>
#include<bitset>
#include<cctype>
#include<cmath>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<climits>
#include<functional>
#include<iostream>
#include<istream>
#include<iterator>
#include<iomanip>
#include<list>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>
using namespace std;
#define LL              long long
#define ULL             unsigned long long
#define FOR(i, a, b)    for(int i = a; i < b; i++)
#define REV(i, a, b)    for(int i = a - 1; i >= b; i--)
#define VI              vector<int>
#define PB              push_back
#define ALL(v)          v.begin(), v.end()
#define MII             map<int, int>
#define MSI             map<string, int>
#define PII             pair<int, int>
#define MP              make_pair
#define X               first
#define Y               second
#define SET(a, v)       memset(a, v, sizeof a)
// return the index (match ? first match : immediate greater)
#define lbA(a, n, x)    lower_bound(a, a + n, x) - a
#define lbV(v, x)       lower_bound(ALL(v), x) - v.begin()
// return the index (match ? last match + 1 : immediate greater)
#define ubA(a, n, x)    upper_bound(a, a + n, x) - a
#define ubV(v, x)       upper_bound(ALL(v), x) - v.begin()

template <class T> inline T bigmod(T b, T p, T M) {
    LL ret = 1;
    for (; p > 0; p >>= 1) {
        if (p & 1) ret = (ret * b) % M;
        b = (b * b) % M;
    }
    return (T)ret;
}

const double            PI = acos(-1.0), EPS = 1e-7;
const LL                INF = (LL)1e18 + 7;
const int               N = 2e5 + 5, M = 1e9 + 7;

string s, t;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc;
    cin >> tc;
    FOR(cs, 1, tc + 1) {
        cin >> s;
        t = "";
        FOR(i, 0, s.size()) {
            if (!i) t += s[i];
            else {
                if (s[i] >= t[0]) t = s[i] + t;
                else t += s[i];
            }
        }
        cout << "Case #" << cs << ": " << t << endl;
    }
    return 0;
}
