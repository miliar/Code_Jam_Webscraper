#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
FILE *answer;
typedef long double LF;


LF naomiDW[1001], kenDW[1001], naomiW[1001], kenW[1001];
int BlocksQuantity;

void read(){
    scanf("%d", &BlocksQuantity);
    for (int i=0; i<BlocksQuantity; i++){
        LF A;
        scanf("%Lf", &A);
        naomiDW[i] = A;
        naomiW[i] = A;
    }

    for (int i=0; i<BlocksQuantity; i++){
        LF A;
        scanf("%Lf", &A);
        kenDW[i] = A;
        kenW[i] = A;
    }
}

int DW(){
    int answerDW = 0;
    for (int k=0; k<BlocksQuantity; k++){
        LF chosennaomi, chosenken;
        chosenken = 1.0;
        int x = -1;
        for (int i=0; i<BlocksQuantity; i++){
            if (kenDW[i] < chosenken && kenDW[i] > 0){
                chosenken = kenDW[i];
                x = i;
            }
        }
        kenDW[x] = 0;

        x = -1;
        chosennaomi = 1.0;
        for (int i=0; i<BlocksQuantity; i++){
            if (naomiDW[i] < chosennaomi && naomiDW[i] > chosenken && naomiDW[i] > 0){
                x = i;
                chosennaomi = naomiDW[i];
            }
        }
        if (chosennaomi == 1){
            for (int i=0; i<BlocksQuantity; i++){
                if (naomiDW[i] < chosennaomi && naomiDW[i] > 0){
                    x = i;
                    chosennaomi = naomiDW[i];
                }
            }
        }
        naomiDW[x] = 0;

        if(chosenken < chosennaomi) answerDW++;
    }

    return answerDW;
}

int W(){
    int answerW = 0;
    for (int k=0; k<BlocksQuantity; k++){
        LF chosennaomi, chosenken;

        //find chosen naomi:
        int x = -1;
        chosennaomi = 1.0;
        for (int i=0; i<BlocksQuantity; i++){
            if (chosennaomi > naomiW[i] && naomiW[i] != 0){
                x = i;
                chosennaomi = naomiW[i];
            }
        }
        naomiW[x] = 0;
        //~

        //find chosen ken:
        LF maxken = 0.0;
        for (int i=0; i<BlocksQuantity; i++)
            maxken = max (maxken, kenW[i]);

        if (maxken < chosennaomi){
            chosenken = 1.0;
            x = -1;
            for (int i=0; i<BlocksQuantity; i++){
                if (chosenken > kenW[i] && kenW[i] != 0){
                    x = i;
                    chosenken = kenW[i];
                }
            }
            kenW[x] = 0;
        }
        else{
            chosenken = 1.0;
            x = -1;
            for (int i=0; i<BlocksQuantity; i++){
                if(chosenken > kenW[i] && kenW[i] > chosennaomi && kenW[i] != 0){
                    x = i;
                    chosenken = kenW[i];
                }
            }
            kenW[x] = 0;
        }

        if (chosennaomi > chosenken) answerW++;
    }

    return answerW;
}

void program(int TestNumber){
    read();
    int answerDW, answerW;
    answerDW = DW();
    answerW = W();
    fprintf(answer, "Case #%d: %d %d \n", TestNumber, answerDW, answerW);
}

int main(){
    answer = fopen("/home/staniul/Desktop/Google Code Jam/ProblemD_DeceitfulWar/answe.in", "w");
    int T;
    scanf("%d", &T);

    for (int i=1; i<=T; i++)
        program (i);

    fclose (answer);
    return 0;
}
