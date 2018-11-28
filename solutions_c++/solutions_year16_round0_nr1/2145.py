#include <iostream>
using namespace std;

int solve(int n) {
	if (n == 0) {
		return -1;
	}
	int k = 0;
	int flag = 0;
	while (flag < (1<<10) - 1) {
		int z = n * (++k);
		while (z) {
			flag |= 1 << (z % 10);
			z /= 10;
		}
	}
	return n * k;
}

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		int N; cin >> N;
		int ans = solve(N);
		cout << "Case #" << No << ": ";
		if (ans < 0) {
			cout << "INSOMNIA" << endl;
		} else {
			cout << ans << endl;
		}
	}
	return 0;
}
