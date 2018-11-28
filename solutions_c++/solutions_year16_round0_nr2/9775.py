#include <cstdio>
#include <cstring>

int T, len, ans;
char s[200];

int main() {
	scanf("%d", &T);
	for(int ti=1; ti<=T; ti++) {
		scanf("%s", s);
		len = strlen(s);
		s[len] = '+';
		s[len+1] = '\0';
		ans = 0;
		for(int i=0; i<len; i++) {
			if(s[i] != s[i+1]) ans ++;
		}
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}