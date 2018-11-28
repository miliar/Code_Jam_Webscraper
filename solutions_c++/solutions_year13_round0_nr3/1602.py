#include <cstdio>
#include <vector>
using namespace std;

vector<long long> palindromy;

bool palindrom(long long x) {
	int tmp[20];
	int i = 0;
	while (x) {
		tmp[i++] = x%10;
		x /= 10;
	}
	for (int j = 0; j < i/2; ++j) {
		if (tmp[j] != tmp[i-j-1]) return false;
	}
	return true;
}

int cnt(long long x) {
	for (int i = 0; i < palindromy.size(); ++i) {
		if (palindromy[i] > x) return i;
	}
	return palindromy.size();
}

int main() {
	long long n = 1;
	while (true) {
		if (n*n > 100000000000000LL) break;
		if (palindrom(n) && palindrom(n*n)) {
			palindromy.push_back(n*n);
		}
		++n;
	}
	
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		long long a, b;
		scanf("%lld %lld\n", &a, &b);
		printf("Case #%d: %d\n", tt, cnt(b) - cnt(a-1));
	}
}
