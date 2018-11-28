#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        int r1, r2;
        int line[4];
        bool cnt[17] = {false};
        scanf("%d", &r1);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &line[j]);
            }
            if (i + 1 == r1) {
                for (int k = 0; k < 4; ++k) {
                    cnt[line[k]] = true;
                }
            }
        }
        int res;
        int ans = 0;
        int tar;
        scanf("%d", &r2);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &line[j]);
            }
            if (i + 1 == r2) {
                for (int k = 0; k < 4; ++k) {
                    if (cnt[line[k]]) {
                        ++ans;
                        tar = line[k];
                    }
                }
            }
        }
        printf("Case #%d: ", t);
        if (ans == 0) {
            printf("Volunteer cheated!\n");
        } else if (ans == 1) {
            printf("%d\n", tar);
        } else {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
