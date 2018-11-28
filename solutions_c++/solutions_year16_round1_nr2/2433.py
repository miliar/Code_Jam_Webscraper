#include <cstdio>
#include <cstdlib>

struct Line{
    int num[50];
};

int compLine(const void *a, const void *b){
    return ( ((Line*)a)->num[0] - ((Line*)b)->num[0] );
}

bool checkR(int idx, int n, int* a, bool* v, int m[50][50]){
    for(int i=0;i<n;i++)
        if( v[i] && a[i] != m[idx][i] )
            return false;
    return true;
}

bool checkC(int idx, int n, int* a, bool* v, int m[50][50]){
    for(int i=0;i<n;i++)
        if( v[i] && a[i] != m[i][idx] )
            return false;
    return true;
}

bool solve(int idx, int N, Line* line, bool* r, bool* c, int m[50][50]){
    if( idx == 2*N-1 )
        return true;

    for(int i=0;i<N;i++){
        if( !r[i] ){
            if( checkR(i, N, line[idx].num, c, m) ){
                r[i] = true;
                for(int j=0;j<N;j++)
                    m[i][j] = line[idx].num[j];
                if( solve(idx+1, N, line, r, c, m) )
                    return true;
                r[i] = false;
            }
        }
        if( m[i][0] >= line[idx].num[0] )
            break;
    }

    for(int i=1;i<N;i++){
        if( !c[i] ){
            if( checkC(i, N, line[idx].num, r, m) ){
                c[i] = true;
                for(int j=0;j<N;j++)
                    m[j][i] = line[idx].num[j];
                if( solve(idx+1, N, line, r, c, m) )
                    return true;
                c[i] = false;
            }
        }
        if( m[0][i] >= line[idx].num[0] )
            break;
    }

    return false;
}

int main(){
    int T, N;
    Line L[100];
    int Mat[50][50];
    bool rows[50];
    bool cols[50];

    scanf("%d", &T);
    for(int caso=1;caso<=T;caso++){
        scanf("%d", &N);
        for(int i=0;i<2*N-1;i++)
            for(int j=0;j<N;j++)
                scanf("%d", &L[i].num[j]);
        qsort(L, 2*N-1, sizeof(Line), compLine);

        for(int i=0;i<N;i++){
            rows[i] = cols[i] = false;
            Mat[i][0] = L[0].num[i];
        }
        cols[0] = true;

        if( !solve(1, N, L, rows, cols, Mat) )
            printf("ERROR\n");

        printf("Case #%d:", caso);
        for(int i=0;i<N;i++){
            if( !rows[i] ){
                for(int j=0;j<N;j++)
                    printf(" %d", Mat[i][j]);
                break;
            }
            if( !cols[i] ){
                for(int j=0;j<N;j++)
                    printf(" %d", Mat[j][i]);
                break;
            }
        }

        if( caso < T )
            printf("\n");
    }

    return 0;
}
