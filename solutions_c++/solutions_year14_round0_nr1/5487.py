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

void set_row(int *T) {
	int row, val;
	scanf("%d", &row);
	FOR(i,0,4) FOR(j,0,4) {
		scanf("%d", &val);
		if(i == row -1) ++T[val];
	}
}

void testcase(int zzz) {
	int T[17];
	FOR(i,1,17) T[i] = 0;
	set_row(T);
	set_row(T);
	list<int> L;
	FOR(i,1,17) if(T[i] == 2) L.push_back(i);
	//FOR(i,1,17) printf("%d ", T[i]);
	//printf("\n");
	printf("Case #%d: ", zzz);
	if(L.size() == 1)
		printf("%d\n", L.front());
	else if(L.size() > 1)
		printf("Bad magician!\n");
	else
		printf("Volunteer cheated!\n");
}

int main() {
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) testcase(zzz + 1);
	return 0;
}
