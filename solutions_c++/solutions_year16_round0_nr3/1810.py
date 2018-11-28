#include <stdio.h>
#include <vector>
#include <set>

using namespace std;

vector<long long> prime;
long long base[11][40];

void build()
{
	prime.push_back(2LL);
	prime.push_back(3LL);
	for (long long x = 3LL; x <= 1LL<<17; x++) {
		bool isPrime = true;
		for (int i = 0; i < int(prime.size()) && prime[i]*prime[i] <= x; i++) {
			if (x%prime[i] == 0) {
				isPrime = false;
				break;
			}
		}

		if (isPrime) {
			prime.push_back(x);
		}
	}

	for (int i = 2; i <= 10; i++) {
		base[i][0] = 1LL;
		for (int j = 1; j <= 33; j++)
			base[i][j] = base[i][j-1] * i;
	}
}

int N, T, J;
int jamcoin[40];

void check()
{
	long long sum[15];
	long long divisor[15];
	bool hasPrime = false;
	for (int i = 2; i <= 10; i++) {
		sum[i] = base[i][0] + base[i][N-1];
		for (int j = 1; j < N-1; j++)
			sum[i] += base[i][j] * jamcoin[j];

		bool isPrime = true;
		for (int j = 0; j < int(prime.size()) && prime[j]*prime[j] <= sum[i]; j++) {
			if (sum[i]%prime[j] == 0) {
				divisor[i] = prime[j];
				isPrime = false;
				break;
			}
		}
		if (isPrime) {
			hasPrime = true;
			break;
		}
	}

	if (!hasPrime) {
		J--;
		for (int i = N-1; i >= 0; i--)
			printf("%d", jamcoin[i]);
		for (int i = 2; i <= 10; i++)
			printf(" %lld", divisor[i]);
		puts("");
	}
}

void dfs(int lv)
{
	if (J == 0)
		return;
	if (lv == N-1) {
		check();
		return;
	}

	jamcoin[lv] = 0;
	dfs(lv+1);
	jamcoin[lv] = 1;
	dfs(lv+1);
}

void solve()
{
	for (int i = 0; i < 40; i++)
		jamcoin[i] = 0;
	jamcoin[0] = jamcoin[N-1] = 1;
	dfs(1);
}

int main()
{
	build();
	scanf(" %d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf(" %d %d", &N, &J);
		printf("Case #%d:\n", cas);
		solve();
	}
	return 0;
}