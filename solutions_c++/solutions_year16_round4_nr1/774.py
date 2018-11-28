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

inline char compete(char a, char b)
{
	if (a == b)
	{
		return 'D';
	}
	return
		a == 'R' && b == 'S' || a == 'S' && b == 'P' || a == 'P' && b == 'R' ?
		a : b;
}

bool checkLineup(string s)
{
	while (s.length() > 1)
	{
		string result;
		for (int i = 0; i < SZ(s); i += 2)
		{
			result.push_back(compete(s[i], s[i + 1]));
		}
		if (find(ALL(result), 'D') != result.end())
		{
			return false;
		}
		s = result;
	}
	return true;
}

string solveSmall(int n, int r, int p, int s)
{
	string lineup;
	lineup.append(p, 'P');
	lineup.append(r, 'R');
	lineup.append(s, 'S');

	do
	{
		if (checkLineup(lineup))
		{
			return lineup;
		}
	} while (next_permutation(ALL(lineup)));
	return "IMPOSSIBLE";
}

string merge_sort(string result)
{
	if (SZ(result) == 1)
	{
		return result;
	}
	string left = merge_sort(result.substr(0, SZ(result) / 2));
	string right = merge_sort(result.substr(SZ(result) / 2, SZ(result)/2));
	return min(left, right) + max(left, right);
}

string solveLarge(int n, int r, int p, int s)
{
	string answer = "IMPOSSIBLE";
	for (string result : {"P", "R", "S"})
	{
		while (SZ(result) != (1U << n))
		{
			string current;
			FI(SZ(result))
			{
				switch (result[i])
				{
				case 'P':
					current.append("PR");
					break;
				case 'R':
					current.append("RS");
					break;
				case 'S':
					current.append("PS");
					break;
				}
			}
			result = current;
		}

		if (count(ALL(result), 'R') != r || count(ALL(result), 'P') != p || count(ALL(result), 'S') != s)
		{
			continue;
		}

		result = merge_sort(result);
		answer = answer == "IMPOSSIBLE" ? result : min(result, answer);

	}
	return answer;
}

int main()
{
	//freopen("A-state.in", "r", stdin);
	//freopen("A-state.out", "w", stdout);
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	ios::sync_with_stdio(false);
	int t;
	scanf("%d", &t);
	for (int testcase = 1; testcase <= t; ++testcase)
	{
		int n, r, p, s;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		printf("Case #%d: %s\n", testcase, solveLarge(n, r, p, s).c_str());
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
