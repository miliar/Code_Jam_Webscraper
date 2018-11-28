#include <iostream>
#include <ios>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <tuple>
#include <utility>
#include <string>
#include <cstring>

using namespace std;

#define N 25
bool skill[N][N];


struct gr {
    int nw;
    int ns;
    int c;
};
bool operator<(gr a, gr b) { return a.nw == b.nw ? a.ns<b.ns : a.nw<b.nw; }
bool operator==(gr a, gr b) { return a.nw == b.nw&&a.ns == b.ns; }


int r(gr* g, int ng, int ig, int wt, int st, int su = 0) {
    bool any = false;
    int tmin = 1 << 30;
    for (; ig < ng; ig++) {
        if (g[ig].c) any = true;
        for (int q = 1; q <= g[ig].c; q++) {
            int wt2 = wt + q * g[ig].nw;
            int st2 = st + q * g[ig].nw * g[ig].ns;
            int su2 = su + q * g[ig].ns;
            g[ig].c -= q;
            tmin = min(tmin, r(g, ng, ig, wt2, st2, su2));
            if(wt2 >= su2)
                tmin = min(tmin,
                    wt2*wt2 - st2 + r(g, ng, 0, 0, 0)
                    );
            g[ig].c += q;
        }
    }
    if (!any && !wt) return 0;
    return tmin;
}

int main()
{
    ios_base::sync_with_stdio(false);

    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int n; cin >> n;
        for (int i = 0; i<n; i++) {
            string s; cin >> s;
            for (int j = 0; j<n; j++)
                skill[i][j] = s[j] == '1';
        }

        int group[N], q[N], gc[N]{};
        int qs = 0, qe = 0;
        memset(group, -1, sizeof(group));
        int ng = 0;
        for (int i = 0; i<n; i++) {
            if (~group[i]) continue;
            q[qe++] = i;
            group[i] = ng;
            gc[ng] = 1;
            while (qs < qe) {
                int w = q[qs++];
                for (int b = 0; b<n; b++) {
                    for (int j = 0; j<n; j++) {
                        if (skill[w][j] && skill[b][j] && !~group[b]) {
                            group[b] = ng;
                            ++gc[ng];
                            q[qe++] = b;
                        }
                    }
                }
            }
            ++ng;
        }

        bool gskill[N][N]{};
        int ngskill[N]{};
        for (int i = 0; i<n; i++)
            for (int j = 0; j < n; j++) {
                if (skill[i][j] && !gskill[group[i]][j]) {
                    gskill[group[i]][j] = true;
                    ngskill[group[i]]++;
                }
            }
        int cost = 0;
        for (int i = 0; i<n; i++) {
            cost += ngskill[group[i]];
            //cost += ngskill[group[i]] - accumulate(skill[i], skill[i] + n, 0);
            for (int j = 0; j < n; j++)
                cost -= skill[i][j];
        }

        gr z[N];
        for (int i = 0; i<ng; i++) {
            z[i].nw = gc[i];
            z[i].ns = ngskill[i];
        }
        int ng2 = 0;
        for (int i = 0; i<ng; i++) {
            int k = 1;
            while (i<ng - 1 && z[i] == z[i + 1])
                i++, k++;
            z[ng2] = z[i];
            z[ng2].c = k;
            ng2++;
        }
        int ans = r(z, ng2, 0, 0, 0);

        printf("Case #%d: %d\n", t, cost + ans);
    }

    return 0;
}
