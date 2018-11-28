#include <iostream>

#define GRID_SIZE 4
#define BAD_MAGICIAN -1
#define CHEATED 0

using namespace std;

void setGrid(int grid[][GRID_SIZE]);
void displayGrid(int grid[][GRID_SIZE]);
int determineCard(int firstGrid[][GRID_SIZE], int seconGrid[][GRID_SIZE], int answer1, int answer2);


int main(void){
    int numOfCases, i, firstAnswer, secondAnswer, veredict;
    int firstGrid[GRID_SIZE][GRID_SIZE];
    int secondGrid[GRID_SIZE][GRID_SIZE];
    cin >> numOfCases;
    for(i=1; i<=numOfCases; i++){
        cin >> firstAnswer;
        setGrid(firstGrid);
        cin >> secondAnswer;
        setGrid(secondGrid);
        /*displayGrid(firstGrid);
        displayGrid(secondGrid);*/
        veredict=determineCard(firstGrid, secondGrid, firstAnswer-1, secondAnswer-1);
        cout << "Case #" << i << ": ";
        switch (veredict){
            case BAD_MAGICIAN:
                cout << "Bad magician!";
                break;
            case CHEATED:
                cout << "Volunteer cheated!";
                break;
            default:
                cout << veredict;
        }
        cout << endl;
    }
    return 0;
}

void setGrid(int grid[][GRID_SIZE]){
    int i, j;
    for(i=0; i<GRID_SIZE; i++){
        for(j=0; j<GRID_SIZE; j++){
            cin >> grid[i][j];
        }
    }
}

int determineCard(int firstGrid[][GRID_SIZE], int seconGrid[][GRID_SIZE], int row1, int row2){
    int posibilities, card, i, j;
    posibilities = 0;
    for(i=0; i<GRID_SIZE; i++){
        for(j=0; j<GRID_SIZE; j++){
            if(firstGrid[row1][i]==seconGrid[row2][j]){
                card=firstGrid[row1][i];
                posibilities++;
            }
        }
    }
    switch (posibilities){
        case 0:
            return CHEATED;
        case 1:
            return card;
        default:
            return BAD_MAGICIAN;
    }
}

void displayGrid(int grid[][GRID_SIZE]){
    int i, j;
    for(i=0; i<GRID_SIZE; i++){
        for(j=0; j<GRID_SIZE; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }
}
