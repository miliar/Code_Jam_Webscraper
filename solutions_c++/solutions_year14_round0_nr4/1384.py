#include <cstdio>
#include <algorithm>
#define N 1010

using namespace std;

int cal(double a[], double b[], int n){
	int i, j;
	for (i = j = 0; i < n; i++, j++){
		while (j < n && b[j] < a[i]) j++;
		if (j == n) break;
	}
	return i;
}

int main(){
	int T, cas, n, i;
	double a[N], b[N];
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++){
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%lf", &a[i]);
		for (i = 0; i < n; i++)
			scanf("%lf", &b[i]);
		sort(a, a+n);
		sort(b, b+n);
		printf("Case #%d: %d %d\n", cas, cal(b, a, n), n-cal(a, b, n));
	}
}
