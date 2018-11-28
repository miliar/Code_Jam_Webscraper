#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>

using namespace std;

#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<pii>    vpii;
typedef vector<int>    vi;
typedef long long ll;

#define MAXN 1000500

int s[MAXN];
int m[MAXN];
int p[MAXN];
int n, d;
int as, cs, rs, s0;
int am, cm, rm, m0;

int l, r;
vi g[MAXN];
int cnt, best;

vpii q;

void rec(int v, int l, int r) {
    int l1, r1;

    //printf("node: %i s=%i  l=%i r=%i\n", v, s[v], l, r);

    if (s[v] < s0) {
        if (s0 - s[v] > d) return;
        l1 = s0 - d;
        r1 = s[v];
    } else {
        if (s[v] - s0 > d) return;
        l1 = s[v] - d;
        r1 = s0;
    }

        l = max(l, l1);
        r = min(r, r1);
        if (l > r) return;

        q.pb( mp(l, 0) );
        q.pb( mp(r, 1) );

    //printf("node %i  :  l=%i  r=%i\n", v, l, r);
    for(int i=0; i<g[v].size(); ++i) rec(g[v][i], l, r);
  
}

int main() {
    int tc;
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        fprintf(stderr, "test %i\n", tt);
        printf("Case #%i: ", tt);

        //printf("\n");
        scanf("%i%i", &n, &d);
        scanf("%i%i%i%i", &s0, &as, &cs, &rs);
        scanf("%i%i%i%i", &m0, &am, &cm, &rm);

        for(int i=0; i<=n; ++i) g[i].clear();

        //printf("---%i\n", rs);

        s[0] = s0;
        m[0] = m0;

        for(int i=1; i<n; ++i) {
            s[i] = ((ll)s[i-1]*(ll)as + cs) % rs;
            m[i] = ((ll)m[i-1]*(ll)am + cm) % rm;
            p[i] = m[i] % i;
            g[p[i]].pb(i);

            //printf("%i: %i %i\n", i, s[i], m[i] % i);
        }

        q.clear();
        for(int i=0; i<g[0].size(); ++i) rec(g[0][i], s0 - d, s0);

        sort(q.begin(), q.end());
        best = 1;
        cnt = 1;
        for(int i=0; i<q.size(); ++i) {
            if (q[i].second == 0) cnt++; else cnt--;
            best = max(best, cnt);            
        }
        printf("%i\n", best);
    }
}