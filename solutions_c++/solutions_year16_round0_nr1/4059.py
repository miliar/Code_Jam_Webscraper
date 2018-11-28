#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long lld;
bool OK(bool check[11]) {
	for (int i = 0; i <= 9; i++) {
		if (check[i] == false)
			return true;
	}
	return false;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int TestCase = 1; TestCase <= T; TestCase++) {
		lld N;
		bool check[11] = { 0, };

		scanf("%lld", &N);

		printf("Case #%d: ", TestCase);
		if (N == 0) {
			printf("INSOMNIA\n");
			continue;
		}

		int i = 1;
		do {
			lld tmp = N * i;
			while (tmp > 0) {
				check[tmp % 10] = true;
				tmp /= 10;
			}
			i++;
		} while (OK(check));

		printf("%lld\n", N * (i - 1));
	}
	return 0;
}