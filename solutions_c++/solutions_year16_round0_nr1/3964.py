#include <cstdio>
#include <iostream>
#include <set>
using namespace std;

#define BASE 10
#define MAXN 100

void printLast(int n) {
	if (n == 0) {
		cout << "INSOMNIA\n";
		return;
	}

	set<int> digits;

	bool found = false;
	for (int i = 1; i <= MAXN; i++) {
		int temp = i * n;
		while (temp > 0) {
			digits.insert(temp % 10);
			temp /= 10;
		}

		if (digits.size() == BASE) {
			cout << (i * n) << '\n';
			found = true;
			break;
		}
	}

	if (!found)
		cout << "INSOMNIA\n";
}

int main(void) {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, N;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> N;
		cout << "Case #" << t << ": ";
		printLast(N);
	}
	return 0;
}
