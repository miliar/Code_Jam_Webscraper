//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define N 100010

vector<int> primes;
int n, m;
set<int> ans;

void Test(int K) {
	if (ans.find(K) != ans.end()) return;
	int divisors[11];
	for (int base = 2; base <= 10; base ++) {
		divisors[base] = -1;
		LL num = 1;
		for (int j = n - 3; j >= 0; j --) {
			num = num * base;
			if (K & (1 << j)) num += 1;
			if (num > primes.back()) num = primes.back() + 1;
		}
		Rep(i, primes.size()) {
			if (primes[i] >= num) break;
			int r = 1, cur = 1, k = K;
			for (int j = 0; j < n - 2; j++, k = k >> 1) {
				cur = cur * base % primes[i];
				if (k % 2 == 1) {
					r += cur;
					r %= primes[i];
				}
			}
			cur = cur * base % primes[i];
			r += cur;
			r %= primes[i];
			if (r == 0) { divisors[base] = primes[i]; break; }
		}
		if (divisors[base] == -1) return;
	}
	ans.insert(K);
	printf("1");
	for (int j = n - 3; j >= 0; j--) printf("%d", (K & (1<<j)) >> j);
	printf("1");
	for (int base = 2; base <= 10; base ++) printf(" %d", divisors[base]);
	puts("");
}

int	main(){
	for (int i = 2; i < 100000; i++) {
		bool isPrime = true;
		for (int j = 0; isPrime && j < primes.size() && sqr(primes[j]) <= i; j++)
			if (i % primes[j] == 0) isPrime = false;
		if (isPrime) primes.push_back(i);
	}
	int cas, tt = 0;
	cin >> cas;
	while (cas --) {
		cin >> n >> m;
		ans.clear();
		printf("Case #%d:\n", ++tt);
		while (ans.size() < m) {
			int k = rand() % (1 << (n - 2));
			Test(k);
		}
	}
	return 0;
}
