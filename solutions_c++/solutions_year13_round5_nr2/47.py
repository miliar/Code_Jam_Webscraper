#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <ctime>
#include <bitset>
using namespace std;

#pragma comment(linker, "/stack:64000000")

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

typedef vector<int> vi;
typedef vector<pair<int, int > > vii;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<ld> vld;

typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef vector<vll> vvll;
typedef vector<vs> vvs;

typedef map<int, int> mpii;
typedef map<int, string> mpis;
typedef map<string, int> mpsi;
typedef map<string, string> mpss;

#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define sz(a) (int)((a).size())
#define len(a) (int)((a).length())

#define forr(i,n) for (int i = 0; i < (n); ++i)
#define fori(n) forr(i,n)
#define forj(n) forr(j,n)
#define fork(n) forr(k,n)
#define forin fori(n)
#define forjn forj(n)
#define forjm forj(m)
#define forkm fork(m)
#define foria(a) fori(sz(a))
#define foriv foria(v)
#define foris fori(len(s))
#define forja(a) forj(sz(a))
#define forjv forj(v)
#define forjs forj(len(s))

#define read cin>>
#define write cout<<
#define writeln write endl

#define readt int aaa; read aaa;
#define gett (bbb+1)
#define fort forr(bbb,aaa)

#define issa(a,s) istringstream a(s);
#define iss(s) issa(ss,s);

ld dis(ld x, ld y) {return sqrt(x*x+y*y);}
const ld PI = acos(ld(0.0))*2;

ll gcd(ll a, ll b){return b ? gcd(b,a%b) : a;}

template<class T>
struct makev
{
    vector<T> v;
    makev& operator << (const T& x)
    {
        v.push_back(x);
        return *this;
    }
    operator vector<T>& ()
    {
        return v;
    }
};

void assert(bool b)
{
    if (!b)
        throw 0;
}

template <int n>
struct nbest
{
    vector<pair<ll, int> > p;
    nbest():p(n+1)
    {
        foria(p) p[i].first = p[i].second = -1;
    }
    void add(ll value, int key)
    {
        p[n] = make_pair(value, key);
        sort(rall(p));
    }
    ll getValue(int pos, int exceptKey = -2)
    {
        if (exceptKey == -1)
            exceptKey = -2;
        if (p[pos].second == exceptKey)
            ++pos;
        return p[pos].first;
    }
    int getKey(int pos, int exceptKey = -2)
    {
        if (exceptKey == -1)
            exceptKey = -2;
        if (p[pos].second == exceptKey)
            ++pos;
        return p[pos].second;
    }
    bool has(int pos, int exceptKey = -2)
    {
        if (exceptKey == -1)
            exceptKey = -2;
        if (p[pos].second == exceptKey)
            ++pos;
        return p[pos].second != -1;
    }
};

inline int vp(ii a, ii b, ii c)
{
	return (b.first - a.first) * (c.second - a.second) - (b.second - a.second) * (c.first - a.first);
}
 
inline bool bounds(int a, int b, int c, int d)
{
	if (a > b)
		swap(a,b);
	if (c > d)
		swap(c,d);
	return max(a,c) <= min(b,d);
}
 
bool intersects(ii a, ii b, ii c, ii d)
{
	if (!bounds(a.first, b.first, c.first, d.first))
		return false;
	if (!bounds(a.second, b.second, c.second, d.second))
		return false;
	if (vp(a,b,c) * vp(a,b,d) > 0)
		return false;
	if (vp(c,d,a) * vp(c,d,b) > 0)
		return false;
	return true;
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	readt;
	fort
	{
		int n;
		read n;
		vii v(n);
		forin read v[i].first >> v[i].second;

		vi order(n);
		forin order[i] = i;

		vi ans;
		ld aval = 0;

		do
		{
			order.push_back(order[0]);
			bool ok = true;
			forin forjn
			{
				if (order[i] == order[j] || order[i+1] == order[j] || order[i] == order[j+1])
					continue;
				if (intersects(v[order[i]], v[order[i+1]], v[order[j]], v[order[j+1]]))
					ok = false;
			}
			if (ok)
			{
				ld test = 0;
				forin test += (v[order[i+1]].second - v[order[i]].second) * (v[order[i+1]].first + v[order[i]].first);
				test = abs(test);
				if (test > aval)
				{
					aval = test;
					ans = order;
				}
			}
			order.pop_back();
		}
		while (next_permutation(all(order)));

		cout.setf(ios::fixed);
		cout.precision(20);
		write "Case #" << gett << ":";
		forin write " " << ans[i];
		writeln;

		//std::cout.setf(ios::fixed);
		//std::cout.precision(20);
		std::cout << "Case #" << gett << ": " << endl;
	}
}