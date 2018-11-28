#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,n) for(int i=1;i<=(n);i++)
#define FORD(i,n) for(int i=(n);i>=1;i--)

#define SZ(x) ((int)x.size())
#define CC(a,x) memset(a,x,sizeof(a))
#define TWO(x) ((LL)1<<(x))

#define DEBUG

using namespace std;

double solve() {
    double C, F, X;
    scanf("%lf%lf%lf", &C, &F, &X);
    double cur = 2;
    double res = X / cur;
    double tim = 0;
    for(;;) {
        tim += C / cur;
        cur += F;
        if (tim + X / cur > res) break;
        res = tim + X / cur;
    }
    return res;
}

typedef long long LL;
int main()
{
#ifdef DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    int T;
    scanf("%d", &T);
    FOR(i, T) {
        printf("Case #%d: %.7lf\n", i, solve());
    }
	return 0;
}
