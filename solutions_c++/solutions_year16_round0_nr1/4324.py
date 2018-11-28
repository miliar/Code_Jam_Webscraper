#include <iostream>
#include <cstdio>
using namespace std;

void runA() {
	freopen("out.out", "w", stdout);
	int t, a, cas = 0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &a);
		if (a == 0) {
			printf("Case #%d: INSOMNIA\n", ++cas);
		}
		else {
			bool d[10] = { 0 };
			int cnt = 0, b = a;
			while (1) {
				int i = b;
				while (i) {
					cnt += !d[i % 10];
					d[i % 10] = 1;
					i /= 10;
				}
				if (cnt == 10)
					break;
				b += a;
			}
			printf("Case #%d: %d\n", ++cas, b);
		}
	}
}

int main()
{
	runA();
}