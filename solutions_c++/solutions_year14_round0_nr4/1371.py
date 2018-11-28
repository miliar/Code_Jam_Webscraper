#include <cstdio>
#include <algorithm>

using namespace std;

double a[1001], b[1001];

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t ++){
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i ++)
			scanf("%lf", &a[i]);
		for (int j = 0; j < n; j ++)
			scanf("%lf", &b[j]);
		sort(a, a + n);
		sort(b, b + n);
		int k = 0, ans1 = 0, ans2 = n;
		for (int i = 0; i < n; i ++){
			while (k < n && a[k] < b[i])
				k ++;
			if (k < n){
				ans1 ++; k ++;
			}
		}
		int j = 0;
		for (int i = 0; i < n; i ++){
			while (j < n && b[j] < a[i]) 
				j ++;
			if (j < n){
				ans2 --; j ++;
			}
		}
		printf("Case #%d: %d %d\n", t+1, ans1, ans2);
	}
	return 0;
}
