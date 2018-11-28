/*
ID: aydn.yu1
LANG: C++11
TASK: 
*/

#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cctype>
#include <iomanip>
#include <bitset>
#include <list>
#include <deque>
#include <utility>
#include <functional>
#include <cassert>
#include <complex>
#include <valarray>

using namespace std;

#define all(a)              (a).begin(), (a).end()
#define ms(a, b)            memset(a, b, sizeof(a))
#define mc(a, b)            memcpy(a, b, sizeof(b))
#define mp                  make_pair
#define mt                  make_tuple
#define pb                  push_back
#define eb                  emplace_back
#define fore(it, a)         for (auto it = (a).begin(), it##_ = (a).end(); it != it##_; ++it)
#define f0r(i, a)           for (int i = 0, i##_ = (a); i < i##_; ++i)
#define read(type, args...) type args; rdr,args;
#define fi                  first
#define se                  second
#define bit_no              __builtin_popcount
#define left(a)             (2*(a))
#define right(a)            (2*(a)+1)
#define mid(left, right)    (((left)+(right))/2)
#define PI                  acos(-1)
#define X                   fi
#define Y                   se
#define sq(a)               ((a)*(a))

#ifdef EBUG
    #define debug(args...)      do {cerr << #args << ": "; dbg,args; cerr << endl;} while(0)
#else
    #define debug(args...)
#endif

typedef long long               ll;
typedef long double             ld;
typedef unsigned long long      ull;
typedef vector<int>             vi;
typedef vector<vi>              vvi;
typedef pair<int, int>          ii;
typedef tuple<int, int, int>    iii;
typedef vector<ii>              vii;
typedef vector<iii>             viii;

template<typename T>
using min_pq = priority_queue<T, vector<T>, greater<T>>;

template<typename T>
using max_pq = priority_queue<T>;

const int inf = 2e9+5;
const ll l_inf = 2e18+5;
const int mod_v = 1e9+7;
const int max_n = 1e5+5;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

#define UP      0
#define RIGHT   1
#define DOWN    2
#define LEFT    3

template<typename T>
T gcd(T a, T b)
{
    while (b) {
        T temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

template<typename T>
tuple<T, T, T> egcd(T a, T b)
{
    T x1 = 1, x2 = 0, y1 = 0, y2 = 1;
    while (b) {
        T q = a / b, r = a % b;
        T new_x = x1 - q*x2, new_y = y1 - q*y2;
        x1 = x2, y1 = y2, x2 = new_x, y2 = new_y;
        a = b, b = r;
    }
    return make_tuple(a, x1, y1);
}

inline ll lcm(ll a, ll b)
{
    return a*b/gcd(a, b);
}

template<typename T>
inline T mod(T a, T b = mod_v)
{
    return (a % b + b) % b;
}

template<typename T>
inline T mod_inv(T a, T b = mod_v)
{
    return mod(get<1>(egcd(a, b)), b);
}

template<typename T>
inline T sum(T a, T b, T m = mod_v)
{
    return mod(mod(a, m) + mod(b, m), m);
}

template<typename T>
inline T difference(T a, T b, T m = mod_v)
{
    return mod(mod(a, m) - mod(b, m), m);
}

inline ll product(ll a, ll b, ll m = mod_v)
{
    return mod(mod(a, m) *  mod(b, m), m);
}

inline ll quotient(ll a, ll b, ll m = mod_v)
{
    return mod(mod(a, m) * mod_inv(b, m), m);
}

template<typename T,typename T2>
ostream& operator<< (ostream &s, const pair<T,T2> &p) {return s << p.fi << ' ' << p.se << ' ';}

template<typename T,typename T2>
istream& operator>> (istream &s, pair<T,T2> &p) {return s >> p.fi >> p.se;}

template<typename T>
ostream& operator<< (ostream &s, const vector<T> &v)  {for (auto it: v) s << it << ' '; return s;}

template<typename T>
istream& operator>> (istream &s, vector<T> &v) {fore (it, v) s >> *it; return s;}

template<typename T>
void read_range(T beg, T end)
{
    while (beg != end)
        cin >> *beg++;
}

template<typename T>
void print_range(T beg, T end)
{
    while (beg != end)
        cout << *beg++ << ' ';
}

struct reader
{
    template<typename T>
    reader& operator, (T &v)
    {
        cin >> v;
        return *this;
    }
} rdr;

struct debugger
{
    template<typename T>
    debugger& operator, (const T &v)
    {
        cerr << v << ", ";
        return *this;
    }
} dbg;

/***************************************************************
----------------------------------------------------------------
----------------------------------------------------------------
***************************************************************/

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
#if !defined(NO_FILE) && !defined(ONLINE_JUDGE)
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
#endif

    int t_no;
    cin >> t_no;
    for (int T = 1; T <= t_no; ++T) {
        string s, t;
        cin >> s >> t;
        int n = s.length();
        int ans = inf, i1 = inf, j1 = inf;
        int mx = (n == 1 ? 10 : n == 2 ? 100 : n == 3 ? 1000 : -1);
        assert(mx != -1);
        //debug(n, mx);
        for (int i = 0; i < mx; ++i)
            for (int j = 0; j < mx; ++j) {
                int tmp = i;
                bool ok = true;
                for (int k = n-1; k >= 0; --k) {

                    if (s[k] != '?' and s[k]-'0' != (tmp % 10)) {
                        ok = false;
                    }
                    tmp /= 10;
                }
                tmp = j;
                for (int k = n-1; k >= 0; --k) {
                    if (t[k] != '?' and t[k]-'0' != tmp % 10) {
                        ok = false;
                    }
                    tmp /= 10;
                }
                if (!ok)
                    continue;
                //debug(T, i, j, abs(i-j));
                if (abs(i-j) < ans or (abs(i-j) == ans and i < i1) or (abs(i-j) == ans and i == i1 and j < j1)) {
                    i1 = i;
                    j1 = j;
                    ans = abs(i-j);
                }
            }
        string s1, t1;
        while (i1) {
            s1.pb('0' + i1 % 10);
            i1 /= 10;
        }
        while (s1.size() < n)
            s1.pb('0');
        while (j1) {
            t1.pb('0' + j1 % 10);
            j1 /= 10;
        }
        while (t1.size() < n)
            t1.pb('0');
        reverse(s1.begin(), s1.end());
        reverse(t1.begin(), t1.end());
        cout << "Case #" << T << ": " << s1 << ' ' << t1 << '\n';
    }

    return 0;
}

