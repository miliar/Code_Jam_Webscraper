#include <stdio.h>
#include <string.h>

int main() {
	int T; scanf("%d",&T);
	for (int t=1;t<=T;++t){
		char S[105]; scanf("%s",S);
		printf("Case #%d: ",t);
		int len = strlen(S);
		int i = len-1;
		while (i >= 0 && S[i] == '+') --i;
		if (i < 0) puts("0");
		else {
			int diffs = 0;
			while (i > 0) { if (S[i]!=S[i-1]) ++diffs; --i;}
			printf("%d\n", 1+diffs);
		}
	}
	return 0;
}
