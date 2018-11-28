#if 1
#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <list>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;

const LD eps = 1e-9;
const LD pi = acos(-1.0);
const LL inf = 1e+9;

#define mp make_pair
#define pb push_back
#define X first
#define Y second

#define dbg(x) { cerr << #x << " = " << x << endl; }

// extended template
#pragma comment(linker, "/STACK:36777216")
typedef vector<int> vi;
typedef vector<vi> vvi;

#define forn(i, n) for (int i = 0; i < n; ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

template<typename T> istream & operator >> (istream &, vector<T> &);
template<typename T> ostream & operator << (ostream &, const vector<T> &);

#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;

#define NAME "problem"

LD farm_cost, farm_add, need;

LD get(int farm_cnt)
{
    LD tm = 0;
    LD delta = 2;
    forn(i, farm_cnt)
    {
        tm += farm_cost / delta;
        delta += farm_add;
    }
    tm += need / delta;
    return tm;
}

LD solve()
{
    int l = 0, r = 1e5 + 100;
    while (r - l > 3)
    {
        int m1 = l + (r - l) / 3;
        int m2 = r - (r - l) / 3;
        LD f1 = get(m1);
        LD f2 = get(m2);
        if (f1 < f2)
            r = m2;
        else
            l = m1;
    }
    
    LD res = get(l);
    for (int i = l + 1; i <= r; ++i)
        res = min(res, get(i));

    res = min(res, get(0));

    return res;
}

void solve(int test)
{
    cin >> farm_cost >> farm_add >> need;

    cout << "Case #" << test << ": " << solve() << endl;
}

int main()
{
    START
    // freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
    cout.setf(ios::fixed);
    cout.precision(9);
    ios_base::sync_with_stdio(false);

    int t; cin >> t;
    forn(i, t)
        solve(i + 1);

    END
    return 0;
}
/*******************************************
*******************************************/

template<typename T> istream & operator >> (istream &is, vector<T> &v)
{
    forn(i, v.size())
        is >> v[i];
    return is;
}
template<typename T> ostream & operator << (ostream &os, const vector<T> &v)
{
    forn(i, v.size())
        os << v[i] << " ";
    return os;
}
#endif