#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <list>
#include <ctime>
#include <sstream>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define mp(x,y) make_pair(x,y)
typedef short int sint;

const int N = 10;
LL n, p;

bool ok(LL a, LL nagr, LL round) {
	//printf("   ok(%lld, %lld, %lld)\n", a, nagr, round);
	if (nagr == 0) return false;
	if (a == 0) return true;
	LL b = (a - 1) - (a/2); // tyle mniejszych moze zostac
	LL dostaje = min(nagr, (1LL << (round-1)));
	return ok(b, nagr - dostaje, round - 1);
}

void solveG() {
	if (n == 1) {
		if (p == 1) printf("0 ");
		else printf("1 ");
		return ;
	}
	if (p <= (1LL << (n-1))) printf("0 ");
	else {
		LL start = 1, end = (1LL << n);
		LL sr;
		while (start < end) {
			sr = (start + end) / 2;
			if (!ok(sr, p, n)) {
				end = sr;
			} else {
				start = sr+1;
			}
		}
		printf("%lld ", start-1);
	}
}

bool okM(LL greater, LL nagr, LL round) {
	if (nagr == 0) return false;
	if (greater == 0) {
		if (nagr >= (1LL << (n - round))) return true;
		return false;
	}
	LL zost = (greater - 1) - greater/2;
	return okM(zost, nagr, round + 1);
}

void solveMax() {
	if (n == 1) {
		if (p == 1) printf("0\n");
		else printf("1\n");
		return ;
	}
	if (p > (1LL<<(n-1))) {
		if (p == (1LL << n)) printf("%lld\n", (1LL <<n) -1);
		else printf("%lld\n", (1LL << n) - 2);
	} else {
		LL start = 1, end = (1LL << n), sr;
		while (start < end) {
			sr = (start + end) / 2;
			if (!okM(sr, p, 0)) {
				start = sr+1;
			} else {
				end = sr;
			}
		}
		printf("%lld\n", (1LL << n) - sr - 1);
	}
}

int main(){
	int t;
	scanf("%d", &t);
	REP(i, t) {
		scanf("%lld %lld", &n, &p);
		printf("Case #%d: ", i+1);
		solveG();
		solveMax();
	}
}