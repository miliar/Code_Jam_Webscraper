#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

typedef long long int tip;

typedef set<tip> sett;
sett S;

tip reverse(tip &b)
{
	tip a = b;
	tip n = 1;
	b = 0;
	while (a > 0)
	{
		n *= 10;
		b *= 10;
		b += (a % 10);
		a /= 10;
	}
	return n;
}

void precalc()
{
	tip i, r, n, a, b;
	
	for (i = 1; i < 1000; i++)
	{
		r = i;
		n = reverse(r);
		
		a = i*n+r;
		b = (i/10)*n+r;
		
		a *= a;
		r = a;
		reverse(r);
		if (r == a) {
			S.insert(a);
		}
		
		a = b;
		a *= a;
		r = a;
		reverse(r);
		if (r == a) {
			S.insert(a);
		}
	}
}

int main()
{
	int T;

	precalc();
/*	printf("%lu\n", S.size());
	for (sett::iterator it = S.begin(); it != S.end(); it++) {
		printf("%lld\n", *it);
	}
	return 0;*/

	scanf("%d", &T);
	
	for (int i = 0; i < T; i++)
	{
		tip a, b;
		int n = 0;
		scanf("%lld%lld", &a, &b);
		sett::iterator it = S.lower_bound(a);
		while (*it <= b) {
			n++;
			it++;
		}
		printf("Case #%d: %d\n", i+1, n);
	}
}

