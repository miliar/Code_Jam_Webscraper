#include <stdio.h>

int n;
char s[1024];

int main() {
	int t, test = 1;
	scanf("%d", &t);
	while(t--) {
		scanf("%d %s", &n, s);
		
		int count = s[0]-'0', ans = 0;
		for(int i=1; i<n+1; i++) {
			if(--count < 0) {
				ans++;
				count++;
			}
			count += (s[i]-'0');
		}
		printf("Case #%d: %d\n", test++, ans);
	}
}
