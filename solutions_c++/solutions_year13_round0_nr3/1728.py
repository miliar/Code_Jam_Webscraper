#include <vector>
#include <string>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cassert>

using namespace std;

#define ll long long
#define ld long double
#define pii pair<int, int>
#define vs vector<string>
#define vi vector<int>
#define vvi vector<vi>
#define vl vector<ll>
#define vvl vector<vl>
#define vd vector<double>
#define vvd vector<vd>
#define vp vector<pii>
#define vvp vector<vp>
#define msi map<string, int>
#define mii map<int, int>

#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define twoLL(n) (1LL << (n))
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()

inline ll pow(int a, int b) { ll res = 1; for (int i = 1; i <= b; ++i) res *= a; return res; }
template<typename T> inline vector<T> split(string const & str, string const & delim = "") { string s = str; for (size_t i = 0; i < delim.size(); ++i) replace(s.begin(), s.end(), delim[i], ' '); vector<T> res; istringstream iss(s); T t; while (iss >> t) res.push_back(t); return res; }
template<typename R, typename T> inline R cast(T const & t) { stringstream ss; ss << t; R r; ss >> r; return r; }

#define inf 2100000000
#define eps 1e-9

vi num;

bool isPalin(ll x)
{
	num.clear();
	while (x)
	{
		num.push_back(x % 10);
		x /= 10;
	}
	int n = sz(num);
	for (int i = 0; i < n; ++i)
		if (num[i] != num[n - 1 - i])
			return false;

	return true;
}

int main()
{
	string _task = "C";
	//string _in = _task + "-small.in", _out = _task + "-small.out";
	string _in = _task + "-large.in", _out = _task + "-large.out";
	ifstream fin(_in.c_str());
	ofstream fout(_out.c_str());

	set<ll> s;
	s.insert(0);
	for (ll i = 1; i < 10000000; ++i)
	{
		if (!isPalin(i))
			continue;
		ll x = i * i;
		if (!isPalin(x))
			continue;
		s.insert(x);
	}

	string ts;
	getline(fin, ts);
	int _N = atoi(ts.c_str());

	for (int _n = 1; _n <= _N; ++_n)
	{
		getline(fin, ts);
		vector<ll> t = split<ll>(ts);

		auto it2 = s.upper_bound(t[1]);
		auto it1 = s.upper_bound(t[0] - 1);
		
		ll res = distance(it1, it2);
		fout << "Case #" << _n << ": ";
		fout << res;
		fout << endl;
	}	

	return 0;
}
