#include <cstdio>
#include <cstring>
using namespace std;

int main() {

	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t) {
		int n;
		scanf("%d ", &n);

		int sum = 0, sol = 0;
		for (int i = 0; i <= n; ++i) {
			char ch = getchar();
			int k = ch - '0';

			if (sum <= i) {
				sol += (i - sum);
				sum = i;
			}
			sum += k;
		}
		getchar(); // read \n

		printf("Case #%d: %d\n", t, sol);
	}

	return 0;
}