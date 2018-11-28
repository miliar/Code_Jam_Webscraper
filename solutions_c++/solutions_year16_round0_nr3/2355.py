#include<iostream>
#include<fstream>
#include<algorithm>
#include<unistd.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

int test(unsigned int n, int base) {
	long long int add = 0, basex = 1;
	while (n) {
		add += basex * (n & 1);
		basex *= base;
		n = n >> 1;
	}
	int upb = 10000;
	if (upb * upb > add)
		upb = sqrt((int)add);
	for (int i = 2; i < upb; ++i)
		if (add % i == 0)
			return i;
	return 0;
}

void print_bin(unsigned int n) {
	int x = 0;
	char buff[32];
	while (n) {
		buff[x] = (n & 1) + '0';
		n = n >> 1;
		++x;
	}
	for (int i = x-1; i >= 0; --i)
		putchar(buff[i]);
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	unsigned int nn[9], x;
	unsigned int n, N, t, tm, i, j;
	scanf("%d", &N);
	for (i = 0; i < N; ++i) {
		printf("Case #%d:\n", i+1);
		scanf("%d %d", &n, &j);
		t = (1 << (n-1)) + 1;
		while (j > 0) {
			t += 2;
			for (tm = 2; tm <= 10; ++tm) {
				x = test(t, tm);
				if (x) {
					nn[tm-2] = x;
				} else {
					break;
				}
			}
			if (tm > 10) {
				--j;
				print_bin(t);
				for (tm = 2; tm <= 10; ++tm)
					printf(" %d", nn[tm-2]);
				printf("\n");
			}
		}
	}
	return 0;
}