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



int main(int argc, char** argv)
{
	int tc;
	scanf("%d", &tc);
	FOR(tccc,1,tc) {
		double c,f,x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double r = 2, t = 0;
		double bt = x/r;
		while (1) {
			double nt = t + c/r;
			double nr = r + f;
			if (nt + x/nr < bt) {
				bt = nt + x/nr;
				t = nt;
				r = nr;
			}
			else break;
		}
		printf("Case #%d: %.7lf\n", tccc, bt);
	}

#ifdef _DEBUG
	system("pause");
#endif
	return 0;
}
