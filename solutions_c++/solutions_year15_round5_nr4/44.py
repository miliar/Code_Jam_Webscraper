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

bool decompose(vector<pair<int, ll> > inp, int x, vector<pair<int, ll> > &result)
{
	result.clear();
	bool rev = false;
	if (x < 0)
	{
		reverse(all(inp));
		x = -x;
		foria(inp) inp[i].first = -inp[i].first;
		rev = true;
	}
	while (sz(inp))
	{
		if (inp.back().second == 0)
		{
			inp.pop_back();
			continue;
		}
		int c = inp.back().first;
		int cn = c - x;
		auto it = lower_bound(all(inp), pair<int, ll>(cn, -1));
		if (it == inp.end())
			return false;
		if (it->first != cn)
			return false;
		if (it->second - inp.back().second < 0)
			return false;
		result.push_back(pair<int, ll>(cn, inp.back().second));
		it->second -= inp.back().second;
		inp.back().second = 0;
	}
	sort(all(result));
	if (rev)
	{
		reverse(all(result));
		foria(result) result[i].first = -result[i].first;
	}
	return true;
}

vi ans;

bool brutforce(const vector<pair<int, ll> > &inp, int xmin, int d)
{
	if (d == 0)
		return true;
	vector<pair<int, ll> > tmp;
	foria(inp)
	{
		if (inp[i].first < xmin || inp[i].first == 0)
			continue;
		ans.push_back(inp[i].first);
		if (decompose(inp, inp[i].first, tmp))
			if (brutforce(tmp, inp[i].first, d - 1))
				return true;
		ans.pop_back();
	}
	return false;
}

vector<pair<int, ll> > gen(int left)
{
	if (left == 0)
	{
		vector<pair<int, ll> > result;
		result.push_back(make_pair(0, 1));
		return result;
	}
	vector<pair<int, ll> > result = gen(left - 1);
	int x = rand() % 11 - 5;
	vector<pair<int, ll> > r2(result);
	foria(r2) r2[i].first += x;
	result.insert(result.end(), all(r2));
	sort(all(result));
	foria(result) if (i && result[i].first == result[i-1].first)
	{
		result[i-1].second += result[i].second;
		result.erase(result.begin() + i);
		--i;
	}
	return result;
}

int main()
{
	ios::sync_with_stdio(false);
#ifdef _MSC_VER
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#else
//	ifstream cin("input.txt");
//	ofstream cout("output.txt");
#endif
	readt;
	fort
	{
		ans.clear();

		vector<pair<int, ll> > sample;
		int n;
		read n;
		sample.resize(n);
		forin read sample[i].first;
		forin read sample[i].second;

		/*sample = gen(55);
		n = sz(sample);*/

		int cnt0 = 0;
		while (sample.back().second != 1)
		{
			forin if (sample.back().second % 2 != 0) throw 0;
			forin sample[i].second /= 2;
			++cnt0;
		}

		ll sum = 0;
		forin sum += sample[i].second;
		int d = 0;
		while (sum > 0)
			++d, sum /= 2;

		if (!brutforce(sample, sample[0].first, d - 1))
			throw 0;

		fori(cnt0) ans.push_back(0);
		sort(all(ans));

		cout << "Case #" << gett << ":";
		foria(ans) cout << ' ' << ans[i];
		cout << endl;
		std::cout << "Case #" << gett << ": " << endl;
	}

	return 0;
}