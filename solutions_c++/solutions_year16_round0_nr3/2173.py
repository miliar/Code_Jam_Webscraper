#include <stdio.h>
#include <vector>
#include <unordered_set>
using namespace std;

vector<int> primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251};

int n, j;
unordered_set<int> seen;

int gen() {
	int res = rand();
	res &= n == 32 ? 0xFFFFFFFF : (1<<n)-1;
	res |= 1 << (n-1);
	res |= 1;
	return res;
}

int work(unsigned long long x, int b, int m) {
	int ans = 0;
	unsigned long long e = 1;
	for (int i = 0; i < n; i++) {
		if (x & (1 << i)) {
			ans = (ans + e) % m;
		}
		e = (e * b) % m;
	}
	return ans;
}

void check(int x) {
	vector<int> stuff;
	for (int i = 2; i <= 10; i++) {
		bool ok = false;
		for (int p: primes) {
			if (work(x, i, p) == 0) {
				stuff.push_back(p);
				ok = true;
				break;
			}
		}
		if (!ok) return;
	}
	j--;
	for (int i = n-1; i >= 0; i--) putchar(((x>>i)&1)+'0');
	for (int i = 2; i <= 10; i++) printf(" %d", stuff[i-2]);
	putchar('\n');
}

int main() {
	int one;
	srand(0xACACACAC);
	scanf("%d%d%d", &one, &n, &j);
	printf("Case #1:\n");
	while (j>0) {
		int c = gen();
		if (seen.count(c) == 0) {
			seen.insert(c);
			check(c);
		}
	}
}
