#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int N = 1e2+10;

int n;
char s[N];

int main() {

	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; ++i) {
		printf("Case #%d: ", i);
		scanf(" %s", s+1);
		n = strlen(s+1);
		int m = 0;
		for (int j = 1; j <= n; ++j) {
			int k = j;
			for (; k < n && s[k+1] == s[j]; ++k);
			++m, j = k;
		}
		if (s[n] == '+') --m;
		printf("%d\n", m);
	}

	return 0;
}
