/*
If you put a million monkeys at a million keyboards, one of them will eventually write a C++ program.
The rest of them will write Perl programs.
*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <functional>
using namespace std;
#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()
#define FORS(i,s,n) for(int i=(s);i<(n);++i)
#define FOR(i,n) FORS(i,0,(n))
#define FI(n) FOR(i,(n))
#define MP(x,y) make_pair((x),(y))
#define PB(x) push_back((x))
#define SZ(c) int((c).size())
typedef long long ll; typedef unsigned long long ull; typedef long double ld;
typedef pair<int, int>pii; typedef pair<ll, ll>pll;
typedef vector<int>vi; typedef vector<vi>vvi; typedef vector<bool>vb; typedef vector<ld>vld;
typedef list<pll> lpll; typedef list<ll> lll; typedef vector<ll> vll;
typedef set < int > si;
#ifndef __GNUG__
int __builtin_popcount(unsigned int x) { int result = 0; while (x) { result += x & 1; x >>= 1; }return result; }
int __builtin_popcountll(unsigned long long x) { int result = 0; while (x) { result += x & 1; x >>= 1; }return result; }
#endif
#define popcount __builtin_popcountll
ll gcd(ll, ll, ll&, ll&); ll gcd(ll, ll); ll lcm(ll, ll);
template<class T>const T sqr(const T x);
template<class T> const T binpow(const T a, const ull, const T);

const int MAXN = 42;
char knows[MAXN][MAXN + 1];

bool check(int n, int order[], bool learned[][MAXN], bool used[])
{
	if (*order == -1)
	{
		return true;
	}

	bool answer = true;
	bool was = false;
	FOR(machine, n) 
	{
		if (!used[machine] && learned[order[0]][machine])
		{
			used[machine] = true;
			answer &= check(n, order + 1, learned, used);
			used[machine] = false;
			was = true;
		}
	}

	return answer && was;
}

int solveSmall(int n)
{
	unsigned knows_mask = 0;
	FI(n)
	{
		FOR(j, n)
		{
			knows_mask |= (knows[i][j] == '1') << (i * n + j);
		}
	}

	int answer = n*n;
	for (unsigned mask = 0; mask < (1U << (n*n)); ++mask)
	{
		if ((mask & knows_mask) != knows_mask || popcount(mask ^ knows_mask) > answer)
		{
			continue;
		}

		static bool learned[MAXN][MAXN];

		FOR(worker, n)
		{
			FOR(machine, n)
			{
				learned[worker][machine] = (mask >> (worker * n + machine))&1;
			}
		}

		static int order[MAXN+1];
		FI(n)
		{
			order[i] = i;
		}
		order[n] = -1;

		bool good = true;
		do
		{
			static bool used[MAXN];
			memset(used, false, sizeof(bool) * n);
			good &= check(n, order, learned, used);
		} while (next_permutation(order, order + n));

		if (good)
		{
			answer = min(popcount(mask ^ knows_mask), answer);
		}

	}
	return answer;
}

int main()
{
	//freopen("D-state.in", "r", stdin);
	//freopen("D-state.out", "w", stdout);
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
	//freopen("D-large.in", "r", stdin);
	//freopen("D-large.out", "w", stdout);
	ios::sync_with_stdio(false);
	int t;
	scanf("%d", &t);
	for (int testcase = 1; testcase <= t; ++testcase)
	{
		int n;
		scanf("%d", &n);
		FI(n)
		{
			scanf("%s", knows[i]);
		}
		printf("Case #%d: %d\n", testcase, solveSmall(n));
	}
	return 0;
}


ll gcd(ll a, ll b, ll & x, ll & y)
{
	if (a == 0)
	{
		x = 0; y = 1;
		return b;
	}
	ll x1, y1;
	ll d = gcd(b%a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}

ll gcd(ll a, ll b) { return gcd(a, b, a, b); }
ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }
template<class T>const T sqr(const T x) { return x*x; }
template<class T> const T binpow(const T a, const ull n, const T modulo) { return n == 0 ? 1 : sqr(binpow(a, n / 2, modulo)) % modulo * (n % 2 ? a : 1) % modulo; }
