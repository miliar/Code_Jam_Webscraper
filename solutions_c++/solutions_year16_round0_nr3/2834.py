#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

map<ll, ll> factor;

bool isPrime(ll N) {
	if (factor.find(N) != factor.end()) return false;
	for (ll i = 2; i * i <= N; ++i)
		if ( N % i == 0 ) {
			factor[N] = i;
			return false;
		}
	return true;
}

// Convert binary string to base number.
ll convertNum(ll bin, ll base) {
	ll num = 0, acc = 1;
	for (int i = 0; i < 32; ++i) {
		if (bin & ( 1 << i ) ) num += acc;
		acc *= base;
	}
	return num;
}

bool tryNum(ll n) {
	if (isPrime(n)) return false;
	for (ll i = 3; i <= 10; ++i) {
		ll num = convertNum(n, i);
		if (isPrime(num)) return false;
	}
	return true;
}

void printBinary(ll num, int len) {
	for (int i = len - 1; i >= 0; --i) {
		if (num & (1 << i)) printf("1");
		else printf("0");
	}
}

vector<ll> getOfLength(int len, int k) {
	int test = (1 << (len - 2)), b = (1 << (len - 1));
	vector<ll> ans;
	while (ans.size() < k && test < b) {
		ll testing = (test << 1) | 1;
		if (tryNum(testing)) {
			ans.push_back(testing);
		}
		++test;
	}
	return ans;
}

void printLen(ll num, int k) {
	printBinary(num, k);
	for (int i = 2; i <= 10; ++i) {
		ll n = convertNum(num, i);
		printf(" %lld", factor[n]);
		//printf("(%lld) ", n);
	}
	printf("\n");
}

int main() {
	int T, N, J;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d:\n");
		scanf("%d %d", &J, &N);
		vector<ll> ans = getOfLength(J, N);
		for (int i = 0; i < ans.size(); ++i) {
			// printf("%d : ", i);
			printLen(ans[i], J);
		}
	}
	return 0;
}

