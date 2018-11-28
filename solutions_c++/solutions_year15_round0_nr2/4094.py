#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

unsigned cuts(unsigned n) {
	return ((unsigned)sqrt(n)) - 1;
}

unsigned divide(unsigned n, unsigned c) {
	return n % c ? n / c + 1 : n / c;
}
unsigned divide(unsigned n) {
	auto c = cuts(n);
	return n % c ? n / c + 1 : n / c;
}

void solvecase() {
	unsigned D;
	cin >> D;
	vector<unsigned> v(D + 1);
	for (unsigned i = 0; i < D; ++i) {
		cin >> v[i];
	}
	v[D] = 0;
	sort(v.begin(), v.end(), [](unsigned a, unsigned b){return a > b; });
	unsigned time = v[0];
	for (unsigned max_c = 1; max_c <= 3; ++max_c) {
		for (unsigned i = 1; i <= D; ++i) {
			unsigned m = v[i];
			unsigned t = 0;
			for (unsigned j = 0; j < i; ++j) {
				auto c = min(cuts(v[j]), max_c);
				auto d = divide(v[j], c + 1);
				t += c;
				if (d > m) m = d;
			}
			t += m;
			if (t < time)
				time = t;
		}
	}

	cout << time << endl;
}

int N;
int main() {
	cin >> N;
	for (int t = 1; t <= N; ++t) {
		cout << "Case #" << t << ": ";
		solvecase();
	}

	return 0;
}