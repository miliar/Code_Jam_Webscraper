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

#include <unordered_map>

unordered_map<string, int> storage;

vi conv(const vector<string> &a)
{
    vi res;
    for (auto &s : a)
    {
        if (!storage.count(s))
            storage.insert(mp(s, int(storage.size())));
        res.push_back(storage[s]);
    }
    return res;
}

vector<string> split(const string &s)
{
    vector<string> ans;
    istringstream is(s);
    string t;
    while (is >> t)
        ans.push_back(t);
    return ans;
}

int bit(int mask, int i)
{
    return (mask >> i) & 1;
}

int solve()
{
    storage.clear();
    string s;

    int n; cin >> n;
    getline(cin, s);
    getline(cin, s);
    vi eng = conv(split(s));
    getline(cin, s);
    vi frn = conv(split(s));

    vvi other(n - 2);
    for (int i = 2; i < n; ++i)
    {
        getline(cin, s);
        other[i - 2] = conv(split(s));
    }

    vi res(storage.size());
    for (auto v : eng)
        res[v] |= 1 << 0;
    for (auto v : frn)
        res[v] |= 1 << 1;

    int cnt = 0;
    for (auto v : res)
        cnt += v == 3;

    stack<pii> hist;

    int ans = inf;

    for (int mask = 0; mask < (1 << other.size()); ++mask)
    {
        int cur = cnt;
        forn(i, other.size())
            for (auto v : other[i])
            {
                hist.push(mp(v, res[v]));

                bool ok1 = res[v] != 3;
                res[v] |= 1 << bit(mask, i);
                bool ok2 = res[v] == 3;

                cur += ok1 && ok2;
            }
        ans = min(ans, cur);

        while (hist.size())
        {
            pii cur = hist.top(); hist.pop();
            res[cur.X] = cur.Y;
        }
    }

    return ans;
}
 
int main()
{
    START
    // freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("C-small-attempt0.in", "r", stdin); freopen("output.txt", "w", stdout);
 
    ios_base::sync_with_stdio(false);
    int t; cin >> t;
    forn(i, t)
    {
        cerr << i + 1 << endl;
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }
 
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