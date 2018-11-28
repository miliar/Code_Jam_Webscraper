#include <cstdio>
#include <cstring>

int mat[55][55];

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int totalCase;
    scanf("%d", &totalCase);
    for(int T = 1; T <= totalCase; ++T){
        memset(mat, 0, sizeof(mat));
        int B;
        long long M, chk = 1;
        scanf("%d%lld", &B, &M);
        for(int i = 1; i < B-1; ++i)
            chk*=2;
        printf("Case #%d: ", T);
        if(M > chk){
            printf("IMPOSSIBLE\n");
            continue;
        }
        M--;
        mat[1][B] = 1;
        for(int i = 2; i < B; ++i){
            for(int j = i+1; j <= B; ++j){
                mat[i][j] = 1;
            }
        }
        int idx = B-1;
        for(long long i = 1; i <= M; i*=2, --idx){
            if(M&i)
                mat[1][idx] = true;
        }
        printf("POSSIBLE\n");
        for(int i = 1; i <= B; ++i){
            for(int j = 1; j <= B; ++j)
                printf("%d", mat[i][j]);
            printf("\n");
        }
    }
    return 0;
}
/*
3
5 4
2 1
4 20
*/
