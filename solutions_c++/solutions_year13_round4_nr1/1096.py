#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

#define MAXN 1100000
#define MAXE 110

struct People{
    int s, e, p;
}peo[MAXN];
int n, m;

int cmp(struct People a, struct People b){
    return a.p < b.p;
}

int main(){
    int i, j, k, cas, T;
    int cost1, cost2;
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas++){
        scanf("%d%d", &n, &m);
        for (i = 0; i < m; i++)
            scanf("%d%d%d", &peo[i].s, &peo[i].e, &peo[i].p);
        cost1 = 0;
        for (i = 0; i < m; i++){
            k = peo[i].e - peo[i].s;
            cost1 += peo[i].p * (n * k - (k - 1) * k / 2);
            if (peo[i].s == peo[i].e) peo[i].p = 0;
        }
        sort(peo, peo + m, cmp);

        cost2 = 0;
        for (i = 0; i < m;){
            if (peo[i].p == 0){
                continue;
                i++;
            }
            for (j = i + 1; j < m; j++){
                if (peo[j].p > 0 && peo[j].s > peo[i].s && peo[j].s <= peo[i].e &&
                    peo[j].e > peo[i].e){
                    if (peo[j].p == peo[i].p){
                        swap(peo[j].s, peo[i].s);
                    }else{
                        peo[m].s = peo[j].s;
                        peo[m].e = peo[i].e;
                        peo[m].p = peo[i].p;
                        peo[i].e = peo[j].e;
                        peo[j].p -= peo[i].p;
                        m++;
                    }
                    break;
                }else if (peo[j].p > 0 && peo[j].e >= peo[i].s && peo[j].e < peo[i].e &&
                    peo[j].s < peo[i].s){
                    if (peo[j].p == peo[i].p){
                        swap(peo[j].s, peo[i].s);
                    }else{
                        peo[m].s = peo[i].s;
                        peo[m].e = peo[j].e;
                        peo[m].p = peo[i].p;
                        peo[i].s = peo[j].s;
                        peo[j].p -= peo[i].p;
                        m++;
                    }
                    break;
                }
            }
            if (j == m) i++;
            else sort(peo + i, peo + m, cmp);
        }
        cost2 = 0;
        for (i = 0; i < m; i++){
            k = peo[i].e - peo[i].s;
            cost2 += peo[i].p * (n * k - (k - 1) * k / 2);
//			printf("%d %d %d\n", peo[i].s, peo[i].e, peo[i].p);
        }
        printf("Case #%d: %d\n", cas, cost1 - cost2);
    }
    return 0;
}
