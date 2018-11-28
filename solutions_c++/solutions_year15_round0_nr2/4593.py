// Just want to sleep...
#include <bits/stdc++.h>

using namespace std;
const int MAXN = 10000;
const int INF = 10000000;

int t, n;
int plates[MAXN + 5];

int main() {
    scanf("%d", &t);
    for(int tt = 1; tt <= t; ++tt) {
        scanf("%d", &n);
        for(int i = 0; i < n; ++i) {
            scanf("%d", &plates[i]);
        }
        int best = INF;
        for(int sp = 0; sp < 10; ++sp) {
            for(int f = 0; f < 90000; ++f) {
                int tsp = sp;
                vector <int> pl;
                for(int i = 0; i < n; ++i) pl.push_back(plates[i]);
                while(tsp-- > 0) {
                    sort(pl.begin(), pl.end());
                    int a;
                    if(pl[pl.size() - 1] < 9) {
                        a = pl[pl.size() - 1] / 2;
                    }
                    if(pl[pl.size() - 1] == 9) {
                        if(rand() % 2 == 0) a = 6;
                        else a = 5;
                    }
                    pl[pl.size() - 1] -= a;
                    pl.push_back(a);
                }
                sort(pl.begin(), pl.end());
                int act_res = pl[pl.size() - 1] + sp;
                best = min(best, act_res);
            }
        }
        printf("Case #%d: %d\n", tt, best);
    }
    return 0;
}
