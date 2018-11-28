#include <cstdio>
using namespace std;

int counter = 0;
void do_magic() {
    int a[4][4];
    int b[4][4];
    int i, j;
    int ans1, ans2;
    int num_elements_match = 0;
    int card_value;

    scanf("%d", &ans1);
    for (i=0; i<4; i++) {
        scanf("%d %d %d %d", &a[i][0], &a[i][1], &a[i][2], &a[i][3]);
    }
    scanf("%d", &ans2);
    for (i=0; i<4; i++) {
        scanf("%d %d %d %d", &b[i][0], &b[i][1], &b[i][2], &b[i][3]);
    }
    ans1--;
    ans2--;

    /* match row b[ans2] with each element of a[ans1] */
    for (i=0; i<4; i++) {
        for (j = 0; j < 4; j++) {
            if (a[ans1][i] == b[ans2][j]) {
                num_elements_match++;
                card_value = a[ans1][i];
            }
        }
    }

    printf("Case #%d: ", ++counter);
    if (num_elements_match == 1) {
        printf("%d\n", card_value);
    } else if (num_elements_match > 1) {
        printf("Bad magician!\n");
    } else {
        printf("Volunteer cheated!\n");
    }
}

int main() {
    int t;
    scanf("%d", &t);
    while(t--) {
        do_magic();
    }
    return 0;
}
