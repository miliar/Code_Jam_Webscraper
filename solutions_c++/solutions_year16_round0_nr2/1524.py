#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

void solve(int no) {
	char S[101];
	scanf("%s", S);
	printf("Case #%d: ", no);

	int btm = strlen(S) - 1;

	auto exec = [&S](int num) {
		char tmp[100];
		for (int i = 0; i < num; i++) {
			tmp[i] = S[num - 1 - i];
			tmp[i] = (tmp[i] == '+') ? '-' : '+';
		}
		memcpy(S, tmp, num);
	};

	int ans = 0;
	while (1) {
		while (S[btm] == '+') {
			if (btm == 0) {
				goto END;
			}
			btm--;
		}

		if (S[0] == '-') {
			exec(btm + 1);
			ans++;
		}
		else {
			int num = 0;
			while (S[num] == '+') {
				num++;
			}
			exec(num);
			ans++;
		}
	}
END:
	printf("%d\n", ans);
}

int main() {
	int T = 0;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		solve(i);
	}
}
