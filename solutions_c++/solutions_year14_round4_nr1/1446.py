#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int x = 1; x <= t; x++){
		printf("Case #%d: ", x);
		int n, x, a[10005];
		scanf("%d %d", &n, &x);
		for(int i=0; i <n; i++){
			scanf("%d", &a[i]);
		}
		sort(a, a+n);
		int c = 0, ans = n;
		for(int i = n-1; i >= 0; i--){
			if(i <= c) break;
			if(a[i]+a[c] <= x){
				ans--;
				c++;
			}
		}
		printf("%d\n", ans);
	}

	return 0;
}

