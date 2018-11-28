#include <iostream>
#include <cstdio>
using namespace std;

bool digits[10];
int cnt, tot;

void update() {
	int x = tot;
	while (x) {
		if (!digits[x % 10]) {
			digits[x % 10] = 1;
			++cnt;
		}
		x /= 10;
	}
}

int main () {
	int _, x;
	cin >> _;
	for (int i = 0; i < _; ++i) {
		printf("Case #%d: ", i + 1);
		scanf("%d", &x);
		if (!x) {
			printf("INSOMNIA\n");
		} else {
			for (int j = 0; j <= 9; ++j) digits[j] = 0;
			cnt = 0;
			tot = x;
			update();
			while (cnt != 10) {
				tot += x;
				update();
			}
			printf("%d\n", tot);
		}
	}
}