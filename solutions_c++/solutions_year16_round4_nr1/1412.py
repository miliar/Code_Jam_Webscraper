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
string ar[300];
int p, r, s;

string f(int n, int a, int b, int c, string ans)
{
    if (n == 0 and a == p and b == r and c == s)
        return ans;
    if (n == 0) {
        string tmp;
        return tmp;
    }
    string s2;
    for (char ch: ans) {
        s2.pb(ar[ch][0]);
        s2.pb(ar[ch][1]);
    }
    return f(n-1, a + c, a + b, b + c, s2); 
}

void g(string &str, int i, int len)
{
    if (len == 2) {
        if (str[i+1] < str[i])
            swap(str[i], str[i+1]);
        return;
    }
    //debug(i, len, str.substr(i, len));
    int l = len / 2;
    g(str, i, l);
    g(str, i+l, l);
    bool sw = false;
    for (int j = i; j < i+l; ++j)
        if (str[j] == str[j+l])
            continue;
        else if (str[j] > str[j+l]) {
            sw = true;
            break;
        }
        else
            break;
        
    if (sw)
      for (int j = i; j < i+l; ++j)
        swap(str[j], str[j+l]);  
    //debug(i, len, str.substr(i, len));
}

char t(char a, char b)
{
    if (a == 'P' and b == 'R')
        return 'P';
    if (a == 'S' and b == 'R')
        return 'R';
    if (a == 'R' and b == 'P')
        return 'P';
    if (a == 'R' and b == 'S')
        return 'R';
    if (a == 'P' and b == 'S')
        return 'S';
    if (a == 'S' and b == 'P')
        return 'S';
    debug(a, b);
}

bool z(string ans)
{
    if (ans.length() == 1)
        return true;
    int len = ans.length();
    string ans2;
    for (int i = 0; i < len; i += 2)
        if (ans[i] == ans[i+1])
            return false;
        else
            ans2.pb(t(ans[i], ans[i+1]));
    return z(ans2);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    ar['P'] = "PR";
    ar['R'] = "RS";
    ar['S'] = "PS";

    read(int, t_no);

    for (int t = 1; t <= t_no; ++t) {
        read(int, n);
        cin >> r >> p >> s;
        string ans, tmp;
        tmp = f(n, 1, 0, 0, "P");
        if (tmp.length() > 0) {
            g(tmp, 0, tmp.length());
            if (ans.length() == 0 or tmp < ans)
                ans = tmp;
        }
        tmp = f(n, 0, 1, 0, "R");
        if (tmp.length() > 0) {
            g(tmp, 0, tmp.length());
            if (ans.length() == 0 or tmp < ans)
                ans = tmp;
        }
        tmp = f(n, 0, 0, 1, "S");
        if (tmp.length() > 0) {
            g(tmp, 0, tmp.length());
            if (ans.length() == 0 or tmp < ans)
                ans = tmp;
        }
        cout << "Case #" << t << ": ";
        if (ans.length() == 0)
            ans = "IMPOSSIBLE";
        /*string ans2;
        for (int i = 0; i < p; ++i)
            ans2.pb('P');
        for (int i = 0; i < r; ++i)
            ans2.pb('R');
        for (int i = 0; i < s; ++i)
            ans2.pb('S');
        string ans3;
        do {
            if (z(ans2) and (ans3.length() == 0 or ans2 < ans3))
                ans3 = ans2;
        } while (next_permutation(ans2.begin(), ans2.end()));
        if (ans3.length() == 0)
            ans3 = "IMPOSSIBLE";

        if (ans3 != ans)
            debug(ans, ans3);
        */
        cout << ans << '\n';
    }

    return 0;
}
