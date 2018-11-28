#include <cstdio>

typedef long long LL;

LL solve1(LL cnt, LL crk) {
	return cnt == 1 || crk == 1 ? 1 : (cnt >> 1) + solve1(cnt >> 1, (crk - 2 >> 1) + 1);
}

LL solve2(LL cnt, LL crk) {
	return cnt == 1 ? 1 : crk == cnt ? cnt : solve2(cnt >> 1, (crk >> 1) + 1);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        LL n, p, a = 0, b = 0;
		scanf("%I64d%I64d", &n, &p);
		n = 1LL << n;
		for (LL c = n; c; c >>= 1)
			if (a + c <= n && solve1(n, a + c) <= p)
                a += c;
		for (LL c = n; c; c >>= 1)
			if (b + c <= n && solve2(n, b + c) <= p)
                b += c;
		printf("Case #%d: %I64d %I64d\n", cs, a - 1, b - 1);
	}
	return 0;
}
