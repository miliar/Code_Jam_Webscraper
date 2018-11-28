#include <cstdio>

int main() {
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; i++) {
		char s[100];
		gets(s);
		int sum = 0;
		bool plus = 0;
		for (int j = 0; s[j]; j++) {
			if (s[j] == '-' && (!s[j+1] || s[j+1] == '+')) {
				sum++;
				sum += plus;
			}
			plus |= s[j] == '+';
		}
		printf("Case #%d: %d\n", i+1, sum);
	}
}
