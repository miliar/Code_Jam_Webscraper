#include <cstdio>

using namespace std;

int main(int argc, char *argv[]) {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int r;
        scanf("%d", &r);
        int r1[4];
        int r2[4];
        int n = -1;
        for (int j = 0; j < 4; j++) {
            scanf("%d %d %d %d", &(r2[0]), &(r2[1]), &(r2[2]), &(r2[3]));
            if (j + 1 == r) {
                r1[0] = r2[0];
                r1[1] = r2[1];
                r1[2] = r2[2];
                r1[3] = r2[3];
            }
        }
        scanf("%d", &r);
        bool bad = false;
        for (int j = 0; j < 4; j++) {
            scanf("%d %d %d %d", &(r2[0]), &(r2[1]), &(r2[2]), &(r2[3]));
            if (j + 1 == r) {
                for (int k = 0; k < 4; k++) {
                    for (int l = 0; l < 4; l++) {
                        if (r1[k] == r2[l]) {
                            if (n == -1) n = r1[k];
                            else {
                                bad = true;
                            }
                        }
                    }
                }
            }
        }
        if (bad) {
            printf("Case #%d: Bad magician!\n", i + 1);
        }
        else if (n == -1) {
            printf("Case #%d: Volunteer cheated!\n", i + 1);
        }
        else {
            printf("Case #%d: %d\n", i + 1, n);
        }
    }
    return 0;
}
