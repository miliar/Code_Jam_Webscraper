#include <iostream>
#include <cstdio>
using namespace std;

int n;
char s[1005];

int main() {
	int T, cases = 0;
	scanf("%d", &T);	
	while (T--) {
		scanf("%d", &n);
		scanf("%s", s);
		int ans = 0;
		int total = 0;
		for (int i = 0; i <= n; ++i) {
			int cur = s[i] - '0';	
			if (total < i) {
				ans += i - total;
				total = i; 
			}
			total += cur;
		}
		printf("Case #%d: %d\n", ++cases, ans);
	}
	return 0;
}
