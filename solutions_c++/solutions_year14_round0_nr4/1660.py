#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <utility>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define F first
#define S second
#define PB push_back
#define MP make_pair

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int INF = 2123123123;
const int MOD = 1e9+7;

typedef long long ll;
typedef pair<int,int> pii;

#define ALL(c) (c).begin(), (c).end()
#define SZ(a) (int)(a).size()
#define RESET(a,x) memset(a,x,sizeof(a))
#define FORIT(it,v) for(__typeof(v.begin()) it = v.begin(); it != v.end(); ++it)
#define MX(a,b) a = max((a),(b));
#define MN(a,b) a = min((a),(b));

inline void OPEN(const string &s) {
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

#define MAXN 1000

int n, ntc, anita, carol;
int vis[MAXN+5], used[MAXN+5];
double naomi[MAXN+5], ken[MAXN+5];

int main() {
    OPEN("D");
    scanf("%d", &ntc);
    for (int itc = 0; itc < ntc; itc++) {
        RESET(vis,0); RESET(used,0);
        scanf("%d", &n);
        printf("Case #%d: ", itc+1);
        for (int i = 0; i < n; i++) scanf("%lf", &naomi[i]);
        for (int i = 0; i < n; i++) scanf("%lf", &ken[i]);
        sort(naomi,naomi+n); sort(ken,ken+n); 
        int last = 0; anita = 0; carol = 0;
        for (int i = 0; i < n; i++) {
            int take = 0;
            for (int j = 0; j < n; j++) 
                if (naomi[i] > ken[j] && !vis[j]) { 
                    take = vis[j] = 1; break;
            }
            if (take) ++anita;
            while (last < n && (ken[last] < naomi[i] || used[last])) ++last;
            used[last] = 1;
            if (last == n) ++carol;
        }
        printf("%d %d\n", anita, carol);
    }
    return 0;
}
