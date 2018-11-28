#include <cstdio>


using namespace std;

int main() {

    int T;
    scanf("%d", &T);
    for(int testCase = 1; testCase <= T; testCase++) {
        int answer1,answer2;
        scanf("%d", &answer1);

        int cards[4][4];
        for (int i = 0; i < 4; i++) {
            scanf("%d %d %d %d", &cards[i][0], &cards[i][1], &cards[i][2], &cards[i][3]);
        }

        int row[4];
        for(int i = 0; i < 4; i++) {
            row[i] = cards[answer1-1][i];
        }

        scanf("%d", &answer2);
        for (int i = 0; i < 4; i++) {
            scanf("%d %d %d %d", &cards[i][0], &cards[i][1], &cards[i][2], &cards[i][3]);
        }

        bool found = false;
        bool multiple = false;
        int result = -1;

        int* snd = cards[answer2-1];
        for(int i = 0; i < 4; i++) {
           
            for(int j = 0; j < 4; j++) {
                if (row[i] == snd[j]) {
                    if (found) multiple = true;
                    found = true;
                    result = row[i];
                }
            }
        }

        printf("Case #%d: ", testCase);
        if (multiple) {
            printf("Bad magician!\n");
        } else if (!found) {
            printf("Volunteer cheated!\n");
        } else {
            printf("%d\n", result);
        }

    }
    return 0;
}

