#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#define Mset(x, y) memset(x, y, sizeof(x))
#define MAX 110
typedef long long LL;
using namespace std;

LL p[100], tmp[20];

LL inv(LL x)
{
	LL ret = 0;
	int len = 0;
	for (; x > 0; x /= 10)
		tmp[++len] = x % 10;
	for (int i = len; i >= 1; --i)
		ret += tmp[i] * p[len - i + 1];
	return ret;
}

bool check(LL x)
{
	int len = 0;
	for (; x > 0; x /= 10)
		tmp[++len] = x % 10;
	for (int i = 1; i <= (len >> 1); ++i)
		if (tmp[i] != tmp[len - i + 1])
			return false;
	return true;
}

int Get(int lim)
{
	LL ret = 0;
	if (lim >= 1) ++ret;
	if (lim >= 4) ++ret;
	if (lim >= 9) ++ret;
	for (int i = 1; i <= 3; ++i)
	{
		for (LL j = p[i]; j <= (p[i + 1] - 1); ++j)
			if (j % 10 != 0)
			{
				LL G = j + inv(j) * p[i + 1];
				if (G * G <= lim && check(G * G)) ++ret;
				for (LL k = 0; k <= 9; ++k)
				{
					G = j + inv(j) * p[i + 2] + k * p[i + 1];
					if (G * G <= lim && check(G * G)) ++ret;
				}
			}
	}
	return ret;
}

int main()
{
	int TestCase;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &TestCase);
	p[1] = 1LL;
	for (int i = 2; i <= 10; ++i)
		p[i] = p[i - 1] * 10LL;
	for (int T = 1; T <= TestCase; ++T)
	{
		LL ans = 0LL, L, R;
		cin >> L >> R;
		cout << "Case #" << T << ": " << Get(R) - Get(L - 1) << endl;
	}
	return 0;
}

