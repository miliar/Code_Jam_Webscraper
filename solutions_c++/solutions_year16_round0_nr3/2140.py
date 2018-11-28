#include <cstdio>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

FILE *fout;
vector<long long> primes;
int e[100000];

void precalcPrimes() {
	for(long long i=2; i*i <= UINT_MAX; i++) {
		if(e[i] == 0) {
			primes.push_back(i);
			for (long long j = i; j*j <= UINT_MAX; j+=i) {
				e[j] = 1;
			}
		}
	}
}

int checkPrime(long long num) {
	for(int i=0; i<primes.size() && primes[i]*primes[i] <= num; i++)
		if (num % primes[i] == 0) return primes[i];
	return 0;
}

long long modBaseN(int *binary, int base, int mod) {
	long long ans = 0;
	long long c = 1;
	for(int i=0;i<32;i++) {
		ans=(ans+binary[i]*c)%mod;
		c*=base;
		c%=mod;
	}
	return ans;
}

int test(long long num) {
	int ans[11] = {0};
	ans[2] = checkPrime(num);
	if (!ans[2]) {
		return 0;
	}
	int binary[32] = {0};
	int l = 0;
	while (num) {
		binary[l++] = num % 2;
		num /= 2;
	}
	for (int i=3;i<=10;i++) {
		for(int j=0;j<100;j++) {
			if(modBaseN(binary, i, primes[j]) == 0) {
				ans[i] = primes[j];
				break;
			}
		}
		if(ans[i] == 0) return 0;
	}
	for(int i=l-1;i>=0;i--)fprintf(fout, "%d", binary[i]);
	fprintf(fout, " ");
	for (int i=2;i<=10;i++) fprintf(fout, "%d ",ans[i]);
	fprintf(fout, "\n");
	return 1;
}

int main(){
	freopen("input.txt","r",stdin);
	fout = fopen("output.txt", "w");
	precalcPrimes();
	int cases = 0;
	scanf("%d",&cases);
	for(int casenum = 1; casenum <= cases; casenum++) {
		int n, j;
		scanf("%d%d", &n, &j);
		fprintf(fout, "Case #%d:\n", casenum);
		for(int i=0;i<(1<<(n-2)) && j>0; i++) {
			long long num = (1LL<<(n-1)) + (i<<1) + 1;
			if (test(num)) printf("%d\n", --j);
			//if (i % 100000 == 0) printf("i = %d\n",i);
		}
	}
	return 0;
}