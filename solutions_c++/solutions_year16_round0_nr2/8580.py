#include<bits/stdc++.h>
using namespace std;

char s[105];
int t, ans;

int main(int argc, char **argv) {
	scanf("%d", &t);
	for(int T = 1, n; T<=t ; ++T) {
		printf("Case #%d: ", T);
		scanf("%s", s);
		n = strlen(s);
		ans = 0;
		for(int i=1 ; i<n ; ++i)
			if(s[i] != s[i-1])
				++ans;
		if(s[n-1] == '-') ++ans;
		printf("%d\n", ans);

	}
	return 0;
}
