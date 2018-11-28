#include <bits/stdc++.h>
using namespace std;
void init_ios() {ios_base::sync_with_stdio(false); cin.tie(nullptr);}

const int MAX = 100000000;
bool prime[MAX];
vector<int> prime_numbers, divisors;

void init_prime() {
	for (int i = 0; i < MAX; ++i) {
		prime[i] = true;
	}
	prime[0] = prime[1] = false;
	for (int i = 0; i * i < MAX; ++i) {
		if (!prime[i]) continue;
		for (int j = i * i; j < MAX; j += i) {
			prime[j] = false;
		}
	}
	for (int i = 0; i < MAX; ++i) if (prime[i]) {
		prime_numbers.push_back(i);
	}
}

int get_divisor(long long x) {
	for (size_t i = 0; i < prime_numbers.size(); ++i) if (x % prime_numbers[i] == 0) return prime_numbers[i];
	return -1;
}

long long convert(long long bin, int base) {
	long long ret = 0;
	int weight = 1;
	while (bin) {
		ret += (bin & 1) * weight;
		bin >>= 1;
		weight *= base;
	}
	return ret;
}

string binary_to_string(long long bin) {
	string ret;
	while (bin) {
		ret += (bin & 1 ? '1' : '0');
		bin >>= 1;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

void solve(int N, int J) {
	init_prime();

	vector<pair<string, vector<int>>> v;

	for (unsigned bit = 0; bit < 1 << (N / 2 - 1); ++bit) {
		long long bin = (bit << 1) + 1;

		int d;
		vector<int> ds;

		for (int base = 2; base <= 10; ++base) {
			long long x = convert(bin, base);
			if ((d = get_divisor(x)) == -1) break;
			ds.push_back(d);
		}

		if (ds.size() == 9) {
			v.emplace_back(binary_to_string(bin), ds);
			if (v.size() == (size_t)J) break;
		}
	}

	for (auto& p : v) {
		string str = p.first;
		while (str.size() + p.first.size() < (size_t)N) str += '0';
		str += p.first;
		printf("%s", str.c_str());
		for (auto& d : p.second) printf(" %d", d);
		puts("");
		if (--J == 0) break;
	}

	// printf("%zu\n", v.size());
}

int main() {
	int T, N, J;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%d%d", &N, &J);
		printf("Case #%d:\n", i);
		solve(N, J);
	}
	return 0;
}
