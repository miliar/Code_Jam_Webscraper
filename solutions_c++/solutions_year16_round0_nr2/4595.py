#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int T;
char str[200];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		scanf("%s", str);
		int len = strlen(str);
		int cnt = 0;
		for (int i = 1; i < len; i++) {
			if (str[i] != str[i - 1]) {
				cnt++;
			}
		}
		if (str[len - 1] == '-') cnt++;
		printf("Case #%d: %d\n", ca, cnt);
	}
}