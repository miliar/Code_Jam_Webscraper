#include <bits/stdc++.h>
using namespace std;
int main() {
	int T, n;
	char s[2000];
	scanf("%d", &T);
	for(int caso=1 ; caso<=T ; caso++) {
		scanf("%d %s", &n, s);
		int sum = 0, ans = 0;
		for(int i=0 ; i<=n ; i++) {
			if( i <= sum ) sum += (s[i] - '0');
			else {
				int inc = i - sum;
				ans += inc;
				sum += (inc + s[i] - '0');
			}
		}
		printf("Case #%d: %d\n", caso, ans);
	}
	return 0;
}