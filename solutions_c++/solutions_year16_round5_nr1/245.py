#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)

int tc, n;
char str[123456];
int main() {
	scanf("%d", &tc);
	fo(_,1,tc+1) {
		printf("Case #%d: ", _);
		scanf("%s", str); n = strlen(str);
		stack<char> stk;
		int ans = (n/2)*5;
		fo(i,0,n) {
			if (!stk.empty() && stk.top() == str[i]) {
				ans += 5; stk.pop();
			}
			else stk.push(str[i]);
		}
		printf("%d\n", ans);
	}

	return 0;
}