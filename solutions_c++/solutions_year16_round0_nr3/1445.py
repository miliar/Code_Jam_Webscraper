#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<bitset>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}
const static int M = 1e6;
const static int B = 16;
bool primes[M];
vector<int> p;
long long found(long long n) {
	for(int i = 0; i < p.size() && p[i] < n; ++i) {
		if (n % p[i] == 0) {
			return p[i];
		}
	}
	return -1;
}
long long comp(bitset<B> n, int d) {
	long long res = 0;
	long long p = 1LL;
	for(int i = 0; i < B; ++i) {
		if (n[i]) {
			res += p;
		}
		p *= d;
	}
	return res;
}
int solve() {
	int a, b; cin >> a >> b;;
	for(int i = 0; i < M; ++i) {
		primes[i] = true;
	}
	primes[0] = primes[1] = false;
	for(int j = 2; j < M; ++j) {
		if (primes[j]) {
			p.push_back(j);
			for(int i = 2*j; i < M; i += j) {
				primes[i] = false;
			}
		}
	}
	for(int n = (1 << (B - 1)) + 1; n < 1 << B; n += 2) {
		bitset<B> no(n);
		bool pr = false;
		//cerr << no << endl;;
		vector<long long> res;
		for(int d = 2; d <= 10; ++d) {
			long long dd = found(comp(no, d));
			if (dd == -1) {
				pr = true;
				break;
			}
			res.push_back(dd);
		}
		if (!pr) {
			--b;
			cout << no << no;
			for(int i = 0; i < 9; ++i) {
				cout << " " << res[i];
			}
			cout << endl;
		}
		if (b == 0) break;
	}
	return 0;
}

int main() {
	int t; cin >> t;
	for(int x = 1; x <= t; ++x){
		cout << "Case #" << x << ":\n";
	 solve();;//result 
	}
	return 0;
}
