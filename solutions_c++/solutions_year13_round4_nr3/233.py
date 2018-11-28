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

const int maxn = 2001;
const int maxm = 40000001;

struct edge {
    int t;
    edge *next;
}*V[maxn], E[maxn*maxn];

int d[maxn], eh;

void addedge(int a, int b) {
    E[++eh].next = V[b]; V[b] = E+eh; V[b]->t = a; d[a]++;
    //printf("%d,%d\n", a, b);
}

int n;
int a[maxn];
int b[maxn];

void init() {
    scanf("%d",&n);
    FOR(i, n) {
        scanf("%d", &a[i]);
    }
    FOR(i, n) {
        scanf("%d", &b[i]);
    }
    CC(d, 0);
    CC(V, 0);
    eh=0;

    FOR(i, n) {
        bool da = false;
        FORD(j, i-1) {
            if (a[i] == a[j]+1 && !da) addedge(i, j), da=true;
            if (a[i] == a[j]) addedge(j, i);
        }
    }

    FORD(i, n) {
        bool da = false;
        for(int j=i+1; j<=n; j++) {
            if (b[i] == b[j]+1 && !da) addedge(i, j), da=true;
            if (b[i] == b[j]) addedge(j, i);
        }
    }
}

set <int> s;

int ans[maxn];
void solve() {
    FOR(i, n) if (d[i]==0) {
        s.insert(i);
    }
    int cur = 1;
    while (!s.empty()) {
        int u = *s.begin();
        ans[u] = cur++;
        s.erase(s.begin());
        for (edge *e = V[u]; e; e=e->next) {
            int v = e->t;
            d[v]--;
            if (d[v] == 0) {
                s.insert(v);
            }
        }
    }

    FOR(i, n) {
        if (i!=n) printf("%d ", ans[i]);
        else printf("%d", ans[i]);
    }
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
        init();
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
	return 0;
}
