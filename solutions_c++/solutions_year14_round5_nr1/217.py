#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <string>
#define PQ priority_queue
#define OO 2147483647
#define Max(a, b) ((FASTBUFFER = ((a) - (b)) >> 31), ((b) & FASTBUFFER | (a) & ~FASTBUFFER))
#define Min(a, b) ((FASTBUFFER = ((a) - (b)) >> 31), ((a) & FASTBUFFER | (b) & ~FASTBUFFER))
#define Swap(a, b) (a ^= b, b ^= a, a ^= b)

int FASTBUFFER;

using namespace std;

long long get(long long l, long long r);

long long n, p, q, rr, s, ans, l, r, i, now, ss[1000005];
int test, tt;

int main()
{
	freopen("A-large.in", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--)
	{
		cin >> n >> p >> q >> rr >> s;
		for (i = 0; i < n; i++)
			ss[i] = (i * p + q) % rr + s;
		for (i = 1; i < n; i++)
			ss[i] += ss[i - 1];
		r = 0;
		ans = ss[n - 1];
		for (l = 0; l < n; l++)
		{
			if (l == 0)
				now = 0;
			else
				now = ss[l - 1];
			while (r < l)
				r++;
			while (r < n - 1 && ss[r] - now < ss[n - 1] - ss[r])
				ans = min(ans, max(now, get(l, r))), r++;
			ans = min(ans, max(now, get(l, r)));
		}
		
		if (ss[n - 1] == 0)
			ss[n - 1]++;
		printf("Case #%d: %.20f\n", ++tt, 1.0 - (double)ans / (double)ss[n - 1]);
	}
	
	return 0;
}

long long get(long long l, long long r)
{
	long long a, b, c;
	if (l == 0)
		a = 0;
	else
		a = ss[l - 1];
	b = ss[r] - a;
	c = ss[n - 1] - a - b;
	return max(b, c);
}
 
