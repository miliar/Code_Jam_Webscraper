#include <bits/stdc++.h>
using namespace std;

FILE *fout = fopen("output.out", "w");

int N, J;
vector<int> sol1;
vector<vector<long long>> sol2;

long long change(int jamcoin, int base) {
	long long ret = 0;
	for (long long pw = 1; jamcoin; pw *= base)
		ret += pw * (jamcoin & 1), jamcoin >>= 1;
	return ret;
}

int isprime(long long n) {
	if (n == 1) return 0;
	for (long long i = 2; i * i <= n; ++i)
		if (n % i == 0) return 0;
	return 1;
}

long long divisor(long long n) {
	for (long long i = 2; i * i <= n; ++i)
		if (n % i == 0) return i;
	assert(0 && "never can reach here");
}

string change(int jamcoin) {
	string ret;
	while (jamcoin) ret.push_back((jamcoin & 1) + '0'), jamcoin >>= 1;
	while (ret.size() < N) ret.push_back('0');
	reverse(ret.begin(), ret.end());
	return ret;
}

int main() {
	scanf("%*d%d%d", &N, &J);
	for (int mid = 0; mid < (1 << (N - 2)); ++mid) {
		int jamcoin = (1 << (N - 1)) | (mid << 1) | 1;
		int isNotAllPrime = 1;
		for (int b = 2; b <= 10; ++b) {
			long long n = change(jamcoin, b);
			isNotAllPrime &= !isprime(n);
		}
		if (isNotAllPrime) {
			sol1.push_back(jamcoin);
			sol2.push_back(vector<long long>());
			for (int b = 2; b <= 10; ++b) {
				long long n = change(jamcoin, b);
				sol2.back().push_back(divisor(n));
			}
			if ((int)sol1.size() == J) break;
		}
	}
	fprintf(fout, "Case #1:\n");
	for (int i = 0; i < (int)sol1.size(); ++i) {
		fprintf(fout, "%s", change(sol1[i]).c_str());
		for (int j = 0; j < (int)sol2[i].size(); ++j)
			fprintf(fout, " %lld", sol2[i][j]);
		fprintf(fout, "\n");
	}
	return 0;
}