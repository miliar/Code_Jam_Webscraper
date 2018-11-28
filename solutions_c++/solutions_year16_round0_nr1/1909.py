#include <cstdio>
#include <iostream>

using namespace std;

int mark = 0;

void check(int a) {
	while (a > 0) {
		int l = a % 10;
		a /= 10;
		mark |= (1 << l);
	}
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; i++) {
		mark = 0;
		int a; scanf("%d", &a);
		int j;
		for (j = 1; j <= 1000 && mark < 1023; j++) {
			check(a*j);
			if (mark >= 1023) break;
		}
		if (mark < 1023) {
			printf("Case #%d: INSOMNIA\n", i);
		} else {
			printf("Case #%d: %d\n", i, a*j);
		}
	}
}