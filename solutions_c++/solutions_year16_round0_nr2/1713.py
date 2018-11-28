#include <bits/stdc++.h>

using namespace std;

int TC, N, k, ans;
char tmp[110];

// Store as 1 or -1, easier to manipulate
// 1 = +, -1 = -
int arr[110];

// flip at k means:
// [0,k] switch signs
// [k+1,n-1] unchanged
int flip(int k) {
	for (int i = 0; i <= k; i++) {
		arr[i] *= -1;
	}
}

int firstPointOfDifference() {
	for (int i = 1; i < N; i++) {
		if (arr[0] != arr[i]) {
			return i-1;
		}
	}
	return N;
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%s", tmp);
		N = strlen(tmp);
		for (int i = 0; i < N; i++) {
			if (tmp[i] == '+') {
				arr[i] = 1;
			} else {
				arr[i] = -1;
			}
		}

		// Greedily flip
		ans = 0;
		while (k = firstPointOfDifference(), k != N) {
			flip(k);
			ans++;
		}
		if (arr[0] == -1) ans++; // It's all --...-, need 1 more flip
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}