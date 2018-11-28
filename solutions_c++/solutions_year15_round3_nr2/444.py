//#define PROB ""        //{{{ Preamble
#define IN   (*PROB ? PROB ".in"  : "input.txt" )
#define OUT  (*PROB ? PROB ".out" : "output.txt")
#ifndef LOCAL_PC
#define NDEBUG
#define LOG(...) static_cast<void>(0)
#else
#include <local>
#endif
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#if __cplusplus >= 201103L || defined(__GXX_EXPERIMENTAL_CXX0X__)
#include <forward_list>
#include <future>
#include <regex>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#endif
using namespace std; typedef long long ll; typedef unsigned long long ull;
const double pi=3.14159265358979323846; const double E=2.7182818284590452354;
const struct __ { ios_base::Init i; int s; __() : s(ios_base::xalloc()) {
    srand(time(NULL)); ios_base::sync_with_stdio(false); cin.tie(NULL); } } _;
#if defined(PROB) && !defined(LOCAL_PC)
const struct $ { filebuf a,b; ~$(){ cin.rdbuf(NULL); cout.rdbuf(NULL); }
    $(){ cin.rdbuf(a.open(IN,ios::in)); cout.rdbuf(b.open(OUT,ios::out)); } }$;
#endif
inline ostream& operator<<(ostream&o,const __&){o.iword(_.s)=0;return o<<'\n';}
#define endl _
template<class T> inline ostream& operator,(ostream&o, const T& x) {
    if (o.iword(_.s)) o << ' '; else o.iword(_.s)=1; return o << x; }
template<> inline ostream& operator,<__>(ostream&o, const __&){return o<<endl;}
template<class I> inline void in(I A, I B) { while (A!=B) { cin >> *A; ++A; } }
template<class I> inline void out(I A, I B, char D=' ') { if (A!=B) {
    cout << *A; while (++A!=B) { cout << D << *A; } } cout << endl; }
template<class T> inline T sq(const T& X) { return X*X; }
template<class T> inline T power(T X, int Y) { assert(Y>=0 && !(X==0 && Y==0));
    T R=(Y&1)?X:1; while (Y >>= 1) { X *= X; if (Y&1) R *= X; } return R; }
#define pb(...)      push_back(__VA_ARGS__)
#define eb(...)      emplace_back(__VA_ARGS__)
#define sz(v)        static_cast<int>((v).size())
#define X            first
#define Y            second
#define FOREACH(i,c) for(__typeof__((c).begin())i=(c).begin();i!=(c).end();++i)
#define mp(x, y)     make_pair((x), (y))
#define mt(...)      make_tuple(__VA_ARGS__)
#define ass(e)       assert(e)
//}}}//////////////////////////////////////////////////////////////////////////

void f(int l, int s, const string& kb, const string& target, string& cur, vector<int>& res)
{
    if (sz(cur) < s)
    {
        for (int i = 0; i < sz(kb); i++)
        {
            cur.push_back(kb[i]);
            f(l, s, kb, target, cur, res);
            cur.pop_back();
        }
    }
    else
    {
        int cnt = 0;
        size_t pos = 0;
        while (true)
        {
            pos = cur.find(target, pos);
            if (pos == string::npos)
            {
                break;
            }
            else
            {
                pos++;
                cnt++;
            }
        }
        res.push_back(cnt);
    }
}

int main()
{
    int T; cin >> T;

    for (int t = 1; t <= T; t++)
    {
        int k, l, s; cin >> k >> l >> s;
        string kb, target; cin >> kb >> target;

        string cur; vector<int> res;
        f(l, s, kb, target, cur, res);

        int m = *max_element(res.begin(), res.end());
        ll sum = 0;
        for (int x : res) {
            sum += m - x;
        }
        cout << "Case #" << t << ": " << fixed << setprecision(7) << (double)sum/sz(res) << endl;
    }
}
