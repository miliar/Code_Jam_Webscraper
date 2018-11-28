#include<cstdio>

int input[1000];

int main() {
	int T;
	scanf("%d", &T);
	for (int nm=1;nm<=T;nm++) {
		int n;
		scanf("%d", &n);
		for (int i=0;i<n;i++) {
			scanf("%d", &input[i]);
		}
		int ans1 = 0, ans2 = 0;
		for (int i=1;i<n;i++) {
			if (input[i] < input[i-1]) ans1 += input[i-1] - input[i];
		}
		int max = 0;
		for (int i=1;i<n;i++) {
			if (input[i-1] - input[i] > max) max = input[i-1] - input[i];
		}
		for (int i=0;i<n-1;i++) {
			if (input[i] < max) {
				ans2 += input[i];
			}
			else {
				ans2 += max;
			}
		}
		printf("Case #%d: %d %d\n", nm, ans1, ans2);
	}
	return 0;
}
