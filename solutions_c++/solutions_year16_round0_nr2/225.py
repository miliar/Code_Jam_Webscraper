#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int t;
char s[123];
int ans;

int main()
{
	scanf("%d\n", &t);
	for(int q=1; q<=t; q++) {
		scanf("%s\n", s);
		ans=0;
		int k=strlen(s)-1;
		while(k>=0 && s[k]=='+') k--;
		while(k>=0) {
			ans++;
			k--;
			while(k>=0 && s[k]==s[k+1]) k--;
		}
		printf("Case #%d: %d\n", q, ans);
	}

	return 0;
}
