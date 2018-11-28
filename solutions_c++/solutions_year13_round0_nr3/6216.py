#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <math.h>
using namespace std;


bool isR(int x)
{
	int cnt = 0;
	int a[10];
	while (x)
	{
		a[cnt++] = x % 10;
		x /= 10;
	}

	for (int i = 0;i  < cnt / 2; ++i)
		if (a[i] != a[cnt - i - 1])
			return false;
	return true;
}

bool check(int x)
{
	if (!isR(x))
		return false;
	
	int tmp = sqrt((double)x);
	if (tmp * tmp != x)
		return false;

	if (!isR(tmp))
		return false;

	return true;
}

int main()
{
	int test;
	int a, b;
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &test);
	for (int t = 1; t <= test; ++t)
	{
		int ans = 0;
		scanf("%d%d", &a, &b);
		for (int i = a; i <= b; ++i)
			if (check(i))
				++ans;
		
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}