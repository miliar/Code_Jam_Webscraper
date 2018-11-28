#include <stdio.h>
#include <iostream>
#define two(x) (1LL << (x))
using namespace std;

typedef long long lld;

int n;
lld m;

int T;

lld guarantee(int n, lld r)
{
	lld left = 0, right = 0;
	lld left_inc = 1, right_inc = two(n);
	while (left < r) {
		left_inc <<= 1;
		right_inc >>= 1;
		left += left_inc;
		right += right_inc;
	}
	return right;
}

lld potential(int n, lld r)
{
	lld left = 0, right = 0;
	lld left_inc = two(n), right_inc = 1;
	while (left < r) {
		left_inc >>= 1;
		left += left_inc;
		right += right_inc;
		right_inc <<= 1;
	}
	return right;
}

lld gao1(int n, lld m)
{
	lld l = 0, r = two(n);
	while (l + 1 < r) {
		lld mid = l + r >> 1;
		if (guarantee(n, mid) <= m - 1)
			l = mid; 
		else
			r = mid;
	}
	return l;
}


lld gao2(int n, lld m)
{
	lld l = 0, r = two(n);
	while (l + 1 < r) {
		lld mid = l + r >> 1;
		if (potential(n, mid) <= m - 1)
			l = mid; 
		else
			r = mid;
	}
	return l;
}

void work()
{
	cin >> n >> m;	
	lld res1 = gao1(n, m);
	lld res2 = gao2(n, m);
	static int ttt = 0;
	printf("Case #%d: %lld %lld\n", ++ttt, res1, res2);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	// for (int i = 0; i < 8; ++i) printf("%lld\n", potential(3, i));
	while (T--) work();
}