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

void solve(int test)
{
    int r1, r2;
    cin >> r1; --r1;
    vvi a(4, vi(4)); cin >> a;
    cin >> r2; --r2;
    vvi b(4, vi(4)); cin >> b;

    vi pa(17), pb(17);
    forn(i, 4)
        forn(j, 4)
            pa[a[i][j]] = pb[b[i][j]] = i;

    map<pii, vi> m;
    for (int i = 1; i <= 16; ++i)
        m[mp(pa[i], pb[i])].push_back(i);

    const vi &ans = m[mp(r1, r2)];
    cout << "Case #" << test << ": ";
    if (ans.size() == 0)
        cout << "Volunteer cheated!" << endl;
    else if (ans.size() == 1)
        cout << ans.front() << endl;
    else
        cout << "Bad magician!" << endl;
}

int main()
{
    START
    // freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
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