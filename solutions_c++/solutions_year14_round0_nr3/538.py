#include <iostream>
#include <cstdio>

using namespace std;


int T, R, C, M;
int A[51][51];

void print() {
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            if (A[i][j] == 1) printf("*");
            if (A[i][j] == 0) printf(".");
            if (A[i][j] == -1) printf("c");
        }
        printf("\n");
    }
}

bool fillinA(int r, int c, int m) {
    int x = min(r, c);
    if (m >= x) {
        if (x == r) {
            for (int i = 1; i <= r; i++) A[i][c] = 1;
            return fillinA(r, c - 1, m - r);

        }
        if (x == c) {
            for (int i = 1; i <= c; i++) A[r][i] = 1;
            return fillinA(r - 1, c, m - c);
        }
    }
    if (r <= 3 && c <= 3 && m >= x - 1) return false;
    for (int i = 0; i < m; i++) {
            A[r][c - i] = 1;
    }
    A[1][1] = -1;
    if (m == c - 1) {
        A[r][2] = 0;
        A[r - 1][c] = 1;
    }

    return true;
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        scanf("%d %d %d", &R, &C, &M);
        printf("Case #%d:\n", i);
        if (M == 0) {
            for (int i = 1; i <= R; i++) {
                for (int j = 1; j <= C; j++) {
                    A[i][j] = 0;
                }
            }
            A[1][1] = -1;
            print();
        }
        else if (M == R * C - 1) {
            for (int i = 1; i <= R; i++) {
                for (int j = 1; j <= C; j++) {
                    A[i][j] = 1;
                }
            }
            A[1][1] = -1;
            print();
        }
        else if (R == 1) {
            if (C - M < 2) printf("Impossible\n");
            else
            {
                 printf("c");
                 for (int j = 1; j < C - M; ++j) printf(".");
                 for (int j = 1; j <= M; ++j) printf("*");
                 printf("\n");
            }
        }
        else if (C == 1) {
            if (R - M < 2) printf("Impossible\n");
            else
            {
                 printf("c\n");
                 for (int j = 1; j < R - M; ++j) printf(".\n");
                 for (int j = 1; j <= M; ++j) printf("*\n");
            }
        }
        else if (R == 2) {
            if (M % 2 == 1 || 2 * C - M < 4) printf("Impossible\n");
            else {
                printf("c");
                for (int j = 1; j < C - M/2; ++j) printf(".");
                for (int j = 1; j <= M/2; ++j) printf("*");
                printf("\n");
                for (int j = 1; j <= C - M/2; ++j) printf(".");
                for (int j = 1; j <= M/2; ++j) printf("*");
                printf("\n");

            }
        }
        else if (C == 2) {
            if (M % 2 == 1 || 2 * R - M < 4) printf("Impossible\n");
            else {
                printf("c.\n");
                for (int j = 1; j < R - M/2; ++j) printf("..\n");
                for (int j = 1; j <= M/2; ++j) printf("**\n");
            }
        }
        else {
            for (int s = 0; s < 51; s++)
                for (int k = 0; k < 51; k++) A[k][s] = 0;
            bool x = fillinA(R, C, M);
            if (!x) printf("Impossible\n");
            else print();

        }

    }
}
