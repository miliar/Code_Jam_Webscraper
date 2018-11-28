#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int x = 1; x <= t; x++){
		printf("Case #%d: ", x);
		int n;
		double a[1005], b[1005];
		scanf("%d", &n);
		for(int i = 0; i < n; i++) scanf("%lf", &a[i]);
		for(int i = 0; i < n; i++) scanf("%lf", &b[i]);
		sort(a, a+n);
		sort(b, b+n);
		int ai = 0, bi = 0, s = 0;
		while(bi < n){
			if(a[ai] < b[bi]){
				ai++;
				bi++;
			}
			else{
				s++;
				bi++;
			}
		}
		int ans = 0;
		for(int i = 0; i < n; i++){
			int c = 0;
			//printf("%lf %lf\n", a[i], b[i]);
			for(int j = i; j < n; j++){
				if(a[j] > b[j-i]){
					c++;
				}
			}
			ans = max(ans, c);
		}

		printf("%d %d\n", ans, s);
	}
	return 0;
}