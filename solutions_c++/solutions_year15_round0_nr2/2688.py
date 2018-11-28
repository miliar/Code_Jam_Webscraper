#include <stdio.h>
#include <algorithm>
using namespace std;

int v[1010];

int main() {
	int _42=1, T;
	scanf(" %d ", &T);
	while (T--) {
		int D;
		scanf(" %d ", &D);
		int Pmax = 0;
		for (int i = 0; i < D; i++) {
			scanf(" %d ", &v[i]);
			Pmax = max(Pmax, v[i]);
		}
		int ans = Pmax;
		for (int i = 1; i <= Pmax; i++) {
			int cost = i;
			for (int j = 0; j < D; j++) {
				cost += (v[j]-1)/i;
			}
			ans = min(ans, cost);
		}
		printf("Case #%d: %d\n", _42++, ans);
	}
	return 0;
}

