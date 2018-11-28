#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
double a[1100], b[1100];

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int cas; scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		scanf("%d", &n); 
		for (int i = 0; i < n; i++) scanf("%lf", &a[i]);
		for (int i = 0; i < n; i++) scanf("%lf", &b[i]);
		sort(a, a + n); sort(b, b + n);
		printf("Case #%d: ", t); m = 0;
		for (int i = 0; i < n; i++) 
			if (a[i] > b[m]) ++m; 
		printf("%d ", m); m = 0;
		for (int i = 0; i < n; i++) 
			if (b[i] > a[m]) ++m; 
		printf("%d\n", n - m);
	}
	return 0;
}

