#include <bits/stdc++.h>
using namespace std;

char str[1111];

int main(void) {


	int cases; scanf("%d", &cases);
	int cas = 0;
	while (cases--) {
	
		printf("Case #%d: ", ++cas);
	
		int S = 0;
		
		scanf("%d %s", &S, str);
		
		int ans = 0;
		int have = 0;
		
		for (int i = 0; i <= S; ++i) {
		
			if (str[i] == '0') continue;
		
			if (have >= i) {
				have += str[i] - '0';
			} else {
				ans += i-have;
				have = i+str[i]-'0';
			}
		}
		printf("%d\n", ans);	
	}

	return 0;
}
