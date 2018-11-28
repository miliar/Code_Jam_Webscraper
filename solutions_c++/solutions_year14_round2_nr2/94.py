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

lint a, b, k;

void read()
{
	cin >> a >> b >> k;
	--a;
	--b;
	--k;
}

const int MAXN = 100;

lint dp[MAXN][2][2][2];

bool bit(lint msk, int id)
{
	return (msk & (1LL << id));
}

void Upd(lint &res, lint val)
{
	res += val;
}

void solve()
{
	
	_(dp, 0);
	dp[60][1][1][1] = 1;

	for (int i = 60; i > 0; -- i)
	{
		for (int c1 = 0; c1 < 2; ++ c1)
		{
			for (int c2 = 0; c2 < 2; ++ c2)
			{
				for (int c3 = 0; c3 < 2; ++ c3)
				{
					// 0 0 
					Upd(dp[i - 1][c1 & (bit(a, i - 1) == 0)][c2 & (bit(b, i - 1) == 0)][c3 & (bit(k, i -1) == 0)], dp[i][c1][c2][c3]);

					// 1 0 
					if (c1 == 0 || bit(a, i - 1) == 1)
						Upd(dp[i - 1][c1][c2 & (bit(b, i - 1) == 0)][c3 & (bit(k, i - 1) == 0)], dp[i][c1][c2][c3]);
					//0 1
					if (c2 == 0 || bit(b, i - 1) == 1)
						Upd(dp[i - 1][c1 & (bit(a, i - 1) == 0)][c2][c3 & (bit(k, i - 1) == 0)], dp[i][c1][c2][c3]);
					//1 1 
					if (((c1 == 0) || (bit(a, i - 1) == 1)) && (c2 == 0 || bit(b, i - 1) == 1) && (c3 == 0 || bit(k, i - 1) == 1))
						Upd(dp[i - 1][c1][c2][c3], dp[i][c1][c2][c3]);
				}
			}
		}
	}

	lint ans = 0;

	for (int i = 0; i < 2; ++ i)
		for (int j = 0; j < 2; ++ j)
			for (int k = 0; k < 2; ++ k)
				ans += dp[0][i][j][k];

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
