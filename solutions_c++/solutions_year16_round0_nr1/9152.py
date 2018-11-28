#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

void updateSeen(long num, bool* seen, int &seencount) {
	long tmp = num;
	while (tmp > 0) {
		int digit = tmp % 10;
		if (!seen[digit]) {
			seen[digit] = true;
			seencount++;
		}
		tmp = tmp / 10;
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int n;
		scanf("%d", &n);
		if (n <= 0) {
			printf("Case #%d: INSOMNIA\n", i);
		} else {
			int count = 0;
			long num = 0;
			bool seen[10];
			memset(seen, 0, sizeof(seen));
			int seencount = 0;
			while (seencount < 10) {
				num += n;
				count++;
				updateSeen(num, seen, seencount);
			}
			printf("Case #%d: %d\n", i, num);
		}
	}
	return 0;
}