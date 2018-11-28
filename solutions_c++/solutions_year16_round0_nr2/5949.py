#include<stdio.h>
int t,j,ans,tmp;
char s[101],a[101];
int main() {
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%s", s);
		ans = 0;
		while (1) {
			a[0]= s[0];
			for (j = 1; s[j]; j++) {
				if (s[j - 1] != s[j])break;
				a[j] = s[j];
			}
			tmp = j;
			for (j = 0; s[j]; j++)
				if (s[j] == '-') {
					j = 200; break;
				}
			if (j != 200) {
				printf("Case #%d: %d\n", i, ans);
				break;
			}
			j = tmp;
			for (int k = 0; k < j; k++) {
				s[k] = a[j - 1 - k] == '+' ? '-' : '+';
			}
			ans++;
		}
	}
	return 0;
}