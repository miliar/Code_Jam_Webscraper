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
int x;

const int MAXN = 10 * 1000;
int a[MAXN];

void read()
{
	cin >> n >> x;
	fin()
	{
		cin >> a[i];
	}
}

void solve_mall()
{
	vector<int> p;
	fin()
	{
		p.push_back(i);
	}
	int ans = INF;
	do 
	{
		int cur = 0;

		for (int i = n & 1; i < n; i += 2)
		{
			if (a[p[i]] + a[p[i + 1]] > x)
				cur += 2;
			else
				cur += 1;
		}
		ans = min(ans, cur + (n & 1));
	}while (next_permutation(all(p)));

	cout << ans;
}

void solve_big()
{
	sort(a, a + n);

	int i = 0;
	int j = n - 1;
	int ans = 0;
	while (i < j)
	{
		if (a[i] + a[j] <= x)
		{
			ans ++ ;
			++ i;
			--j;
		}
		else
		{
			ans ++;
			j --;
		}
	}

	ans += (i == j);

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
		solve_big();
		cout << endl;
	}

	return 0;
}
