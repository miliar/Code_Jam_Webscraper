#include <cstdio>

int solve(char *S) {
	
	char c = S[0];
	int ans = (c=='-')?1:0;
	for (int i=0;S[i]!='\0';i++) {
		
	//	printf("debug: %d %c %c\n", i, c, S[i]);
		if (c==S[i]) 
			continue;
		else if (c=='+' && S[i]=='-') 
			ans+=2, c = '-';
		else if (c=='-' && S[i]=='+')
			c = '+';
		else 
			return -404;	//should never happen !!	
	}
	return ans;
}

int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int t, ans;
	char S[110];
	scanf("%d", &t);
	for (int i=0;i<t;i++) {
		
		scanf("%s", S);
		ans = solve(S);
		printf("Case #%d: %d\n", i+1, ans);
	} 
	return 0;
}
