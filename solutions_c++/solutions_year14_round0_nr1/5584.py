#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wunused-result"
#else
#define _CRT_SECURE_NO_WARNINGS
#define _SCL_SECURE_NO_WARNINGS
#endif
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <string>
#include <iostream>
#define FOR(x,y,z) for (int x=(y); x<=(z); ++x)
#define FORD(x,y,z) for(int x=(y); x>=(z); --x)
#define REP(x,y) for (int x=0; x<(y); ++x)
#if defined(__GNUC__) && __cplusplus < 201103L
#define FOREACH(y,x) for (typeof((x).begin()) y = (x).begin(); y != (x).end(); ++y)
#else
#define FOREACH(y,x) for (auto y = (x).begin(); y != (x).end(); ++y)
#endif
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)(x).size())
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
const int INF = 1000000001;

int Go(VI r1, VI r2)
{
	sort(ALL(r1));
	sort(ALL(r2));
	VI t(4);
	int m = set_intersection(ALL(r1), ALL(r2), t.begin()) - t.begin();
	if (m == 0) return -1;
	else if (m == 1) return t[0];
	else return 0;
}

int main(int argc, char** argv)
{
	int tc;
	scanf("%d", &tc);
	FOR(tccc,1,tc) {
		int ans[2];
		VVI b[2];
		REP(k,2) {
			scanf("%d", &ans[k]);
			b[k].resize(4, VI(4));
			REP(i,4) {
				REP(j,4) scanf("%d", &b[k][i][j]);
			}
		}
		int res = Go(b[0][--ans[0]], b[1][--ans[1]]);
		printf("Case #%d: ", tccc);
		if (res >= 1) printf("%d", res);
		else if (res == 0) printf("Bad magician!");
		else printf("Volunteer cheated!");
		printf("\n");
	}


#ifdef _DEBUG
	system("pause");
#endif
	return 0;
}
