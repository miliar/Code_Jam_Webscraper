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

int a[1002], r[1002];

void swap(int t1, int t2) {
    int tmp = a[t1];
    a[t1] = a[t2];
    a[t2] = tmp;
}

void solve() {
    scanf("%d", &n);
    FOR(i, n) scanf("%d", &a[i]);
    int l = 0, r = 0;
    int ans = 0;
    FOR(i, n) {
        int x = l + 1;
        for(int j = l + 1; j <= n - r; j++) {
            if (a[j] < a[x]) x = j;
        }
        if (x - l - 1 < n - r - x) {
            for (int j = x; j > l + 1; j--) {
                swap(j, j-1);
                ans++;
            }
            l++;
        } else {
            for (int j = x; j < n - r; j++) {
                swap(j, j+1);
                ans++;
            }
            r++;
        }
    }
    printf("%d", ans);
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
