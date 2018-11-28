#include <cstdio>
#include <cmath>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		int n;
		scanf("%d", &n);
		char c;
		int wyn = 0;
		int res = 0;
		getchar();

		for(int j = 0; j<= n; ++j) {
			res += (int)fmax(0, j - wyn);
			wyn += (int)fmax(0, j - wyn);
			c = getchar();
			wyn += int(c) - 48;
		}
		getchar();
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}