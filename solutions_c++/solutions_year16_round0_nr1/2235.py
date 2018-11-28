#include "main.h"

using namespace std;

void Core::init() {}

void Core::solve() {
	int N;
	CGET(N);
	if (0 == N) {
		cout << "INSOMNIA";
		return;
	}
	set<int> abc;
	fori(i, 10) {
		abc.insert(i);
	}
	fori(i, 10000) {
		if (0 == i) continue;
		int n = N * i;
		while (n > 0) {
			abc.erase(n % 10);
			n /= 10;
		}
		if (abc.empty()) {
			cout << N * i;
			return;
		}
	}
}
