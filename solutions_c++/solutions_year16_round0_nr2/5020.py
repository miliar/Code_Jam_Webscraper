#include<stdio.h>
#include<string.h>
char str[200];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc; scanf("%d\n", &tc);
	for (int test = 1; test <= tc; test++) {
		scanf("%s\n", str);
		int len = strlen(str);
		str[len] = '+';
		int cnt = 0;
		bool p = (str[0] == '+' ? true : false);
		for (int i = 0; i < len; i++) {
			if ((p?'+':'-') != str[i + 1]) {
				p = !p;
				cnt++;
			}
		}

		printf("Case #%d: %d\n", test, cnt);
	}
	fclose(stdin);
	fclose(stdout);
}