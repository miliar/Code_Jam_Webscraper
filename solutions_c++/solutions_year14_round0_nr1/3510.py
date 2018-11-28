#include <cstdio>
#include <cstdlib>
#include <cstring>


int cnt[16];

void check_unique(int cs)
{
    int two_pos = -1;
    for (int i = 0; i < 16; i++) {
        if (cnt[i] == 2) {
            if (two_pos == -1) {
                two_pos = i;
            } else {
                printf("Case #%d: Bad magician!\n", cs);
                return;
            }
        }
    }
    if (two_pos == -1) {
        printf("Case #%d: Volunteer cheated!\n", cs);
    } else {
        printf("Case #%d: %d\n", cs, two_pos +1 );
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int cs = 1; cs <= T; cs++) {
        memset(cnt, 0, sizeof(int) * 16);
        for (int k = 0; k < 2; k++) {
            int row;
            scanf("%d", &row);
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    int num;
                    scanf("%d", &num);
                    if (i == row - 1) {
                        cnt[num-1]++;
                    }
                }
            }
        }
        check_unique(cs);
    }
    return 0;
}
