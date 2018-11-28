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

typedef long long LL;

int a[5][5], b[5][5];
int an, bn;

void solve() {
    scanf("%d", &an);
    FOR(i, 4) FOR(j, 4) scanf("%d", &a[i][j]);
    scanf("%d", &bn);
    FOR(i, 4) FOR(j, 4) scanf("%d", &b[i][j]);

    int ans = 0;
    FOR(ja, 4) FOR(jb, 4) {
        if (a[an][ja] == b[bn][jb]) {
            if (ans == 0) ans = a[an][ja];
            else ans = -1;
        }
    }

    if (ans == 0) printf("Volunteer cheated!");
    else if (ans == -1) printf("Bad magician!");
    else printf("%d", ans);
}

int main()
{
#ifdef DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    int T;
    scanf("%d", &T);
    FOR(i, T) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
	return 0;
}

