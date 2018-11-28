#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main() {
	int t;
	scanf("%d ", &t);
	for (int tcase = 1; tcase <= t; tcase++) {
		long long int k, c, s;
		scanf("%lld %lld %lld ", &k, &c, &s);
		long long int dx = 1;
		for (int i = 1; i <= c - 1; i++)
			dx *= k;
		long long int valor = 1;
		printf("Case #%d: ", tcase);
		for (int i = 1; i <= s; i++) {
			printf("%lld ", valor);
			valor += dx;
		}
		putchar('\n');
	}
	return 0;
}
