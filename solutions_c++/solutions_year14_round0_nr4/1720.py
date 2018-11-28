#include <stdio.h>
#include <algorithm>

double a[1001], b[1001];

int main(){
	int T, n;
	int x, y;
	int pos_a, pos_b;
	scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		scanf("%d", &n);
		for(int i=0; i<n; ++i) scanf("%lf", &a[i]);
		for(int i=0; i<n; ++i) scanf("%lf", &b[i]);
		std::sort(a, a+n);
		std::sort(b, b+n);
		//for(int i=0; i<n; ++i) printf("%.3lf ", a[i]);
		//printf("\n");
		//for(int i=0; i<n; ++i) printf("%.3lf ", b[i]);
		//printf("\n");
		x = y = 0;
		pos_a = pos_b = 0;
		while(pos_a<n && pos_b < n){
			if(a[pos_a] > b[pos_b]){
				x++;
				pos_a++;
				pos_b++;
			}
			else pos_a++;
		}
		pos_a = pos_b = n-1;
		int tmp = 0;
		while(pos_a>=0 && pos_b >= tmp){
			if(a[pos_a] > b[pos_b]){
				tmp++;
				pos_a--;
				y++;
			}
			else{
				pos_a--;
				pos_b--;
			}
		}
		printf("Case #%d: %d %d\n", t, x, y);
	}
	return 0;
}

