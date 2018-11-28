#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int T, TT;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; TT++) {
		char str[1010];
		char ans[2010];
		scanf("%s", str);
		int n = strlen(str);
		int st = 1000, en = 1001;
		ans[st] = str[0];
		for (int i = 1; i < n; i++) {
			for (int j = st; j <= en; j++) {
				if (str[i] != ans[j] || j == en) {
					if (str[i] > ans[j]) ans[--st] = str[i];
					else ans[en++] = str[i];
					break;
				}
			}
		}
		printf("Case #%d: ", TT);
		for (int i = st; i < en; i++) printf("%c", ans[i]);
		printf("\n");
	}

	return 0;
}