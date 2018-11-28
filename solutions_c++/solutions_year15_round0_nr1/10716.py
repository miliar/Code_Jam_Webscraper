#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	int r = 1;
	scanf ("%d", &t);
	while (t--) {
		int k;
		scanf ("%d", &k);
		char str[k+1];
		scanf ("%s", str);
		int sum[k + 1];
		int i;
		sum [0] = (int)str[0] - 48;
		for (i = 1; i <= k; i++) {
				int m = (int)str[i] - 48;
				sum[i] = sum[i - 1] + m;
		}

		int ans = 0;
		for (i = 1; i <= k; i++) {
			if (ans + sum[i - 1] >= i)
				continue;
			else {
				int m = i - (ans + sum[i - 1]);
				ans += m;
			}

		}

		printf ("Case #%d: %d\n", r, ans);
		r++;
	}
	return 0;
}
