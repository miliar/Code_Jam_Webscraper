#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <climits>
#include <cfloat>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stdexcept>

using namespace std;

#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ULL unsigned long long
#define LL long long
#define REP(i,n) for(int i=0;i<(n);i++)
#define set_bit(x, i) (x) |= (1 << (i))
#define clr_bit(x, i) (x) & ~(1 << (i))
#define tog_bit(x, i) (x) ^= (1 << (i))
#define chk_bit(x, i) (((x) >> (i)) & 1)
#define feq(x,y) (fabs(x-y) <= DBL_EPSILON)

#define MAXN 33000

#define MOD 1000000007

typedef pair<int,int> ii;
#define mp make_pair


#define sq(x) ((x)*(x))


set<int> S;

int count(ULL x) {

	int na = 0;
	while(x) {
		int d = x % 10;
		if(S.find(d) == S.end()) {
			na++;
			S.insert(d);
		}
		x /= 10;
	}
	return na;
}

ULL solve(ULL x) {

	int na = 0;
	S.clear();
	ULL y = 0;
	while(na < 10) {
		y += x;
		na += count(y);
	}
	return y;
}



//#define ONLINE_JUDGE
int main() {

#ifndef ONLINE_JUDGE
	//freopen("test", "r", stdin);
	freopen("in-large", "r", stdin);
	freopen("out-large", "w+", stdout);
#endif

	int testcases = 1000;
	scanf("%d", &testcases);
	for(int k=1;k<=testcases;k++) {
		//ULL x = rand() % 100000;
		ULL x;
		scanf("%llu", &x);
		if(x == 0) {
			printf("Case #%d: INSOMNIA\n", k);
		}
		else {
			ULL ans = solve(x);
			printf("Case #%d: %llu\n", k, ans);
		}
	}

	return 0;
} 


