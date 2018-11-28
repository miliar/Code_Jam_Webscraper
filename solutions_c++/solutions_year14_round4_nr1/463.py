#include <stdio.h>
#include <algorithm>

int a[10001];

int main(){
	int T, n, x;
	scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		scanf("%d%d", &n, &x);
		for(int i=0; i<n; ++i) scanf("%d", &a[i]);
		std::sort(a, a+n);
		int ans = 0;
		int st = 0, ed = n-1;
		while(st <= ed){
			if(ed == st){
				++ans;
				++st;
			}
			else if(a[ed] + a[st] <= x){
				st++;
				ed--;
				ans++;
			}
			else{
				ed--;
				ans++;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
