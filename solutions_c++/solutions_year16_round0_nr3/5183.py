#include <bits/stdc++.h>

using namespace std;

const int N = 16;
const int NP = 4;
int primes[] = {2, 3, 5, 7};
int remain[11], binCode[N];

struct Base{
	int base;
	int mod[NP][N];

	void init(int x) {
		base = x;
		for(int i = 0; i < NP; ++i) {
			mod[i][0] = 1 % primes[i];
			for(int at = 1; at < N; ++at)
				mod[i][at] = (mod[i][at - 1] * base) % primes[i];
		}
	}

	int calc() {
		for(int i = 0; i < NP; ++i) {
			int sum = 0;
			for(int at = 0; at < N - 2; ++at)
				if (binCode[at])
					sum = (sum + mod[i][at]) % primes[i];
			sum = ((sum * base) % primes[i] + mod[i][0] + mod[i][N - 1]) % primes[i];
			if (sum == 0) return primes[i];
		}
		return -1;
	}
} check[11];

int main() {
	printf("Case #1:\n");
	int C = 50;
	for(int i = 2; i < 11; ++i) check[i].init(i);
	for(int mask = 0; mask < (1 << (N - 2)); ++mask) {
		for(int i = 0, cur = mask; i < N - 2; ++i) {
			binCode[i] = cur % 2;
			cur /= 2;
		}
		reverse(binCode, binCode + N - 2);
		bool all = true;
		for(int base = 2; base < 11; ++base) {
			remain[base] = check[base].calc();
			if (remain[base] == -1){
				all = false;
				break;
			}
		}
		if (all) {
			printf("1");
			for(int i = 0; i < N - 2; ++i) printf("%d", binCode[i]);
			printf("1 ");
			for(int base = 2; base < 11; ++base) printf("%d ", remain[base]);
			printf("\n");
			--C;
			if (C == 0) break;
		}
	}
	return 0;
}