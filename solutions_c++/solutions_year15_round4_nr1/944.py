#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

int dx[] = {0, 0, -1, 1};
int dy[] = {1,-1, 0, 0};

char M[128][128];
int T, C=1, n, m;
map<char,int> dir;

bool vaipraborda(int i, int j, int k) {
    int ni, nj;
    ni = i + dx[k];
    nj = j + dy[k];
    while (0 <= ni and ni < n and 0 <= nj and nj < m and M[ni][nj] == '.') {
        ni += dx[k];
        nj += dy[k];
    }

    if (0 <= ni and ni < n and 0 <= nj and nj < m)
        return false;

    return true;
}

int main() {
    dir['^'] = 2;
    dir['<'] = 1;
    dir['v'] = 3;
    dir['>'] = 0;

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d %d",&n,&m);
        for (int i=0;i<n;i++)
            scanf("%s",M[i]);
        int resp = 0;
        bool da = true;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++) if (M[i][j] != '.') {
                int k = dir[M[i][j]];
                if (!vaipraborda(i,j,k))
                    continue;

                // eh borda. troca
                resp++;

                // da pra trocar?
                bool troca=false;
                for (int kk=0;kk<4;kk++) if (kk != k)
                    if (!vaipraborda(i,j,kk)) {
                        troca=true;
                        break;
                    }
                if (!troca) {
                    da=false;
                    goto resp;
                }
            }

        resp:;
        if (!da)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",resp);


    }

    return 0;
}
