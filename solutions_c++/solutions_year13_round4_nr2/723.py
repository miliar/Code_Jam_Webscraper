/*========================================================================
#   FileName: B.cpp
#     Author: YIMMON
#      Email: yimmon.zhuang@gmail.com
#   HomePage: http://qr.ae/8DMzu
# LastChange: 2013-06-01 22:43:10
========================================================================*/
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int T, n, p;
int ans1, ans2;

inline int log2(int x)
{
	int ret = 0;
	while(x > 1)
	{
		ret++;
		x >>= 1;
	}
	return ret;
}

inline int get_best(int x)
{
	if(x == 0) return 0;
	int a = log2((1<<n)-x);
	a = n-a;
	return (1<<a)-1;
}

inline int get_worse(int x)
{
	if(x == 0) return 0;
	int a = log2(x+1);
	a = n-a;
	int ret = (1<<n)-1;
	ret >>= a;
	return ret << a;
}

int main(int argc, char **argv)
{
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas)
	{
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &p);
		ans1 = ans2 = -1;
		for(int i = (1<<n)-1; i >= 0 && (ans1 < 0 || ans2 < 0); --i)
		{
			int best = get_best(i), worse = get_worse(i);
			if(worse < p && ans1 < 0)
				ans1 = i;
			if(best < p && ans2 < 0)
				ans2 = i;
		}
		printf("%d %d\n", ans1, ans2);
	}

	return 0;
}
