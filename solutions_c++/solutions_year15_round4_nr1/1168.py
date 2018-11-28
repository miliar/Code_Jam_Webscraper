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
#pragma comment(linker, "/STACK:99999999999")
typedef vector<int> vi;
typedef vector<vi> vvi;
 
#define forn(i, n) for (int i = 0; i < n; ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
 
template<typename T> istream & operator >> (istream &, vector<T> &);
template<typename T> ostream & operator << (ostream &, const vector<T> &);
 
#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;
 
#define NAME "input"

string i2s(int x)
{
    ostringstream os;
    os << x;
    return os.str();
}

string solve()
{
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    cin >> a;

    vi cn(n), cm(m);
    forn(i, n)
        forn(j, m)
        {
            cn[i] += int(a[i][j] != '.');
            cm[j] += int(a[i][j] != '.');
        }

    forn(i, n)
        forn(j, m)
            if (a[i][j] != '.' && cn[i] == 1 && cm[j] == 1)
                return "IMPOSSIBLE";

    int cnt = 0;
    forn(i, n)
        forn(j, m)
            if (a[i][j] != '.')
            {
                bool change = true;
                if (a[i][j] == '<')
                {
                    for (int k = 0; k < j; ++k)
                        if (a[i][k] != '.')
                            change = false;
                }
                else if (a[i][j] == '>')
                {
                    for (int k = j + 1; k < m; ++k)
                        if (a[i][k] != '.')
                            change = false;
                }
                else if (a[i][j] == 'v')
                {
                    for (int k = i + 1; k < n; ++k)
                        if (a[k][j] != '.')
                            change = false;
                }
                else if (a[i][j] == '^')
                {
                    for (int k = 0; k < i; ++k)
                        if (a[k][j] != '.')
                            change = false;
                }
                cnt += int(change);
            }

    return i2s(cnt);
}

 
int main()
{
    START
    // freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("A-large.in", "r", stdin); freopen("output.txt", "w", stdout);
 
    int t; cin >> t;
    forn(i, t)
        cout << "Case #" << i + 1 << ": " << solve() << endl;
 
    // END
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