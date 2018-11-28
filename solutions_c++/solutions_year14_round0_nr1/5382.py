#include <bits/stdc++.h>

using namespace std;

int main() {
    string file;
    cin>>file;
    FILE* in = NULL, *out = NULL;
    if (file != "std") {
        in = fopen(file.c_str(), "r");
        file += ".out";
        out = fopen(file.c_str(), "w");
    }
    else {
        in = stdin;
        out = stdout;
    }

    int T;
    fscanf(in, "%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
    int a[5][5], b[5][5];
    int row1, row2;
    fscanf(in, "%d", &row1);
    for (int i = 1; i <= 4; ++i) {
        for (int j = 1; j <= 4; ++j) {
            fscanf(in, "%d", &a[i][j]);
        }
    }
    fscanf(in, "%d", &row2);
    for (int i = 1; i <= 4; ++i) {
        for (int j = 1; j <= 4; ++j) {
            fscanf(in, "%d", &b[i][j]);
        }
    }

    int cnt = 0, val = 0;
    for (int i = 1; i <= 4; ++i) {
        bool flag = 0;
        for (int j = 1; j <= 4; ++j) {
            if (a[row1][i] == b[row2][j]) {
                flag = true;
                break;
            }
        }
        if (flag) {++cnt, val = a[row1][i];}
    }

        fprintf(out, "Case #%d: ", cas);
        if (!cnt) {
            fprintf(out, "Volunteer cheated!\n");
        }
        else if (cnt == 1) {
            fprintf(out, "%d\n", val);
        }
        else fprintf(out, "Bad magician!\n");
    }

    if (file != "std") {
        fclose(in), fclose(out);
    }

    getchar();
    return 0;
}
