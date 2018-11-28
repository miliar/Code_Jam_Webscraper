#include <iostream>

typedef enum {NORTH=1, NORTH_WEST, NORTH_EAST, WEST, EAST, SOUTH, SOUTH_WEST, SOUTH_EAST} neighbors;

using namespace std;

char** grid;

int rows, colums;
int numOfCellsRevealed;
int cellsToBeRevealed;

void initializeGrid();
void deleteAll();
void printGrid();
bool findQuickestGame();
void putMines();
bool revealNeighborsCells(int row, int colum, char** originalGrid, int numOfCells);
void copyGrid(char** cloneGrid, char** originalGrid );
int* addDierection(int* directions, int n, int direction);


int main(){
    int numOfCases, i, j, numOfMines;
    cin >> numOfCases;
    for(i=1; i<=numOfCases; i++){
        cin >> rows;
        cin >> colums;
        cin >> numOfMines;
        grid = new char*[rows];
        for(j=0; j<rows; j++){
            grid[j] = new char[colums];
        }
        cellsToBeRevealed = (rows*colums) - numOfMines;
        cout << "Case #" << i << ":" << endl;
        if(findQuickestGame()){
            printGrid();
        }
        else{
            cout << "Impossible" << endl;
        }
        deleteAll();
    }
}

void initializeGrid(){
    int i, j;
    for(i=0; i<rows; i++){
        for(j=0; j<colums; j++){
            grid[i][j] = ' ';
        }
    }
}

void deleteAll(){
    for(int i=0; i<rows; i++){
        delete[] grid[i];
    }
    delete[] grid;
    grid = NULL;
}

void printGrid(){
    int i, j;
    for(i=0; i<rows; i++){
        for(j=0; j<colums; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }
}

void putMines(){
    int i, j;
    for(i=0; i<rows; i++){
        for(j=0; j<colums; j++){
            if(grid[i][j]==' '){
                grid[i][j]='*';
            }
        }
    }
}

bool findQuickestGame(){
    int i, j;
    //For each cell we will assume that it is the one that will reveal all the other cells
    bool isPossible=false;
    for(i=0; i<rows && !isPossible; i++){
        for(j=0; j<colums && !isPossible; j++){
            initializeGrid();
            grid[i][j]='c';
            numOfCellsRevealed = 1;
            isPossible = revealNeighborsCells(i, j, grid, numOfCellsRevealed);
        }
    }
    if (isPossible)
        putMines();
    return isPossible;
}

bool revealNeighborsCells(int row, int colum, char** originalGrid, int numOfCells){
    bool isPossible=false;
    char** cloneGrid;
    int* possibleDirections=NULL;
    int i, num;
    num=0;
    cloneGrid = new char*[rows];
    for(i=0; i<rows; i++){
        cloneGrid[i] = new char[colums];
    }
    copyGrid(cloneGrid, originalGrid);
    if(numOfCellsRevealed<cellsToBeRevealed){
        if(row>0){
            //Check North
            if(cloneGrid[row-1][colum]==' '){
                possibleDirections = addDierection(possibleDirections, num++, NORTH);
                cloneGrid[row-1][colum]='.';
                numOfCells++;
            }
            //Check North-West
            if(colum>0 && cloneGrid[row-1][colum-1]==' '){
                possibleDirections = addDierection(possibleDirections, num++, NORTH_WEST);
                cloneGrid[row-1][colum-1]='.';
                numOfCells++;
            }
            //Check North-East
            if(colum<colums-1 && cloneGrid[row-1][colum+1]==' '){
                possibleDirections = addDierection(possibleDirections, num++, NORTH_EAST);
                cloneGrid[row-1][colum+1]='.';
                numOfCells++;
            }
        }
        if(row<rows-1){
            //Check South
            if(cloneGrid[row+1][colum]==' '){
                possibleDirections = addDierection(possibleDirections, num++, SOUTH);
                cloneGrid[row+1][colum]='.';
                numOfCells++;
            }
            //Check South-West
            if(colum>0 && cloneGrid[row+1][colum-1]==' '){
                possibleDirections = addDierection(possibleDirections, num++, SOUTH_WEST);
                cloneGrid[row+1][colum-1]='.';
                numOfCells++;;
            }
            //Check South-East
            if(colum<colums-1 && cloneGrid[row+1][colum+1]==' '){
                possibleDirections = addDierection(possibleDirections, num++, SOUTH_EAST);
                cloneGrid[row+1][colum+1]='.';
                numOfCells++;
            }
        }
        //Check West
        if(colum>0 && cloneGrid[row][colum-1]==' '){
            possibleDirections = addDierection(possibleDirections, num++, WEST);
            cloneGrid[row][colum-1]='.';
            numOfCells++;
        }
        //Check East
        if(colum<colums-1 && cloneGrid[row][colum+1]==' '){
            possibleDirections = addDierection(possibleDirections, num++, EAST);
            cloneGrid[row][colum+1]='.';
            numOfCells++;
        }
    }
    if(numOfCells<cellsToBeRevealed){
        for(i=0; i<num && !isPossible; i++){
            switch(possibleDirections[i]){
            case NORTH:
                isPossible = revealNeighborsCells(row-1, colum, cloneGrid, numOfCells);
                break;
            case NORTH_EAST:
                isPossible = revealNeighborsCells(row-1, colum+1, cloneGrid, numOfCells);
                break;
            case NORTH_WEST:
                isPossible = revealNeighborsCells(row-1, colum-1, cloneGrid, numOfCells);
                break;
            case SOUTH:
                isPossible = revealNeighborsCells(row+1, colum, cloneGrid, numOfCells);
                break;
            case SOUTH_EAST:
                isPossible = revealNeighborsCells(row+1, colum+1, cloneGrid, numOfCells);
                break;
            case SOUTH_WEST:
                isPossible = revealNeighborsCells(row+1, colum-1, cloneGrid, numOfCells);
                break;
            case EAST:
                isPossible = revealNeighborsCells(row, colum+1, cloneGrid, numOfCells);
                break;
            case WEST:
                isPossible = revealNeighborsCells(row, colum-1, cloneGrid, numOfCells);
                break;
            default: ;
            }
        }
    }
    else if(numOfCells==cellsToBeRevealed){
        isPossible=true;
    }
    if(isPossible){
        copyGrid(originalGrid, cloneGrid);
    }
    for(i=0; i<rows; i++){
        delete[] cloneGrid[i];
    }
    delete[] cloneGrid;
    delete[] possibleDirections;
    return isPossible;
}

int* addDierection(int* directions, int n, int direction){
    int i;
    int* temp = new int[n+1];
    for(i=0; i<n; i++){
        temp[i] = directions[i];
    }
    temp[i]=direction;
    delete[] directions;
    return temp;
}

void copyGrid(char** cloneGrid, char** originalGrid ){
    int i, j;
    for(i=0; i<rows; i++){
        for(j=0; j<colums; j++){
            cloneGrid[i][j]=originalGrid[i][j];
        }
    }
}
