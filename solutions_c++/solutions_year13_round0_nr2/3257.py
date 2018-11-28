#include <cstdio>

int data[100][100];

bool readandanswer() {
    int rows, cols;

    scanf("%d %d", &rows, &cols);

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &data[i][j]);
        }
    }

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            bool okay = true;
            for (int k = 0; k < rows; k++) {
                if (data[i][j] < data[k][j]) {
                    okay = false;
                    break;
                }
            }
            if (okay) continue;
            

            for (int k = 0; k < cols; k++) {
                if (data[i][j] < data[i][k]) {
                    return false;
                }
            }
        }
    }
}

int main() {
//    freopen("
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        if (readandanswer()) printf("YES\n");
        else printf("NO\n");
    }
}
