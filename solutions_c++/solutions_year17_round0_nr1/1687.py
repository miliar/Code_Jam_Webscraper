#include <bits/stdc++.h>
using namespace std;

char str[1005], f[1005];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int i, flip, k, n, kase = 0, testcase, ans;
	scanf("%d", &testcase);
	while(testcase --){
		scanf("%s%d", str + 1, &k);
		n = strlen(str + 1);
		for(i = 1; i <= k; ++ i) f[i] = 0;
		for(i = 1, flip = ans = 0; i + k - 1 <= n; ++ i){
			str[i] = (str[i] == '-');
			flip ^= f[i];
			if(str[i] ^ flip) ++ ans, f[i + k] = 1, flip ^= 1;
			else f[i + k] = 0;
		}
		for(; i <= n; ++ i){
			flip ^= f[i];
			if(flip ^ (str[i] == '-')) break;
		} printf("Case #%d: ", ++ kase);
		if(i <= n) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	} return 0;
}
