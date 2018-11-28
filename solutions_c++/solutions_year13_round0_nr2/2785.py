#include <cstdio>
#include <cstring>
#define N 15
int main() {
    int t, n, m, sw, mapa[N][N], fila[N], col[N];
    scanf("%d", &t);
    for( int casos=1 ; casos<=t ; casos++ ) {
        scanf("%d %d", &n, &m);
        memset(fila,0,sizeof(fila));
        memset(col,0,sizeof(col));
        for( int i=0 ; i<n ; i++ )
            for( int k=0 ; k<m ; k++ ) {
                scanf("%d", &mapa[i][k]);
                fila[i] += mapa[i][k];
                col[k] += mapa[i][k];
            }
        sw = 1;
        for( int i=0 ; i<n ; i++ ) 
            for( int k=0 ; k<m ; k++ )
                if( mapa[i][k] == 1 )
                    if( fila[i] != m && col[k] != n ) sw = 0;
        printf("Case #%d: ", casos);
        if( sw ) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
