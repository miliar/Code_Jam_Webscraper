#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, x, y) for(int i = (x); i <= (y); i++)
#define RFOR(i, x, y) for(int i = (x); i >= (y); i--)

#define REMIN(x, y) x = (x < (y)) ? x : (y)
#define REMAX(x, y) x = (x > (y)) ? x : (y)

//#define DEBUG

#ifndef DEBUG
#define ISDEBUG false
#define PRINT(x)
#else
#define ISDEBUG true
#define PRINT(x) cout << #x << ": " << x << endl
#endif
#define IFDEBUG() if(ISDEBUG)

using namespace std;

//#define MAX 1024000
#define MAX 1024

long long P, Q;
int pc;
long long prime[MAX];

bool is_prime(long long x) {
	REP(i, pc) {
		if(x % prime[i] == 0) {
			return false;
		}
	}
	return true;
}

void gen_prime() {
	pc = 0;
	prime[pc++] = 2;
	for(long long i = 3; i < MAX; i += 2) {
		if(is_prime(i)) {
			prime[pc++] = i;
		}
	}
}

long long lcm(long long x, long long y) {
	if(x > y) {
		return lcm(x, y);
	}

	if(y % x == 0) {
		return x;
	}

	REP(i, pc) {
		if(prime[i] * prime[i] > x)break;
		if(x % prime[i] == 0 && y % prime[i] == 0) {
			return prime[i] * lcm(x / prime[i], y / prime[i]);
		}
	}
	return 1;
}

void find_ans() {
	scanf("%lld/%lld", &P, &Q);

	long long l = lcm(P, Q);
	P /= l;
	Q /= l;

	long long t = Q;
	while(t > 1) {
		if(t % 2 != 0) {
			printf("impossible");
			return;
		}
		t /= 2;
	}

	long long ans = 0;
	while(P < Q) {
		if(Q % 2 != 0) {
			printf("impossible");
			return;
		}
		ans++;
		Q /= 2;
	}
	printf("%lld", ans);
}

int main() {
	int i, c;

	gen_prime();

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
