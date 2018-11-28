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
const int inf = 1e+9;
 
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

int get3t(int r, int c, int n)
{
    vvi a(r, vi(c));
    forn(i, r)
        forn(j, c)
            if (((i + j) & 1) != 0 && n > 0)
            {
                a[i][j] = 1;
                --n;
            }
     
    if (a[r - 1][0] == 0 && n > 0)
        a[r - 1][0] = 1, --n;
    
    if (a[0][c - 1] == 0 && n > 0)
        a[0][c - 1] = 1, --n;
    
    if (a[r - 1][c - 1] == 0 && n > 0)
        a[r - 1][c - 1] = 1, --n;
        
    forn(i, r)
        if (a[i][0] == 0 && n > 0)
            a[i][0] = 1, --n;
    forn(i, r)
        if (a[i][c - 1] == 0 && n > 0)
            a[i][c - 1] = 1, --n;
    forn(i, c)
        if (a[0][i] == 0 && n > 0)
            a[0][i] = 1, --n;
    forn(i, c)
        if (a[r - 1][i] == 0 && n > 0)
            a[r - 1][i] = 1, --n;
            
    forn(i, r)
        forn(j, c)
            if (a[i][j] == 0 && n > 0)
                a[i][j] = 1, --n;
          
    int res = 0;      
    forn(i, r)
        forn(j, c)
            if (a[i][j])
            {
                res += i - 1 >= 0 && a[i - 1][j];
                res += j - 1 >= 0 && a[i][j - 1];
            }
    return res;
}


int get2t(int r, int c, int n)
{
    vvi a(r, vi(c));
    forn(i, r)
        forn(j, c)
            if (((i + j) & 1) == 0 && n > 0)
            {
                a[i][j] = 1;
                --n;
            }
     
    if (a[r - 1][0] == 0 && n > 0)
        a[r - 1][0] = 1, --n;
    
    if (a[0][c - 1] == 0 && n > 0)
        a[0][c - 1] = 1, --n;
    
    if (a[r - 1][c - 1] == 0 && n > 0)
        a[r - 1][c - 1] = 1, --n;
        
    forn(i, r)
        if (a[i][0] == 0 && n > 0)
            a[i][0] = 1, --n;
    forn(i, r)
        if (a[i][c - 1] == 0 && n > 0)
            a[i][c - 1] = 1, --n;
    forn(i, c)
        if (a[0][i] == 0 && n > 0)
            a[0][i] = 1, --n;
    forn(i, c)
        if (a[r - 1][i] == 0 && n > 0)
            a[r - 1][i] = 1, --n;
            
    forn(i, r)
        forn(j, c)
            if (a[i][j] == 0 && n > 0)
                a[i][j] = 1, --n;
          
    int res = 0;      
    forn(i, r)
        forn(j, c)
            if (a[i][j])
            {
                res += i - 1 >= 0 && a[i - 1][j];
                res += j - 1 >= 0 && a[i][j - 1];
            }
    return res;
}

int get2(int r, int c, int n)
{
    return min(get2t(r, c, n), get3t(r, c, n));
}

int get(int r, int c, int n)
{
    int res = 1e9;
    int lim = 1 << (r * c);
    for (int mask = 0; mask < lim; ++mask)
        if (__builtin_popcount(mask) == n)
        {
            int cnt = 0;
            for (int i = 0; i < r * c; ++i)
                if ((mask >> i) & 1)
                {
                    cnt += i - c >= 0 && ((mask >> (i - c)) & 1);
                    cnt += i - 1 >= 0 && (i % c) != 0 && ((mask >> (i - 1)) & 1);
                    
                    // if (r == 2 && c == 3 && mask == 63)
                    // {
                    //     if (i - c >= 0 && ((mask >> (i - c)) & 1))
                    //         cout << 1 << " " << i << endl;
                    //     if (i - 1 >= 0 && ((mask >> (i - 1)) & 1))
                    //         cout << 2 << " " << i << endl;
                    // }
                }
            res = min(res, cnt);
        }
    return res;
}

void solve(int test)
{
    int r, c, n; cin >> r >> c >> n;
    //int v1 = get(r, c, n);
    int v2 = get2(r, c, n);
    cout << "Case #" << test << ": " << v2 << endl;
}
 

int main()
{
    START
    // freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
 
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