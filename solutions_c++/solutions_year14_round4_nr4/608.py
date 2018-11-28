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

const int MAXN = 1000;

string a[MAXN];
int n,m;

void read()
{

	cin >> n >> m;

	fin()
		cin >> a[i];

}

bool get_nxt(vector<int> &p)
{
	int cur = n - 1;
	while (cur >= 0 && p[cur] == m - 1)
	{
		p[cur] = 0;
		-- cur;
	}
	if (cur < 0)
		return false;

	p[cur] ++;

	return true;
}

void add(vector< vector<int> > &bor, string &s)
{
	int cur = 0;

	for (int i = 0; i < sz(s); ++ i)
	{
		int d = s[i] - 'A';
		if (bor[cur][d] == -1)
		{
			bor[cur][d] = sz(bor);
			bor.push_back(vector<int>(26, -1));
		}
		cur = bor[cur][d]; 
	}
}
vector< vector<int> > bor;//(1, vector<int>(26, -1));

int f(vector<string> &b)
{
	bor.resize(1);
	bor[0] = vector<int>(26, -1);

	forv(i, b)
		add(bor, b[i]);

	return sz(bor);
}

int cnt[100];

bool check(vector<int> &p)
{
	fjm()
		cnt[j] = 0;

	fin()
		cnt[p[i]] ++;

	if (*min_element(cnt, cnt + m) == 0)
		return false;
	return true;
}

void solve()
{
	vector<int> p;

	fin()
		p.pb(0);

	int cnt_all = 0;
	int cnt_max = 0;
	int ans = 0;


	do 
	{
		if (!check(p))
			continue;
		cnt_all ++;
		//cerr << cnt_all << endl;
		int cur = 0;
		for (int j = 0; j < m; ++ j)
		{
			vector<string> b;

			fin()
			{
				if (p[i] == j)
					b.push_back(a[i]);
			}

			cur += f(b);
		}
		if (ans < cur)
		{
			ans = cur;
			cnt_max = 1;
		}
		else if (ans == cur)
		{
			cnt_max++;
		}

	} while (get_nxt(p));

	cout << ans << ' ' << cnt_max; 
	//if (cnt_max >= INF + 7) throw;
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
