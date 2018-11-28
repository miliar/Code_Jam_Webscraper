#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

const int BOUND = 100;

vector<int> answer;
vector<int> prime;


int n, cnt;

bool pass(long long x) {
	static vector<int> divisor;
	divisor.clear();

	for (int base = 2; base <= 10; base++) {
		bool succ = false;
		int divide = 0;
		for (int i = 0; i < (int)prime.size(); i++) {
			int remain = 0;
			for (int j = n - 1; j >= 0; j--) {
				remain = remain * base + (x >> j & 1);
				remain %= prime[i];
			}
			//cout << remain << endl;
			if (remain == 0) {
				succ = true;
				divide = prime[i];
				break;
			}
		}
		if (succ) {
			divisor.push_back(divide);
		} else {
			return false;
		}
	}
	//cout << x << " ";
	for (int j = n - 1; j >= 0; j--) {
		printf("%d", x >> j & 1 ? 1 : 0);
	}
	for (int i = 0; i < (int)divisor.size(); i++) {
		printf(" %d", divisor[i]);
	}
	puts("");
	return true;
}

int main() {
	{
		int tests;
		scanf("%d", &tests);
		printf("Case #%d:\n", 1);
	}

	for (int i = 2; i <= BOUND; i++) {
		bool is_prime = true;
		for (int j = 2; j < i; j++) {
			if (i % j == 0) {
				is_prime = false;
			}
		}
		if (is_prime) {
			prime.push_back(i);
		}
	}

	scanf("%d %d", &n, &cnt);
	for (int mask = 0; mask < (1LL << (n - 2)) && cnt; mask++) {
		if (pass((1LL << (n - 1)) + (mask << 1) + 1)) {
			cnt--;
		}
	}
	return 0;
}
