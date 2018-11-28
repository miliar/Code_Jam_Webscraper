#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;
const int MX = 10000001;

LG T[MX];
int top;

bool check_pal(LG x) {
	int s[20];
	int c = 0;
	while(x > 0) {
		s[c] = x % 10;
		x /= 10;
		++c;
	}
	int i = 0, j = c - 1;
	while(i < j) {
		if(s[i] != s[j]) return false;
		++i, --j;
	}
	return true;
}

void preproc() {
	FOR(i,0,MX) {
		LG x = LG(i) * LG(i);
		if(check_pal(i) && check_pal(x))
			T[top++] = x;
	}
}

void testcase(int zzz) {
	LG a, b;
	scanf("%lld%lld", &a, &b);
	int res = lower_bound(T, T + top, b + 1) - lower_bound(T, T + top, a);
	printf("Case #%d: %d\n", zzz, res);
}

int main() {
	preproc();
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) testcase(zzz + 1);
	return 0;
}
