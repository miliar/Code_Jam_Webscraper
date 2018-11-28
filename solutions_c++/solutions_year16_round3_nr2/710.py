#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>

#define INF 1000000007

using namespace std;

#define MAXN 51

int vis[MAXN];
unsigned long long pd[MAXN];
unsigned long long mat[MAXN][MAXN];
unsigned long long n, m;

unsigned long long busca(unsigned long long u) {
    unsigned long long &res=pd[u];
    if (vis[u]!=-1) {
        return res;
    }
    vis[u]=1;
    if (u==n) {
        return res=1;
    }
    res=0;
    unsigned long long v;
    for (v=1; v<=n; v++) {
        if (mat[u][v]==1) {
            res+=busca(v);
        }
    }
    return res;
}

int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    unsigned long long t;
    scanf("%llu", &t);
    unsigned long long caso;
    for (caso=1; caso<=t; caso++) {
        scanf("%llu %llu", &n, &m);
        memset(mat, 0, sizeof(mat));
        unsigned long long i, j;
        for (i=1; i<=n; i++) {
            memset(vis, -1, sizeof(vis));
            if (busca(1)<m) {
                for (j=i+1; j<=n; j++) {
                    mat[i][j]=1;
                }
            }
        }
        memset(vis, -1, sizeof(vis));
        unsigned long long val=busca(1);
//        printf("** %llu\n", val);
        while (true) {
            if (val==m) {
                break;
            }
            unsigned long long iEsc, jEsc;
            iEsc=INF;
            jEsc=INF;
            unsigned long long melhor=18446744073709551614LLU;
            for (i=1; i<=n; i++) {
                for (j=1; j<=n; j++) {
                    if (mat[i][j]==1) {
                        mat[i][j]=0;
                        memset(vis, -1, sizeof(vis));
                        unsigned long long aux=busca(1);
                        if (aux>=m && aux<melhor) {
                            melhor=aux;
                            iEsc=i;
                            jEsc=j;
                        }
                        mat[i][j]=1;
                    }
                }
            }
            if (iEsc==INF) {
                break;
            }
            mat[iEsc][jEsc]=0;
            val=melhor;
        }
        if (val==m) {
            printf("Case #%llu: POSSIBLE\n", caso);
            for (i=1; i<=n; i++) {
                for (j=1; j<=n; j++) {
                    printf("%llu", mat[i][j]);
                }
                printf("\n");
            }
        }
        else {
            printf("Case #%llu: IMPOSSIBLE\n", caso);
        }

    }
    return 0;
}






