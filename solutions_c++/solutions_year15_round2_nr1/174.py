#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

#define mp make_pair
#define pb push_back
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define all(c) (c).begin(), (c).end()
#define sz(c) (int)(c).size()


using namespace std;

typedef long long ll;

const int maxn = 1 << 23;
int p[maxn];
int d[maxn];

long long rev(long long n) {
	long long r = 0;
	while (n) {
		r = r * 10 + n % 10;
		n /= 10;
	}
	return r;
}

void calc() {
	for (int i = 0; i < maxn; i++) {
		d[i] = maxn;
		p[i] = -1;
	}
	d[0] = 0;
	p[0] = -1;
	for (int i = 0; i < maxn; i++) {
		if (i + 1 < maxn && d[i + 1] > d[i] + 1) {
			d[i + 1] = d[i] + 1;
			p[i + 1] = i;
		}
		int c = rev(i);
		if (c < maxn && d[c] > d[i] + 1) {
			d[c] = d[i] + 1;
			p[c] = i;
		}
	}
}

map<long long, long long> dp;

long long len(long long n) {
	int r = 0;
	while (n) {
		r++;
		n /= 10;
	}        
	return r;
}

long long solve2(long long n) {
	if (n <= 10) return n;
	if (n % 10 != 1) return 1 + solve2(n - 1);
	int l = (len(n) - 1) / 2 + 1;
	long long ten = 1;
	for (int i = 0; i < l; i++) ten *= 10LL;
	if ((n - 1) % ten == 0 && rev(n) < n) return 1 + solve2(rev(n));
	long long r = (n - 1) % ten;
	if (r != 0) return r + solve2(n - r);
	//if (rev(n) < n) return 1 + solve2(rev(n));
	return 1 + solve2(n - 1);
}

void solve(int test) {
	long long n;
	scanf("%lld", &n);
	//if (solve2(n) != d[n]) {
		//eprintf("n = %lld\n", n);
		//assert(0);
	//}
	printf("Case #%d: %lld\n", test, solve2(n));
}

int main(){
	calc();
	for (int i = 1; i < maxn; i++) {
		//if (p[i] != i - 1) printf("%d\n", i);
	} 

	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) solve(test);
}
