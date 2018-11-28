#include <cstdio>

int main(int argc, char const *argv[])
{
    int T, cases, frow, srow;
    int first[4][4];
    int second[4][4];
    scanf("%d", &T);
    for(cases = 1; cases <= T; cases++) {
        scanf("%d", &frow);
        frow--;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &first[i][j]);
            }
        }
        scanf("%d", &srow);
        srow--;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &second[i][j]);
            }
        }
        int matches = 0;
        int match;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                if(first[frow][i] == second[srow][j]) {
                    match = first[frow][i];
                    matches++;
                }
            }
        }
        printf("Case #%d: ", cases);
        if(matches == 0) {
            printf("Volunteer cheated!\n");
        } else if (matches > 1) {
            printf("Bad magician!\n");
        } else {
            printf("%d\n", match);
        }
    }
    return 0;
}