#include <bits/stdc++.h>
using namespace std;
int tcs, n, x, s[1000000], u[10000000];
int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		scanf("%i%i", &n, &x);
		for(int i=0;i<n;i++){
			scanf("%i", &s[i]);
		}
		sort(s, s+n);
		memset(u, 0, sizeof u);
		int ans = 0;
		for(int i=n-1;i>=0;i--){
			if(u[i]) continue;
			ans++;
			u[i] = 1;
			int k = upper_bound(s, s+n, x - s[i]) - s;
			if(k == 0) continue;
			k--;
			while(u[k] && k != 0) k--;
			if(u[k] && k == 0) continue;
			u[k] = 1;
		}
		printf("Case #%i: %i\n", tc, ans);
	}
}