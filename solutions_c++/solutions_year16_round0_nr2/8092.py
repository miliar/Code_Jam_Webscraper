#include <stdio.h>

int main() {
	int c;
	scanf("%d", &c);
	for (int t = 0; t < c; t++) {
		char buf[128];
		scanf("%s", &buf);
		char last = 'x';
		int count = 0;
		for (int i = 0; buf[i] != 0; i++) {
			if (buf[i] != last) {
				count++;
				last = buf[i];
			}
		}
		if (last == '+') {
			count--;
		}

		printf("Case #%d: %d\n", t + 1, count);


	}
}