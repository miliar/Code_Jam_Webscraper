#include <cstdio>
#include <cstring>

int main() {
    int testc;
    std::scanf("%d", &testc);
    int ***input = new int** [testc];
    int *rows = new int[testc];
    int *cols = new int[testc];
    for (int k = 0; k < testc; k++) {
        int m, n;
        std::scanf("%d%d", &m, &n);
        rows[k] = m;
        cols[k] = n;
        input[k] = new int* [m];
        for (int i = 0; i < m; i++)
            input[k][i] = new int[n];

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                std::scanf("%d", input[k][i] + j);
    }

    bool *output = new bool[testc];
    #pragma omp parallel for schedule(dynamic)
    for (int test = 0; test < testc; test++) {
        int **board = input[test];
        int m = rows[test];
        int n = cols[test];

        int *maxrow = new int[m];
        int *maxcol = new int[n];

        std::memset(maxrow, 0, m*sizeof(int));
        std::memset(maxcol, 0, n*sizeof(int));

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (board[i][j] > maxrow[i])
                    maxrow[i] = board[i][j];
                if (board[i][j] > maxcol[j])
                    maxcol[j] = board[i][j];
            }

        output[test] = true;
        for (int i = 0; i < m && output[test]; i++)
            for (int j = 0; j < n && output[test]; j++)
                if (board[i][j] < maxrow[i] && board[i][j] < maxcol[j])
                    output[test] = false;
    
        delete [] maxrow;
        delete [] maxcol;
    }

    for (int test = 0; test < testc; test++)
        std::printf("Case #%d: %s\n", test+1, (output[test] ? "YES" : "NO"));

    delete [] input;
    delete [] rows;
    delete [] cols;
    delete [] output;

    return 0;
}
