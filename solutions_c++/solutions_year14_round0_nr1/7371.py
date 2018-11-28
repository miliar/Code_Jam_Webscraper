#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int cmp_asc(const void* p1, const void *p2) {
    return *(int*)p1 - *(int*)p2;
}

int cmp_desc(const void* p1, const void *p2) {
    return *(int*)p2 - *(int*)p1;
}

int cards1[10][10];
int cards2[10][10];

int main() {
    int cnt_case = 0;
    scanf("%d", &cnt_case);
    int case_idx = 0;
    while (cnt_case--) {
        ++case_idx;

        // compute here

        memset(cards1, 0, sizeof(cards1));
        memset(cards2, 0, sizeof(cards2));

        int row1,row2;
        scanf("%d", &row1);
        for (int i = 1; i <= 4; ++i) {
            for (int j = 1; j <= 4; ++j) {
                scanf("%d", &cards1[i][j]);
            }
        }

        scanf("%d", &row2);
        for (int i = 1; i <=4; ++i) {
            for (int j = 1; j <= 4; ++j) {
                scanf("%d", &cards2[i][j]);
            }
        }

        bool showed[20] =  {false};
        for (int i = 1; i <= 4; ++i) {
            showed[cards1[row1][i]] = true;
        }

        bool found = false;
        int res = -1;
        bool bad = false;
        for (int i = 1; i <=4; ++i) {
            if (showed[cards2[row2][i]]) {
                if (found) {
                    bad = true;
                } else {
                    found = true;
                    res = cards2[row2][i];
                }
            }
        }

        printf("Case #%d: ", case_idx);
        
        // output here
        if (!found) {
            printf("Volunteer cheated!\n");
        } else {
            if (bad) {
                printf("Bad magician!\n");
            } else {
                printf("%d\n", res);
            }
        }
    }
    return 0;
}
