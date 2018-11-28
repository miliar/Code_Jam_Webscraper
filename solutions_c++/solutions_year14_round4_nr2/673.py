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

int n;
const int MAXN = 1041;

int a[MAXN];
int buf[MAXN];


void read()
{
	cin >> n;
	fin()
		cin >> a[i];
}

bool check(vector<int> &p)
{
	bool up = true;

	for (int i = 0; i < n - 1; ++ i)
	{
		if (a[p[i]] < a[p[i + 1]] && up)
			continue;
		if (a[p[i]] < a[p[i + 1]])
			return false;
		up = false;
	}

	return true;
}
int cntI_(vector<int> &a, int left, int right)
{
	if (left >= right)
		return 0;

	int mid = (left + right) >> 1;

	int ans = cntI_(a, left, mid);
	ans += cntI_(a, mid + 1, right);

	int i = left;
	int j = mid + 1;

	for (int k = left; k <= right; ++ k)
	{
		if (j > right || (i <= mid && a[i] < a[j]))
		{
			buf[k] = a[i];
			++ i;
		}
		else
		{
			buf[k] = a[j];
			ans += mid - i + 1;
			++ j;
		}
	}
	for (int k = left; k <= right; ++ k)
		a[k] = buf[k];

	return ans;
}

int cntI(vector<int> &a)
{
	return cntI_(a, 0, sz(a) - 1);
}
int f(vector<int> p)
{
	int cur = 0;
	for (int i = 0; i < n; ++ i)
	{
		for (int j = 0; j < n - 1; ++ j)
		{
			if (p[j] > p[j + 1])
			{
				swap(p[j], p[j + 1]);
				++ cur;
			}
		}
	}

	return cur;
}

int f2(vector<int> p)
{
	return cntI(p);
}

void solve()
{

	vector<int> p;
	fin()
		p.pb(i);
	int ans = INF;
	do
	{

		if (!check(p))
		{
			continue;
		}

		ans = min(ans, f(p));
	}
	while( next_permutation(all(p)));
	cout << ans;
}

void solve2()
{

	vector<int> p;
	fin()
		p.pb(i);
	int ans = INF;
	do
	{

		if (!check(p))
		{
			continue;
		}

		ans = min(ans, f2(p));
	}
	while( next_permutation(all(p)));
	cout << ans;
}




void solve_smart()
{
	int ans = INF;

	for (int i = 0; i < n; ++ i)
	{
		vector<int> b;
		for (int j = 0; j <= n; ++ j)
			b.pb(a[j]);

		int cur_ans = 0;
		int cur = max_element(all(b)) - b.begin();

		/*while (cur > i)
		{
			swap(b[cur], b[cur - 1]);
			++ cur_ans;
			-- cur;
		}

		while (cur < i)
		{
			swap(b[cur], b[cur + 1]);
			++ cur_ans;
			++ cur;
		}*/
		vector<int> c;
		for (int j = 0; j < i; ++ j)
			c.push_back(b[j]);
		cur_ans += cntI(c);
		c.clear();
		for (int j = n - 1; j >= i; -- j)
			c.push_back(b[j]);
		cur_ans += cntI(c);


		ans = min(ans, cur_ans);
	}

	cout << ans;
}

void solve_bbb()
{
	vector<int> b;
	fin()
		b.pb(a[i]);
	int ans = 0;
	for (int i = 0; i < n; ++ i)
	{
		int id = min_element(all(b)) - b.begin();

		ans += min(id, sz(b) - id - 1);

		b.erase(b.begin() + id);
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
		//cerr << "Case #" << i + 1 << ": " << endl;
		/*if (i + 1 == 50)
		{
			cerr << n << endl;
			fin()
				cerr << a[i] << ' ';
		}*/
		solve_bbb();
		cout << endl;
	}

	return 0;
}
