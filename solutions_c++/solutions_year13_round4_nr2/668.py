#pragma comment(linker, "/STACK:10000000")
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE

#include <cassert>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <numeric>
#include <bitset>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <functional>
#include <cstring>
#include <ctime>

#define y1 AAA_BBB
#define y0 AAA_AAA

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(v) (int)((v).size())
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
template <class T> T inline sqr(T x) {
    return x * x;
}
const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;

typedef pair<i64, i64> pll;

const int maxn = 10500;

i64 solve1(i64 n, i64 p)
{
	i64 pos[maxn], q[maxn];
	i64 addPos = (1LL << (n - 1)), addQ = 2;
	int m = 1;
	pos[0] = 1, q[0] = 1;
	for (i64 i = 1 + addPos; addPos > 0; i+= addPos)
	{
		pos[m] = i;
		q[m] = addQ;
		m++;
		addQ *= 2;
		addPos /= 2;
	}
	q[m - 1] = 1;
	i64 ans = 0;
	for (int i = 0; i < m; i++)
		if (pos[i] <= p)
			ans += q[i];
	return ans - 1;
}

i64 solve2(i64 n, i64 p)
{
	i64 pos[maxn], q[maxn];
	i64 addPos = (1LL << (n - 1)), addQ = 2;
	int m = 1;
	pos[0] = (1LL << n), q[0] = 1;
	for (i64 i = (1LL << n) / 2; addPos > 0; i -= addPos)
	{
		pos[m] = i;
		q[m] = addQ;
		m++;
		addQ *= 2;
		addPos /= 2;
	}
	q[m - 1] = 1;
	i64 ans = 0;
	for (int i = m - 1; i >= 0; i--)
		if (pos[i] <= p)
			ans += q[i];
	return ans - 1;
}


pll solve()
{
	i64 n, p;
	cin >> n >> p;
	return mp(solve1(n, p), solve2(n, p));
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w", stdout);
	int t;
	cin >> t;
	forn (i, t){
		pair<i64, i64> ans = solve();
		cout << "Case #" << i + 1 << ": " << ans.first << " " << ans.second << endl;
	}
	return 0;
}
