#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long I64;
typedef unsigned long long U64;

char gS[2002];
char gO[2000];

char gD[10][10] = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
int gR[10] = { 0, 2, 4, 3, 8, 6, 7, 5, 1, 9 };

int findD() {
    for (int i = 0; i <= 9; i++) {
        int r = gR[i];
        int j = 0;
        int s = 0;
        while (gD[r][j]) {
            char* p = strchr(gS + s, gD[r][j]);
            if (p == NULL)
                break;
            s = p - gS + 1;
            j++;
        }
        if (gD[r][j] == 0)
            return r;
    }
    return -1;
}

void eraseD(int n) {
    for (int i = 0; gD[n][i]; i++) {
        char* p = strchr(gS, gD[n][i]);
        if (p != NULL)
            strcpy(p, p + 1);
    }
}

void solve() {
    int o = 0;
    while (gS[0]) {
        int d = findD();
        gO[o++] = d + '0';
        eraseD(d);
    }

    gO[o] = 0;
}

int main(int argc, char* argv[]) {
    FILE* fin = fopen(argv[1], "rt");
    FILE* fout = fopen(argv[2], "wt");

    int T;

    for (int i = 0; i < 10; i++)
        sort(gD[i], gD[i] + strlen(gD[i]));

    fscanf(fin, "%d", &T);
    for (int tn = 1; tn <= T; tn++) {
        fscanf(fin, "%s", gS);
        sort(gS, gS + strlen(gS));

        solve();
        sort(gO, gO + strlen(gO));
        fprintf(fout, "Case #%d: %s\n", tn, gO);
    }

    fclose(fin);
    fclose(fout);

    return 0;
}
