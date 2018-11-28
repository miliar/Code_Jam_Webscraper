#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <climits>
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

void testcase(int zzz) {
	LD c, f, x, res, inc = 2, got = 0;
	scanf("%Lf%Lf%Lf", &c, &f, &x);
	//printf("%Lf %Lf %Lf\n", c, f, x);
	res = x / 2;
	while(true) {
		got += c / inc;
		inc += f;
		LD tmp = got + x / inc;
		//printf("got:%Lf inc:%Lf tmp:%Lf\n", got, inc, tmp);
		if(tmp > res) break;
		res = tmp;
	}
	printf("Case #%d: %.7Lf\n", zzz, res);
}

int main() {
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) testcase(zzz + 1);
	return 0;
}
