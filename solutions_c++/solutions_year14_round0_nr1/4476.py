#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int r[2];
int mat[2][4][4];
int main() {
    int cases;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        for (int t = 0; t < 2; t++) {
            scanf("%d", &r[t]);
            r[t]--;
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    scanf("%d", &mat[t][i][j]);
                }
            }
        }
        vector<int> v;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (mat[0][r[0]][i] == mat[1][r[1]][j]) {
                    v.push_back(mat[0][r[0]][i]);
                }
            }
        }
        printf("Case #%d: ", T);
        if (v.size() == 1) {
            printf("%d\n", v[0]);
        } else if (v.size() == 0) {
            puts("Volunteer cheated!");
        } else if (v.size() > 1) {
            puts("Bad magician!");
        }
    }
}