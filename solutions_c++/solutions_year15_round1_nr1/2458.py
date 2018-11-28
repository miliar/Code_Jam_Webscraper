#include <iostream>
using namespace std;

int a[1010];

int main()
{
	int T, t;
	int N, i;
	int ans1, ans2;
	int min;
	scanf("%d\n", &T);
	
	for (t = 1; t <= T; ++t) {
		scanf("%d\n", &N);
		min = ans1 = ans2 = 0;
		for (i = 0; i < N; ++i) {
			scanf("%d", &a[i]);
			if (i > 0 && a[i] - a[i-1] < 0) {
				ans1+=a[i-1] - a[i];
			}
			if (i > 0 && a[i] - a[i-1] < min) {
				min = a[i] - a[i-1];
			}
		}
		min = 0 - min;
		for (i = 0; i < N - 1; ++i) {
			ans2 += (min < a[i]) ? min : a[i];
		}
		printf("Case #%d: %d %d\n", t, ans1, ans2);
	}
}