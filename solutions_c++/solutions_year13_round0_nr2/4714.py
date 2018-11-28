#include <cstdio>
#include <cstdlib>

int in[105][105];
int T;
int tt;
int N, M;
int CAN;
int v1, v2;

int main(){
    int i, j, k;

    freopen( "B-large.in", "r", stdin);
    freopen( "out.txt", "w", stdout);

    scanf("%d", &T);
    while( tt++ < T){
        CAN = true;

        scanf("%d %d", &N, &M);

        for( i = 0; i < N; i++)
            for( j = 0; j < M; j++)
                scanf("%d", &in[i][j]);

        for( i = 0; i < N && CAN; i++){
            for( j = 0; j < M && CAN; j++){
                v1 = v2 = 1;

                for( k = 0; k < N && v1; k++)
                    if( in[k][j] > in[i][j])v1 = 0;
                for( k = 0; k < M && v2; k++)
                    if( in[i][k] > in[i][j])v2 = 0;

                if( !v1 && !v2)CAN = false;
            }
        }

        printf("Case #%d: ", tt);

        if( CAN)printf("YES\n");
        else printf("NO\n");
    }
}
