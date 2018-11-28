#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define mt make_tuple
#define ll long long
#define pii pair<int,int>
#define tii tuple <int,int,int>
#define N 200005
#define mod 1000000005
#define X first
#define Y second
#define eps 0.0000000001
#define all(x) x.begin(),x.end()
#define tot(x) x+1,x+n+1
using namespace std;

int t, T, n, nn, j, k, sc, m, i, poz, cnt, a[120][55], x, soll[55][55];
vector<int>v, sol;
map<vector<int>, int>M, M1;
vector<vector<int>>w;
int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);

    for(t = 1; t <= T; t++) {
        w.clear();
        M.clear();
        sol.clear();
        printf("Case #%d: ", t);
        scanf("%d", &n);
        m = 2 * n;
        m--;
        nn = (1 << m);
        nn--;

        for(i = 0; i < m; i++) {
            v.clear();

            for(j = 0; j < n; j++) {
                scanf("%d", &a[i][j]);
                v.pb(a[i][j]);
            }

            M[v] ++;
            w.pb(v);
        }

        M1 = M;
        sort(all(w));

        for(i = 1; i <= nn; i++) {
            if(__builtin_popcount(i) != n)
                continue;

            M = M1;
            x = i;
            poz = 0;
            cnt = -1;

            while(x) {
                if(x % 2) {
                    ++cnt;

                    for(j = 0; j < n; j++)
                        soll[cnt][j] = w[poz][j];

                    M[w[poz]]--;
                }

                poz++;
                x /= 2;
            }

            sc = 0;

            for(j = 0; j < n; j++) {
                v.clear();

                for(k = 0; k < n; k++)
                    v.pb(soll[k][j]);

                if(!M[v]) {
                    sc++;
                    sol = v;
                }
                else
                    M[v]--;
            }

            if(sc == 1) {
                i = nn + 1;

                for(auto it : sol)
                    printf("%d ", it);
            }
        }

        printf("\n");
    }

    return 0;
}
