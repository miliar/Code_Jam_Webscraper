#include<cstdio>
#include<cstring>

int _, T;
char s[11111];
int k;

int main() {
	scanf("%d", &_);
	for(int T=1; T<=_; T++) {
		scanf("%s%d", s, &k);
		int n = strlen(s), ans=0;
		for(int i=0;i<=n-k;i++)
			if(s[i]=='-') {
				for(int j=0;j<k;j++)
					s[i+j] = '+' + '-' - s[i+j];
				ans++;
			}
		for(int i=n-k;i<n;i++)
			if(s[i]=='-') ans = -1;
		printf("Case #%d: ", T);
		if (ans>=0) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
	
	return 0;
}