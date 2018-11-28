#include <cstdio>

int T, N, M, actual[110][110], target[110][110];

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a < b ? a : b;
}

int max_in_row(int row) {
    int mx = -1;
    for (int j=0 ; j<M ; j++)
        mx = max(mx, target[row][j]);

    return mx;
}

int max_in_column(int column) {
    int mx = -1;
    for (int i=0 ; i<N ; i++)
        mx = max(mx, target[i][column]);

    return mx;
}

void init() {
    for (int i=0 ; i<N ; i++)
        for (int j=0 ; j<M ; j++)
            actual[i][j] = 100;
}

bool good() {
    for (int i=0 ; i<N ; i++)
        for (int j=0 ; j<M ; j++)
            if (actual[i][j] != target[i][j])
                return false;

    return true;
}

void pactual() {
    for (int i=0 ; i<N ; i++) {
        for (int j=0 ; j<M ; j++)
            printf("%d ", actual[i][j]);
        printf("\n");
    }
    printf("\n");
}

void ptarget() {
    for (int i=0 ; i<N ; i++) {
        for (int j=0 ; j<M ; j++)
            printf("%d ", target[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    scanf("%d", &T);
    for (int c=1 ; c<=T ; c++) {
        printf("Case #%d: ", c);
        scanf("%d %d", &N, &M);
        init();
        for (int i=0 ; i<N ; i++) {
            for (int j=0 ; j<M ; j++) {
                scanf("%d", &target[i][j]);
            }
        }

        for (int i=0 ; i<N ; i++) {
            int mx_row = max_in_row(i);
            for (int j=0 ; j<M ; j++)
                actual[i][j] = min(mx_row, actual[i][j]);

        }

        for (int j=0 ; j<M ; j++) {
            int mx_col = max_in_column(j);
            for (int i=0 ; i<N ; i++)
                actual[i][j] = min(mx_col, actual[i][j]);
        }

        printf(good() ? "YES\n" : "NO\n");
    }
}