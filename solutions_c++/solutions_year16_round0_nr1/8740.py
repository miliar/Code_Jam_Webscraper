#include<cstdio>
#include<iostream>

using namespace std;

int main() {
	int t;
	bool digits[10];
	scanf("%d", &t);
	for (int time = 1; time <= t; time++) {
		int n;
		fill(digits, digits + 10, false);
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", time);
			continue;
		}
		int n2 = n;
		while (true) {
a:
			int tmp = n2;
			while (tmp != 0) {
				digits[tmp % 10] = true;
				tmp /= 10;
			}
			for (int i=0; i < 10; i++) {
				if (digits[i] == false){n2 += n;goto a;}
			}
			break;
		}
		printf("Case #%d: %d\n",time, n2);
	}
}
