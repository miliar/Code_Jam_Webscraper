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

int n, m;

int a[10001];

void solve() {
    scanf("%d%d", &n, &m);
    REP(i, n) scanf("%d", &a[i]);
    sort(a, a+n);
    int j = n - 1;
    int i = 0;
    int res = 0;
    while (true) {
        while (i<j && a[i] + a[j] > m) res++, j--;
        if (i<j && a[i] + a[j] <= m) res++, j--, i++;
        if (i == j) {res++; break;}
        if (i > j) break;
    }
    printf("%d", res);
}

typedef long long LL;
int main()
{
#ifdef DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    int T;
    scanf("%d",&T);
    FOR(i, T) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
	return 0;
}
