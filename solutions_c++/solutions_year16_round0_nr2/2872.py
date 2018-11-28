#include<iostream>
#include<fstream>
#include<algorithm>
#include<unistd.h>

using namespace std;

char flip(char c) {
	if (c == '+')
		return '-';
	return '+';
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	char pan[1000], c, ct;
	int n, N, t, tm, i, j;
	scanf("%d", &N);
	for (i = 0; i < N; ++i) {
		printf("Case #%d: ", i+1);
		t = n = 0;
		scanf("%s", pan);
		n = strlen(pan);
		if (n <= 0)
			continue;
		while (true) {
			for (j = n-1; j >= 0; --j) {
				if (pan[j] == '-')
					break;
			}
			if (j < 0) {
				printf("%d\n", t);
				break;
			}
			++t;
			if (pan[0] == '+') {
				for (j = 0; j < n; ++j) {
					if (pan[j] == '+')
						pan[j] = '-';
					else
						break;
				}
				continue;
			}
			for (tm = 0; tm <= j/2; ++tm) {
				ct = pan[tm];
				pan[tm] = flip(pan[j-tm]);
				pan[j-tm] = flip(ct);
			}
			// printf("%d\t%s\n", t, pan);
			// sleep(1);
		}
	}
	return 0;
}