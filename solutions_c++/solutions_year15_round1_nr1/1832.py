#include <iostream>
#include <vector>
#include <algorithm>

#define PB push_back

using namespace std;

int main() {
	int n, t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		scanf("%d", &n);
		vector<int> V;
		int m;
		int maks = 0;
		int last;
		int sum = 0;
		int sum2 = 0;
		scanf ("%d", &last);
		V.PB(last);
		n--;
		while (n--) {
			scanf ("%d", &m);
			maks = max(maks, max(last - m, 0));
			sum += max(last - m, 0);
			last = m;
			V.PB(m);
		}

		for(int k = 0; k < V.size() - 1; ++k) {
			sum2 += min(maks, V[k]);
		}
		printf ("Case #%d: %d %d\n", i, sum, sum2);
	}
	return 0;
}