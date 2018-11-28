#include <stdio.h>

typedef long long LL;

LL gcd (LL a, LL b)
{
	return b ? gcd(b, a%b) : a;
}
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	int ca = 0;
	LL p,q;
	scanf("%d", &t);
	while (ca++ < t) {
		scanf("%lld/%lld", &p, &q);
		int g = gcd(p, q);
		p /= g;
		q /= g;
		if ((q&(q-1)) != 0) {
			printf("Case #%d: impossible\n", ca);
			continue;
		}
		int i = 0;
		int count = 0;
		for (i = 0; i < 41 ; i++) {
			if (p >= q) {
				break;
			}
			p *= 2;
			count++;
		}
		if (count < 40) printf("Case #%d: %d\n", ca, count);
		else printf("Case #%d: impossible\n", ca);
	}
}