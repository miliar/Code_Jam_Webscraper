#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <stdio.h>

#include <algorithm>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <deque>
#include <stack>

#include <cmath>
#include <string>

#include <cassert>
#include <time.h>
#include <memory.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

#define fi(n) for (int i = 0; i < (n); ++ i)
#define fj(n) for (int j = 0; j < (n); ++ j)
#define fin() for (int i = 0; i < n; ++ i)
#define fjm() for (int j = 0; j < m; ++ j)
#define forv(i, v) for (int i = 0; i < sz((v)); ++ i)


#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int, int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	if (sz(s) > 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

const int MAXN = 141;

int n;
string a[MAXN];
vector<pii> b[MAXN];
void read()
{
	cin >> n;
	fin()
	{
		cin >> a[i];
	}
}

vector<pii> split(string s)
{
	vector<pii> res;
	forv(i, s)
	{
		if (sz(res) == 0 || res.back().first != (int)s[i])
			res.push_back(pii((int)s[i], 0));
		res.back().second++;
	}
	return res;
}

void solve()
{
	int i = 0; 
	int j = 0;

	fin()
	{
		b[i] = split(a[i]);
	}

	for (int i = 1; i < n; ++ i)
	{
		if (sz(b[0]) != sz(b[i]))
		{
			cout << "Fegla Won";
			return;
		}
	}
	lint ans = 0;
	forv(i,b[0])
	{
		lint res = LINF;
		fj(n)
		{
			lint sum = 0;
			if (b[j][i].first != b[0][i].first)
			{
				cout << "Fegla Won";
				return;
			}
			int mid = b[j][i].second;

			for (int k = 0; k < n; ++ k)
			{
				sum += abs(mid - b[k][i].second); 
			}
			res = min(res, sum);
		}

		ans += res;
	}
	cout << ans;
}

int main()
{
	prepare("");

	int T;
	cin >> T;
	fi(T)
	{
		read();
		cout << "Case #" << i + 1 << ": ";
		cerr << "Case #" << i + 1 << ": " << endl;
		solve();
		cout << endl;
	}

	return 0;
}
