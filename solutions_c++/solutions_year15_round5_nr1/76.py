#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;
const int N = 1e6+3;
int tmin[N], tmax[N];
int T, n, D, s[N], m[N], as, cs, rs, am, cm, rm;
bool vis[N];
vector<int> mins[N], maxs[N];
void process(int a) {
    if (vis[a]) return;
    if (!vis[m[a]]) process(m[a]);
    tmin[a] = min(s[a], tmin[m[a]]);
    tmax[a] = max(s[a], tmax[m[a]]);
    vis[a] = true;
}
int main() {
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d%d", &n,&D);
        scanf("%d%d%d%d", &s[0],&as,&cs,&rs);
        scanf("%d%d%d%d", &m[0],&am,&cm,&rm);
        for (int i=1; i<n; i++) {
            s[i] = (s[i-1]*(long long)as + cs) % rs;
            m[i] = (m[i-1]*(long long)am + cm) % rm;
        }
        for (int i=1; i<n; i++) m[i] %= i;
        bool ins[n];
        for (int i=0; i<n; i++) vis[i] = ins[i] = false;
        tmin[0] = tmax[0] = s[0];
        vis[0] = true;
        ins[0] = true;
        int ans = 1;
        int beg = max(0, s[0]-D), end = min(rs, s[0]);
        for (int i=1; i<n; i++) {
            process(i);
            if (tmin[i] >= beg) mins[tmin[i]].push_back(i);
            if (tmax[i] <= end+D) maxs[tmax[i]].push_back(i);
            if (tmin[i] >= beg && tmax[i] <= beg+D) {
                ins[i] = true;
                ans++;
            }
        }
        int res = ans;
        for (int i=beg; i<end; i++) {
            for (int x: mins[i]) {
                if (ins[x]) {
                    ins[x] = false;
                    ans--;
                }
            }
            if (i+D+1 < rs) {
                for (int x: maxs[i+D+1]) {
                    if (tmin[x] > i) {
                        ins[x] = true;
                        ans++;
                    }
                }
           }
            res = max(res, ans);
        }
        printf("Case #%d: %d\n", t, res);
        for (int i=1; i<n; i++) {
            mins[tmin[i]].clear();
            maxs[tmax[i]].clear();
        }
    }
    return 0;
}
