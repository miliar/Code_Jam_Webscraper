#include <bits/stdc++.h>
using namespace std;

int main(){
	int x;
	scanf(" %d ",&x);
	for(int z = 1; z <= x; z++){
		printf("Case #%d: ", z);
		int n, c = 0, ans = 0;
		char a[1005];
		scanf(" %d %s ", &n, a);
		for(int i = 0; i <= n; i++){
			int np = max(0,i-c);
			ans += np;
			c += a[i]-'0'+np;
		}
		printf("%d\n", ans);
	}
	return 0;
}
			
