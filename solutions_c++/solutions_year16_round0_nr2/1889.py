#include <bits/stdc++.h>
using namespace std;
int main() {
	int T;
	char s[500];
	scanf("%d", &T);
	for(int caso=1 ; caso<=T ; caso++) {
		scanf("%s", s);
		int len = strlen(s), pos = 0, ans = 0;
		while( pos < len ) {
			char c = s[pos];
			while( pos < len && s[pos] == c ) pos++;
			ans++;
		}
		if( s[len - 1] == '+' ) ans--;
		printf("Case #%d: %d\n", caso, ans);
	}
	return 0;
}