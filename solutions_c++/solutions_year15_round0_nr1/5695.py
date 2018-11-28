#include <bits/stdc++.h>

using namespace std;

int arr[1010], S;

int main() {
	int T, tc=1, i, cur, res;
	scanf("%d", &T);
	while (T--) {
		scanf("%d ", &S);
		S++;
		for (i=0; i<S; i++) {
			scanf("%1d", &arr[i]);
		}
		res = cur = 0;
		for (i=0; i<S; i++) {
			if (cur < i) {
				cur++;
				res++;
			}
			cur += arr[i];
		}
		printf("Case #%d: %d\n", tc++, res);
	}
	return 0;
}