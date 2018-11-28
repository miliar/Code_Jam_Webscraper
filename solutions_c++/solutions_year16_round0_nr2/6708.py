#include <stdio.h>
#include <string.h>

int count;
char s[1000];

void work() {
	int i, n = strlen(s);
	count = 1;
	for (i=1; i<n; ++i) 
		if (s[i]!=s[i-1]) ++count;
	if (s[n-1]=='+') --count;
}

int main() {
	int i, t, T;
	scanf("%d",&T);
	for (t=1; t<=T; ++t) {
		scanf("%s",s);
		work();
		printf("Case #%d: %d\n", t, count);
	}
	return 0;
}
