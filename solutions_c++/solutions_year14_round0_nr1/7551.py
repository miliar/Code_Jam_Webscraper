#include <iostream>
#include <stdio.h>

using namespace std;

int card1[4][4];
int card2[4][4];
bool mark[4];

int main() {
    int NN;
    scanf("%d",&NN);
    for (int II = 0; II < NN; ++II) {
        mark[0] = false;
        mark[1] = false;
        mark[2] = false;
        mark[3] = false;
        int card1SelectedRow, card2SelectedRow;
        scanf("%d",&card1SelectedRow);
        --card1SelectedRow;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                card1[i][j] = 0;
                scanf("%d",&card1[i][j]);
            }
        }
        scanf("%d",&card2SelectedRow);
        --card2SelectedRow;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                card2[i][j] = 0;
                scanf("%d",&card2[i][j]);
            }
        }
        /*printf("%d\n",card1SelectedRow);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                printf("%d ",card1[i][j]);
            }
            printf("\n");
        }
        printf("%d\n",card2SelectedRow);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                printf("%d ",card2[i][j]);
            }
            printf("\n");
        }*/
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (card2[card2SelectedRow][i] == card1[card1SelectedRow][j]) {
                    mark[j] = true;
                }
            }
        }
        int countMark = 0, number;
        for (int i = 0; i < 4; ++i) {
            if (mark[i] == true) {
                number = card1[card1SelectedRow][i];
                ++countMark;
            }
        }
        
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (card2[card2SelectedRow][i] == card1[card1SelectedRow][j]) {
                    mark[j] = true;
                }
            }
        }
        printf("Case #%d: ", II+1);
        if (countMark == 0) {
            printf("Volunteer cheated!");
        }
        else if (countMark == 1) {
            printf("%d", number);
        }
        else {
            printf("Bad magician!");
        }
        printf("\n");
    }
}