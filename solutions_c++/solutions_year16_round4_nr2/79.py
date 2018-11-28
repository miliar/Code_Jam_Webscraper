#include <bits/stdc++.h>

using namespace std;

int T, C=1;

int n, k;
long double P[256], v[256];
bool tem[256][256];
long double PD[256][256];

long double calc(int u, int votos) {
    if (votos < 0) return 0.0;
    if (u==k) {
        if (votos==0)
            return 1.0;
        return 0.0;
    }
    if (tem[u][votos])
        return PD[u][votos];

    long double soma=0.0;
    soma += v[u]*calc(u+1, votos-1);
    soma += (1.0-v[u])*calc(u+1, votos);

    tem[u][votos] = true;
    return PD[u][votos] = soma;
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);

        scanf("%d %d",&n,&k);
        for (int i=0;i<n;i++)
            scanf("%Lf",P+i);
        sort(P,P+n);

        long double maior = 0.0;
        for (int qts=0;qts<=k;qts++) {
            int tt=0;
            for (int i=0;i<qts;i++)
                v[tt++] = P[i];
            for (int i=0;i<k-qts;i++)
                v[tt++] = P[n-1-i];
            // tt == k
            memset(tem,false,sizeof(tem));
            long double r = calc(0, k/2);
            if (r > maior)
                maior = r;
        }
        printf("%.12Lf\n",maior);
    }

    return 0;
}
