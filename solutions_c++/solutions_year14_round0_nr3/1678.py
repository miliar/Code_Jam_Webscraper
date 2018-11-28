#include <cstdio>
#include <cstring>

using namespace std;

// warning: apenas para small! XXX

int dx[] = {-1,-1,-1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1,-1, 1,-1, 0, 1};
int T, C=1, visitados, qropontos, n, m, minas, respi, respj;
char M[32][32];
int numero[32][32];

void dfs(int i, int j) {
    visitados++;
    int conta=0;
    for (int k=0;k<8;k++) {
        int ni = i+dx[k];
        int nj = j+dy[k];
        if (!(0 <= ni and ni < n and 0 <= nj and nj < m)) continue;
        if (M[ni][nj]=='*') {
            conta++;
            break;
        }
    }
    numero[i][j] = conta;
    if (conta == 0) {
        for (int k=0;k<8;k++) {
            int ni = i+dx[k];
            int nj = j+dy[k];
            if (!(0 <= ni and ni < n and 0 <= nj and nj < m)) continue;
            if (numero[ni][nj]==-1)
                dfs(ni,nj);
        }
    }
}

bool go(int u, int pontos, int ultini, int ultfim, bool aberto) {
     if (u==n) {
         if (pontos > 0) return false;
         for (respi=0;respi<n;respi++)
         for (respj=0;respj<m;respj++) if (M[respi][respj]=='.') {
             memset(numero,0xff,sizeof(numero));
             visitados=0;
             dfs(respi,respj);
             if (visitados == qropontos)
                 return true;
         }
         return false;
     }

     // continua fechado ou fecha
     if (!aberto or pontos==0) {
        for (int j=0;j<m;j++) M[u][j] = '*';
        if (go(u+1,pontos,ultini,ultfim,false)) return true;
     }

     // abre
     if (pontos > 0)
     for (int ini=0;ini<m;ini++) if (ini <= ultfim or !aberto)
         for (int fim=ini;fim<m;fim++) if (fim >= ultini or !aberto) {
             if (fim-ini+1 > pontos) continue;
             // preenche
             for (int j=0;j<ini;j++) M[u][j] = '*';
             for (int j=ini;j<=fim;j++) M[u][j] = '.';
             for (int j=fim+1;j<m;j++) M[u][j] = '*';
             if (go(u+1,pontos-(fim-ini+1), ini, fim, true))
                 return true;
         }

     // fecha
     return false;
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d:\n",C++);
        scanf("%d %d %d",&n,&m,&minas);
        qropontos = n*m - minas;
        if (go(0,n*m - minas,0,m-1,false)) {
            for (int i=0;i<n;i++) {
                for (int j=0;j<m;j++)
                    if (i==respi and j==respj)
                        printf("c");
                    else
                        printf("%c",M[i][j]);
                printf("\n");
            }
        } else
            printf("Impossible\n");
    }

    return 0;
}
