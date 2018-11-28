#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <set>
#include <iostream>

using namespace std;

#define MAX 5
#define INF 0x3f3f3f3f
#define MOD 1000000007

typedef long long LL;

int nMatrix[MAX][MAX];
int nMatrix2[MAX][MAX];

int main(void) {
    int nCase;
    while (~scanf("%d", &nCase)) {
        for (int cas = 1; cas <= nCase; ++cas) {
            int A;
            int B;
            scanf("%d", &A);
            for (int i = 0; i < 4; ++i) {
                for (int j = 0; j < 4; ++j) {
                    scanf("%d", &nMatrix[i][j]);
                }
            }
            scanf("%d", &B);
            for (int i = 0; i < 4; ++i) {
                for (int j = 0; j < 4; ++j) {
                    scanf("%d", &nMatrix2[i][j]);
                }
            }
            printf("Case #%d: ", cas);

            if (A < 0 || A > 4 || B < 0 || B > 4) {
                printf("Volunteer cheated!\n");
            } else {
                int nSum = 0;
                int id = -1;
                --A;
                --B;
                for (int j = 0; j < 4; ++j) {
                    for (int k = 0; k < 4; ++k) {
                        if (nMatrix[A][j] == nMatrix2[B][k]) {
                            ++nSum;
                            id = nMatrix[A][j];
                            break;
                        }
                    }
                }
                if (0 == nSum) {
                    printf("Volunteer cheated!\n");
                } else if (1 == nSum) {
                    printf("%d\n", id);
                } else {
                    printf("Bad magician!\n");
                }
            }
        }
    }
    return 0;
}