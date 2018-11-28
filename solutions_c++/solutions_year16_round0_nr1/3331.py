#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

void print_result(int t, int result) {
	if (result == -1) {
		printf("Case #%d: INSOMNIA\n", t);
	} else {
		printf("Case #%d: %d\n", t, result);
	}
}

bool check_digit_in_n(int d, int n) {
	while (n > 0) {
		if (n % 10 == d) return true;
		n /= 10; 
	}
	return false;
}

int solve(int n) {
	if(n == 0) return -1;
	int x = n;
	vector<bool> dig(10, false);
	int ile = 0;
	while (ile < 10) {
		for (int i = 0; i < 10; ++i) {
			if (!dig[i]) {
				dig[i] = check_digit_in_n(i, x);
				ile += dig[i];
			}
		}
		if (ile < 10)
			x += n;
	}
	return x;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n;
		scanf("%d", &n);
		int result = solve(n);
		print_result(t, result);
	}
	return 0;
}