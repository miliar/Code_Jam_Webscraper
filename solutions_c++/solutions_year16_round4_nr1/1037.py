#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <utility>
#include <stack>
#include <set>
#include <algorithm>
#include <bitset>
#include <functional>
#include <ctime>
#include <cassert>
#include <valarray>
#include <unordered_map>
#include <unordered_set>
#pragma comment(linker, "/STACK:167772160")

using namespace std;
#pragma region TypeDefs

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef vector< vector<int> > vvint;

#pragma endregion

const int INF = 1e9 + 10;
const ll LINF = ll(2e18) + 10;
const ld PI = acosl(-1);
const double eps = 1e-8;
const ld EPS = 1e-12;

bool good(int r, int p, int s)
{
	return 0 <= r && r < 2 &&
		0 <= p && p < 2 &&
		0 <= s && s < 2;
}

void print(int r, int p, int s, int n)
{
	if (r == 0)
	{
		printf("PS");
		return;
	}
	if (p == 0)
	{
		printf("RS");
		return;
	}
	if (s == 0)
	{
		printf("PR");
		return;
	}
	int nn = (n / 2);
	if (nn % 3 == 1)
	{
		if (good(r - nn / 3 * 2, p - nn / 3 * 2 - 1, s - nn / 3 * 2))
		{
			print(nn / 3, nn / 3 + 1, nn / 3, nn);
			print(r - nn / 3, p - nn / 3 - 1, s - nn / 3, nn);
		}
		else if (good(r - nn / 3 * 2 - 1, p - nn / 3 * 2, s - nn / 3 * 2))
		{
			print(nn / 3 + 1, nn / 3, nn / 3, nn);
			print(r - nn / 3 - 1, p - nn / 3, s - nn / 3, nn);
		}
		else
		{
			print(nn / 3, nn / 3, nn / 3 + 1, nn);
			print(r - nn / 3, p - nn / 3, s - nn / 3 - 1, nn);
		}
	}
	else
	{
		if (good(r - nn / 3 * 2 - 1, p - nn / 3 * 2 - 1, s - nn / 3 * 2))
		{
			print(nn / 3 + 1, nn / 3 + 1, nn / 3, nn);
			print(r - nn / 3 - 1, p - nn / 3 - 1, s - nn / 3, nn);
		}
		else if (good(r - nn / 3 * 2, p - nn / 3 * 2 - 1, s - nn / 3 * 2 - 1))
		{
			print(nn / 3, nn / 3 + 1, nn / 3 + 1, nn);
			print(r - nn / 3, p - nn / 3 - 1, s - nn / 3 - 1, nn);
		}
		else
		{
			print(nn / 3 + 1, nn / 3, nn / 3 + 1, nn);
			print(r - nn / 3 - 1, p - nn / 3, s - nn / 3 - 1, nn);
		}
	}
}

void solve()
{
	int n, r, p, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	n = 1 << n;
	int t = n / 3;
	if (!good(p - t, r - t, s - t))
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	print(r, p, s, n);
	printf("\n");
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen("chocolate.in", "r", stdin);
	//freopen("chocolate.out", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}

#ifdef LOCAL
	fprintf(stderr, "\n\nTime: %.3f", double(clock()) / CLOCKS_PER_SEC);
#endif
	return 0;
}