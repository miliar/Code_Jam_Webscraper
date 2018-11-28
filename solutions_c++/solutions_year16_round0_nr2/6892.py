#include <cstdio>
#include <iostream>

#pragma warning(disable:4996)

using namespace std;

int t;
char a[101];

int sol(char* k) {
	int i = 1, rlt = 0;
	char tmp = k[0];
	while (k[i] != '\0') {
		if (tmp != k[i]) {
			rlt++;
			tmp = k[i];
		}
		i++;
	}
	if (k[i - 1] == '-') {
		rlt++;
	}
	return rlt;
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%s", &a);
		printf("Case #%d: %d\n", i, sol(a));
	}
	return 0;
}
