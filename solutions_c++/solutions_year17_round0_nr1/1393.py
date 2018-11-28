#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int N = 1000;

char s[N];
int a[N];
int n, k;

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%s %d", s, &k);
		n = strlen(s);
		for (int i = 0; i < n; ++i) {
			a[i] = s[i] == '+';
		}
		int ret = 0;
		for (int i = 0; i + k <= n; ++i) {
			if (a[i] == 0) {
				++ret;
				for (int j = 0; j < k; ++j) {
					a[i + j] ^= 1;
				}
			}
		}
		for (int i = 0; i < n; ++i) {
			if (a[i] == 0) {
				ret = -1;
				break;
			}
		}
		printf("Case #%d: ", _);
		if (ret == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ret);
		}
	}
	return 0;
}
