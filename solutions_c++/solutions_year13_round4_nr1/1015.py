#include <cstdio>
#include <cstring>

using namespace std;

#define MOD 1000002013

int N;

int O[1001];
int E[1001];
int P[1001];

/* TODO: coord compression for large dataset */
int geton[1001];
int getoff[1001];
int ontrain[1001];
int maxstop;

int c(int o, int e) {
    int n = e - o;
    return n*N - ((n * (n+1)) / 2) + n;
}

int main() {
    int T; scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int M;
        int fullcost = 0;

        scanf("%d", &N);
        scanf("%d", &M);

        memset(geton, 0, sizeof geton);
        memset(getoff, 0, sizeof getoff);
        memset(ontrain, 0, sizeof getoff);
        maxstop = 0;

        for (int j = 0; j < M; j++) {
            int o, e, p;
            scanf("%d %d %d", &o, &e, &p);
            getoff[e] += p;
            geton[o] += p;
            if (e > maxstop)
                maxstop = e;
            fullcost += (c(o, e) * p)%MOD;
            fullcost %= MOD;

            O[j] = o; E[j] = e; P[j] = p;
        }

        //printf("maxstop = %d\n", maxstop);

        ontrain[0] = 0;
        /* make every station be its net effect;
         * geton[j] = 0 or getoff[j] = 0 for every j
         */
        for (int j = 1; j <= maxstop; j++) {
            if (getoff[j] > geton[j]) {
                getoff[j] -= geton[j];
                geton[j] = 0;
            } else {
                geton[j] -= getoff[j];
                getoff[j] = 0;
            }
            ontrain[j] = ontrain[j-1] + geton[j] - getoff[j];
        }

        int mincost = 0;
        /* now handle passenger travels */
        for (int j = 1; j < maxstop; j++) {
            for (int k = j+1; k <= maxstop; k++) {
                if (ontrain[k] < geton[j]) {
                    int diff = geton[j] - ontrain[k];

                    //printf("%d passengers from %d to %d *\n", diff, j, k);
                    mincost += (c(j, k) * diff)%MOD;
                    mincost %= MOD;
                    getoff[k] -= diff;
                    geton[j] -= diff;
                    for (int l = j; l < k; l++)
                        ontrain[l] = ontrain[l-1] + geton[l] - getoff[l];
                }
            }

            for (int k = maxstop; geton[j] && k > j; k--) {
                if (getoff[k] == 0)
                    continue;
                int diff;
                if (getoff[k] > geton[j])
                    diff = getoff[k] - geton[j];
                else
                    diff = geton[j] - getoff[k];

                //printf("%d passengers from %d to %d\n", diff, j, k);
                mincost += (c(j, k) * diff)%MOD;
                mincost %= MOD;
                getoff[k] -= diff;
                geton[j] -= diff;
                for (int l = j; l < k; l++)
                    ontrain[l] = ontrain[l-1] + geton[l] - getoff[l];
            }
        }

        //printf("fullcost = %d; mincost = %d;\n", fullcost, mincost);

        printf("Case #%d: %d\n", i+1, fullcost-mincost);
    }
}
