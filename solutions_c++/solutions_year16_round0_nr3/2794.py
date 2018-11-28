# include <stdio.h>
# include <vector>

using namespace std;

# define MAXP 100000000
# define N 14
# define J 50

vector<int> prime;
bool notPrime[MAXP];

void genPrime() {
	notPrime[0] = notPrime[1] = true;

	for (int i = 2; i < MAXP; i ++) {
		if (!notPrime[i]) prime.push_back(i);

		for (int j = 0; j < prime.size() && i * prime[j] < MAXP; j ++) {
			notPrime[i * prime[j]] = true;
			if (i % prime[j] == 0) break;
		}
	}
}

vector<int> test(int x) {
	vector<int> ans;

	for (long long base = 2; base <= 10; base ++) {
		long long cur = 1;
		long long mul = 1;
		for (int i = 0; i < N; i ++) {
			mul *= base;
			if (x & (1 << i)) {
				cur += mul;
			}
		}
		cur += mul * base;

		bool flag = false;
		for (int i = 0; i < prime.size() && prime[i] * prime[i] < cur; i ++) {
			if (cur % prime[i] == 0) {
				ans.push_back(prime[i]);
				flag = true;
				break;
			}
		}

		if (!flag) return ans;
	}

	return ans;
}

void print(int x, vector<int> ok) {
	printf("1");
	for (int i = N - 1; i >= 0; i --) {
		if (x & (1 << i)) printf("1"); else printf("0");
	}
	printf("1 ");

	for (int i = 0; i < 8; i ++) {
		printf("%d ", ok[i]);
	}

	printf("%d\n", ok[8]);
}

int main() {
	freopen("b.txt", "w", stdout);
	
	genPrime();

	printf("Case #1:\n");

	int ans = 0;
	for (int i = 0; i < (1 << N) && ans < J; i ++) {
		vector<int> ok = test(i);

		if (ok.size() == 9) {
			ans ++;
			print(i, ok);
		}
	}
}