#include <bits/stdc++.h>
using namespace std;

char s[10005];
int n;
int main() {
	int T;
	scanf("%d", &T);
	for(int _=1; _<=T; ++_) {
		printf("Case #%d: ", _);
		scanf("%d", &n);
		scanf("%s", s);
		int ans=0, sum=0;
		for(int i=0; i<=n; ++i) {
			if(sum<i) { ans+=i-sum; sum+=i-sum; }
			sum+=s[i]-'0';
		}
		printf("%d\n", ans);
	}
	return 0;
}