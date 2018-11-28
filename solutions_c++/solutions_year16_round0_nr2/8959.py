#include <bits/stdc++.h>

int main() {
	int t, i, j, ans, k;
	char s[101];
	bool flag;

	scanf("%d", &t);
	for (k = 1; k <= t; k++) {
		scanf("%s", s);
		
		ans = 0;
		i = strlen(s) - 1;

		while (i >= 0) {
			if (s[i] == '-') {
				if (s[0] == '-') {
					flag = false;
					ans++;
					for(j = 0; j < ((i + 1) / 2); j++) {
					    char temp = s[j];
					    s[j] = s[i - j];
						s[i - j] = temp;
					}
					for(j = 0; j <= i; j++) {
					    if (s[j] == '+') {
					    	s[j] = '-';
					    } else {
					    	s[j] = '+';
					    }
					}
				} else {
					ans++;
					j = 0;
					while (s[j] == '+') {
						s[j] = '-';
						j++;
						flag = true;
					}
				}
				if (!flag) {
					i--;
					flag = false;
				}
			} else {
				i--;
			}
			
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}