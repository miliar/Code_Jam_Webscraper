#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
	int t, n, i, j, ct1, ct2, tc = 0;
	double a[1000], b[1000];
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf("%lf", &a[i]);
		for(i = 0; i < n; i++)
			scanf("%lf", &b[i]);
		sort(a, a + n);
		sort(b, b + n);
		ct1 = ct2 = 0;
		i = j = n - 1;
		while(i >= 0 && j >= 0){
			if(a[i] > b[j])
				ct1++, i--, j--;
			else
				j--;
		}
		i = j = n - 1;
		while(i >= 0 && j >= 0){
			if(b[i] > a[j])
				ct2++, i--, j--;
			else
				j--;
		}
		printf("Case #%d: %d %d\n", ++tc, ct1, n - ct2);
	}
	return 0;
}
