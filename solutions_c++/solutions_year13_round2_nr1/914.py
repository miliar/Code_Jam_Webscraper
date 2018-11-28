#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define maxn 105
#define inf 10000

int n;
long long s;
long long f[maxn];

void input()
{
	scanf("%lld", &s);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%lld", &f[i]);
}

int cal(long long &a, long long m)
{
	if (a <= 1)
		return inf;
	int ret = 0;
	while (m >= a)
	{
		ret++;
		a += a - 1;
	}
	a += m;
	return ret;
}

int work()
{
	int ret = n;
	long long a = s;
	int temp = 0;
	for (int i = 0; i < n; i++)
	{
		if (f[i] < a)
			a += f[i];
		else
			temp += cal(a, f[i]);
		ret = min(ret, n - i - 1 + temp);
	}
	return ret;
}

int main()
{
//	freopen("t.txt", "r", stdin);
//	freopen("y.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		input();
		sort(f, f + n);
		printf("%d\n", work());
	}
	return 0;
}
