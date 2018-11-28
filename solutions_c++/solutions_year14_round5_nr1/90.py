#if 1
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

template<class T> string to_str(const T &a) { oss os; os << a; return os.str(); }
template<> string to_str<LD>(const LD& a) { oss os; os.precision(10); os.setf(ios::fixed); os << a; return os.str(); }
template<class T> T from_str(const string &s) { iss is; T val; is >> val; return val; }
string T(int test) { ostringstream os; os << "Case #" << test << ":"; return os.str(); }
int _test_start = -1, _test_end = -1;
bool need_to_run(int test) { return _test_start == -1 || _test_start <= test && test <= _test_end; }

int next(const vector<LL> &ps, int start, LL lim)
{
    int l = start, r = ps.size();
    while (l + 1 < r)
    {
        int mid = (l + r) >> 1;
        if (ps[mid] - ps[start] <= lim)
            l = mid;
        else
            r = mid;
    }
    if (ps[l] - ps[start] <= lim)
        return l;
    return -1;
}
bool can(const vector<LL> &ps, LL lim)
{
    int p1 = next(ps, 0, lim);
    if (p1 == -1)
        return false;
    int p2 = next(ps, p1, lim);
    if (p2 == -1)
        return false;
    return (ps.back() - ps[p2] <= lim);
}

void solve(int test)
{
    // read
    int n, p, q, r, s;
    cin >> n >> p >> q >> r >> s;
    vector<int> a(n);
    for (int i = 0; i < n; ++i)
        a[i] = ((LL(i) * p + q) % r + s);

    if (!need_to_run(test)) return;
    // solve
    vector<LL> ps(n + 1);
    for (int i = 1; i <= n; ++i)
        ps[i] = ps[i - 1] + a[i - 1];

    LL l = -1, ri = ps.back() + 1;
    while (l + 1 < ri)
    {
        LL mid = (l + ri) / 2;

        if (can(ps, mid))
            ri = mid;
        else
            l = mid;
    }
    LL res = ps.back() - ri;
    LD resd = res / LD(ps.back());
    // write
    cout.precision(10);
    cout.setf(ios::fixed);
    cout << T(test) << " " << resd << endl;
}

int main(int argc, char *argv[])
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    //freopen(NAME ".in","r",stdin); freopen(NAME ".out","w",stdout);
    if (argc == 2) { _test_start = _test_end = from_str<int>(argv[1]); }
    if (argc == 3) { _test_start = from_str<int>(argv[1]); _test_end = from_str<int>(argv[2]); }

    clock_t tstart = clock();

    int tests;
    scanf("%d", &tests);
    for(int test = 1; test <= tests; ++test)
    {
        clock_t tprev = clock();
        solve(test);
        //if (need_to_run(test))
        //    dbg("elapsed for #" << test << ": " << (clock() - tprev) / LD(CLOCKS_PER_SEC));
    }

    dbg("elapsed: " << (clock() - tstart) / LD(CLOCKS_PER_SEC));
    return 0;
}
/*************************
*************************/
#endif

