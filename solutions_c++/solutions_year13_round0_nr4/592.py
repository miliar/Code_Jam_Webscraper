#include <cstdio>
#include <cstring>

using namespace std;

int T, C=1, n, m;
int fechadura[256], tenho[256];
int chave[256][256], qnts[256];
int v[256], k;
bool PD[(1<<20)+2];
int tem[(1<<20)+2], TT;
int filho[(1<<20)+2];

bool da(int aberto) {
    if (aberto==((1<<n)-1)) return true;
    if (tem[aberto]==TT) return PD[aberto];
    int te[256];
    memcpy(te,tenho,sizeof(tenho));

    for (int i=0;i<n;i++) if (aberto&(1<<i)) {
        te[fechadura[i]]--;
        for (int j=0;j<qnts[i];j++)
            te[chave[i][j]]++;
    }

    for (int i=0;i<n;i++) if (!(aberto&(1<<i)) and te[fechadura[i]])
        if (da(aberto^(1<<i))) {
            tem[aberto]=TT;
            filho[aberto]=i;
            return PD[aberto] = true;
        }
    tem[aberto]=TT;
    return PD[aberto] = false;
}

int main() {
    memset(tem,0,sizeof(tem));
    TT=0;

    for(scanf("%d",&T);T--;) {
        TT++;
        printf("Case #%d:",C++);
        scanf("%d %d",&k,&n);
        memset(tenho,0,sizeof(tenho));
        for (int i=0;i<k;i++) {
            int t;
            scanf("%d",&t);
            tenho[t]++;
        }
        for (int i=0;i<n;i++) {
            scanf("%d",fechadura+i);
            scanf("%d",qnts+i);
            for (int j=0;j<qnts[i];j++)
                scanf("%d",&chave[i][j]);
        }
        if (da(0)) {
            int u = 0;
            while (u != (1<<n)-1) {
                printf(" %d",filho[u]+1);
                u = u^(1<<filho[u]);
            }
            printf("\n");
        } else
            printf(" IMPOSSIBLE\n");
    }

    return 0;
}
