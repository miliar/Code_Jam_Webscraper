#include <string.h>
#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int num_case;
    scanf("%d", &num_case);

    int cards[2][4][4];

    int choice[2];
    
    for (int ncas = 0; ncas < num_case; ++ncas) {
        scanf("%d", &choice[0]);
        choice[0]--;
        
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &cards[0][i][j]);
            }
        }
        scanf("%d", &choice[1]);
        choice[1]--;
        
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &cards[1][i][j]);
            }
        }
        int may_choose = 0;
        int may_be_result = -1;
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                if (cards[0][choice[0]][j] == cards[1][choice[1]][k]) {
                    may_choose++;
                    may_be_result = cards[0][choice[0]][j];
                }
            }
        }

        if (may_choose == 1) {
            printf("Case #%d: %d\n", ncas+1, may_be_result);
        } else if (may_choose > 1){
            printf("Case #%d: Bad magician!\n", ncas+1);
        } else {
            printf("Case #%d: Volunteer cheated!\n", ncas+1);            
        }
    }
    return 0;
}

//(setenv "PATH" "/usr/bin")
