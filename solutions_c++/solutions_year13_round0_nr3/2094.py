
#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;

typedef long long LL;

vector<LL> fairSquares;

int nextInt() {
	int res;
	scanf("%d", &res);
	return res;
}

LL nextLL() {
	LL res;
	scanf("%lld", &res);
	return res;
}

inline bool palindrome(LL x) {
	static int digs[16];
	int count = 0;
	while (x > 0) {
		digs[count++] = x % 10;
		x /= 10;
	}
	for (int i = 0; i < count; ++i) {
		if (digs[i] != digs[count - 1 - i])
			return false;
	}
	return true;
}

void init() {
	for (LL x = 1; x <= 10000000LL; ++x) {
		if (palindrome(x * x) && palindrome(x)) {
			fairSquares.push_back(x * x);
		}
	}
}

int main() {
	init();
	int tst = nextInt();
	for (int cas = 0; cas < tst; ++cas) {
		LL A = nextLL();
		LL B = nextLL();
		int res = 0;
		for (int i = 0; i < (int)fairSquares.size(); ++i)
			if (fairSquares[i] >= A && fairSquares[i] <= B)
				++res;
		printf("Case #%d: %d\n", cas + 1, res);
	}
	return 0;
}