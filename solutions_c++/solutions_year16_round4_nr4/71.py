#include <bits/stdc++.h>

using namespace std;

int T, C=1;
int n, ordem[32], resp;
bool maquina[32];
int sabe[32][32], orig[32][32];
char s[32];

bool fode(int u) {
    if (u==n) {
        for (int i=0;i<n;i++)
            if (!maquina[i])
                return true;
        return false;
    }
    bool entra=false;
    for (int i=0;i<n;i++)
        if (!maquina[i] and sabe[ordem[u]][i]) {
            entra=true;
            maquina[i] = true;
            if (fode(u+1)) return true;
            maquina[i] = false;
        }
    return !entra;
}

bool ok() {
    // pra cada ordem de chegada
    for (int i=0;i<n;i++) ordem[i] = i;
    do {
        // existe alguma associacao de maquina que fodei?
        memset(maquina,false,sizeof(maquina));
        if (fode(0)) return false;
    } while (next_permutation(ordem,ordem+n));
    return true;
}

void vai(int i, int j, int gasto) {
    if (i==n) {
        if (ok())
            resp = min(resp, gasto);
        return;
    }
    if (j==n) {
        vai(i+1,0,gasto);
        return;
    }
    if (orig[i][j]==1) {
        sabe[i][j] = 1;
        vai(i,j+1,gasto);
    } else {
        sabe[i][j] = 0;
        vai(i,j+1,gasto);
        sabe[i][j] = 1;
        vai(i,j+1,gasto+1);
    }
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d",&n);
        for (int i=0;i<n;i++) {
            scanf("%s",s);
            for (int j=0;j<n;j++)
                orig[i][j] = s[j]-'0';
        }

        resp = 0x3f3f3f3f;
        vai(0, 0, 0);
        printf("%d\n",resp);
    }

    return 0;
}
