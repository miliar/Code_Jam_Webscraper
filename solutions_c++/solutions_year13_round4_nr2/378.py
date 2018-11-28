#include <iostream>
#include <cassert>

using namespace std;

long long N, P;

long long could() {
	long long macht = 1;
	long long num = (1ll << N);
	long long bovengrens = num;
	long long cur = 0;
	while (true) {
		macht *= 2;
		if (macht > P) return cur;
		num /= 2;
		cur += num;
		assert(cur <= bovengrens);
	}
}

// sorry, it became a bit of a mess...
long long guaranteed() {
	long long macht = 1;
	long long num = (1ll << N);
	long long sum = 1;
	long long bovengrens = num;
	long long cur = 0;
	while (true) {
		num /= 2;
		sum += num;
		if (sum > P) return cur;
		if (num == 0) return bovengrens - 1;
		macht *= 2;
		cur += macht;
		assert(sum <= bovengrens);
	}
}

int main() {
	int T;
	cin >> T;
	assert(T > 0 && T <= 100);
	for (int cs = 1; cs <= T; cs++) {
		cin >> N >> P;
		assert(N >= 1 && N <= 50);
		assert(P >= 1 && P <= (1ll << N));
		cout << "Case #" << cs << ": " << guaranteed() << " " << could() << endl;
	}
	return 0;
}
