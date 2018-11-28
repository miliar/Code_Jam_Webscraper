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
 
#define NAME "improvements"

bool check(int tm, const vi &a)
{
    for (int h = 1; h <= tm; ++h)
    {
        int actions = tm - h;
        int need = 0;
        forn(i, a.size())
            need += (a[i] - 1) / h;
        if (need <= actions)
            return true;
    }
    return false;
}

void solve(int test)
{
    int n; cin >> n;
    vi a(n); cin >> a;
    int l = 0, r = *max_element(all(a)) + 1;
    while (r - l > 1)
    {
        int m = (l + r) / 2;
        if (check(m, a))
            r = m;
        else
            l = m;
    }
    cout << "Case #" << test << ": " << r << endl;
}
 
int main()
{
    START
    // freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("B-large.in", "r", stdin); freopen("output.txt", "w", stdout);

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