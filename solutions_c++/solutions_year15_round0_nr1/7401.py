#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int cases = 1; cases <= t; cases++) {
		int k;
		scanf("%d",&k);
		int cnt = 0;
		int ans = 0;
		for(int i = 0; i <= k; i++) {
			char c;
			scanf(" %c",&c);
			int x = c - '0';
			if(x > 0 && cnt < i) {
				ans += (i - cnt);
				cnt = i;
			}
			cnt += x;
		}
		printf("Case #%d: %d\n",cases, ans);
	}
}