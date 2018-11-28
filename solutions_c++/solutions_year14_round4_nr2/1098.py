#pragma comment(linker, "/STACK:255000000")
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <stack>
#include <memory.h>
#include <algorithm>
#include <math.h>
#include <valarray>
#include <complex>
#include <bitset>
#include <ctime>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef complex<double> comp;
typedef pair<int, int> pint;

long double eps = 1e-7;
const int BASE = (int) 1e9;
const long double PI = 3.1415926535897932384626433832795;
const int MOD = (int) 1e9 + 7;
const int HMOD = (1 << 18) - 1;
const int INF = 1 << 30;
const LL LLINF = 1ll << 60;
const int N = 310000;

int t, n;
int b[11000], a[11000];

bool Check()
{
	for (int i = 0; i < n; i++)
	{
		bool res = true;
		for (int j = 1; j <= i; j++)
			res &= b[j] > b[j - 1];
		for (int j = i + 1; j < n; j++)
			res &= b[j] < b[j - 1];
		if (res)
			return true;
	}
	return false;
}

int Count()
{
	int answ = 0;
	int c[110000];
	memcpy(c, b, sizeof(b));
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			if (a[i] == c[j])
			{
				answ += abs(i - j);
				int tmp = c[j];
				for (int k = j; k > i; k--)
					c[k] = c[k - 1];
				c[i] = tmp;
			}
	}
	return answ;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int k = 0; k < t; k++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		int Min = 1 << 30;
		sort(b, b + n);
		do
		{
			if (Check())
				Min = min(Min, Count());
		} while (next_permutation(b, b + n));
		printf("Case #%d: %d\n", k + 1, Min);
	}
	return 0;
}