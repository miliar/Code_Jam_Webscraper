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

char s[102][102];
int h[102];
int cur[102];
int n;

int solve() {
    CC(h, 0);
    int ans = 0;
    while (true) {
        char c = s[0][h[0]];
        if (c == '\0') {
            REP(i, n) if (s[i][h[i]] != '\0') return -1;
            break;
        }
        CC(cur, 0);
        REP(i, n) {
            while(c==s[i][h[i]]) cur[i]++, h[i]++;
            if (cur[i] == 0) return -1;
        }
        sort(cur, cur+n);
        REP(i, n) ans += abs(cur[i] - cur[n/2]);
    }
    return ans;
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
        scanf("%d", &n);
        REP(j, n) scanf("%s", s[j]);
        int res = solve();
        if (res != -1)
            printf("Case #%d: %d\n",i, res);
        else
            printf("Case #%d: Fegla Won\n",i);
    }
	return 0;
}
