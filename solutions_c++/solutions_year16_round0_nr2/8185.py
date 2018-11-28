#include <stdio.h>
#include <string.h>

//문자열이 +인지 확인
bool isHappy(char *str, int len) {
	for (int i = 0; i < len; i++) {
		if (str[i] == '-')
			return false;
	}
	return true;
}
//지정 위치 부터 뒤집기

void solve() {
	char str[102];
	char tmp[102];

	scanf("%s", str);

	int ans = 0;
	int len = strlen(str);
	strcpy(tmp, str);

	while (1) {
		if (isHappy(tmp, len))
			break;

		//끝에서부터 -찾기
		int i;
		int start = 0;
		for (i = len - 1; i >= 0; i--) {
			if (tmp[i] == '-') {
				if (tmp[start] == '-') {
					start++;
					break;
				}					
				int flag = 1;
				for (int j = 0; j < i; j++) {
					if (tmp[j] == '+') {
						flag = 0;
						break;
					}
				}
				if (flag)
					break;
			}
			else if (tmp[i] == '+') {
				if (i < len - 1) {
					if (tmp[i + 1] == '-')
						break;
				}
			}
		}
		// 뒤집기
		for (int j = 0; j <= i / 2; j++) {
			char t = tmp[j];
			tmp[j] = tmp[i - j];
			tmp[i - j] = t;
		}
		//모양 바꾸기
		for (int j = 0; j <= i; j++) {
			if (tmp[j] == '-')
				tmp[j] = '+';
			else
				tmp[j] = '-';
		}
		ans++;
	}
	printf("%d\n", ans);
}
int main(void) {
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}
}