#include<iostream>
#define QTD 4

using namespace std;

char table[4][4];

enum State{
    PLAYEROWON,PLAYERXWON,GAMENOTCOMPLETE
};

bool isNotOver(State gameState){
    return (gameState!=PLAYERXWON&&gameState!=PLAYEROWON);
}

int main(){

    int qtd;
    int pO=0,pX=0,pT=0,pP=0,pPointsEmpty=0;
    State gameState;

    cin >> qtd;

    for(int k=0;k<qtd;++k){

        // Inicializing varibles
        gameState = GAMENOTCOMPLETE;
        pO = pX = pT = pP = pPointsEmpty = 0;

        // Receiving values
        for(int i=0;i<QTD;++i){
            for(int j=0;j<QTD;++j){
                cin >> table[i][j];
            }
        }

        // Looking for lines
        for(int i=0;i<QTD;++i){
            // Reseting varibles
            pO = pX = pT = pP = 0;
            for(int j=0;j<QTD;++j){
                if(table[i][j]=='X') pX++;
                else if(table[i][j]=='O') pO++;
                else if(table[i][j]=='.'){
                    pP++;
                    pPointsEmpty++;
                }
                else pT++;
            }
            if(pO>2&&pP==0&&pX==0&&isNotOver(gameState)) gameState = PLAYEROWON;
            if(pX>2&&pP==0&&pO==0&&isNotOver(gameState)) gameState = PLAYERXWON;
        }

        // Looking for columns
        for(int i=0;i<QTD;++i){
            // Reseting varibles
            pO = pX = pT = pP = 0;
            for(int j=0;j<QTD;++j){
                if(table[j][i]=='X') pX++;
                else if(table[j][i]=='O') pO++;
                else if(table[j][i]=='.'){
                    pP++;
                    pPointsEmpty++;
                }
                else pT++;
            }
            if(pO>2&&pP==0&&pX==0&&isNotOver(gameState)) gameState = PLAYEROWON;
            if(pX>2&&pP==0&&pO==0&&isNotOver(gameState)) gameState = PLAYERXWON;
        }

        // Looking diagonals

        // Diagonal 1
        pO = pX = pT = pP = 0;
        for(int i=0;i<QTD;++i){
            if(table[i][i]=='X') pX++;
            else if(table[i][i]=='O') pO++;
            else if(table[i][i]=='.'){
                pP++;
                pPointsEmpty++;
            }
            else pT++;
        }
        if(pO>2&&pP==0&&pX==0&&isNotOver(gameState)) gameState = PLAYEROWON;
        if(pX>2&&pP==0&&pO==0&&isNotOver(gameState)) gameState = PLAYERXWON;

        // Diagonal 2
        pO = pX = pT = pP = 0;
        for(int i=0;i<QTD;++i){
            if(table[QTD-1-i][i]=='X') pX++;
            else if(table[QTD-1-i][i]=='O') pO++;
            else if(table[QTD-1-i][i]=='.'){
                pP++;
                pPointsEmpty++;
            }
            else pT++;
        }
        if(pO>2&&pP==0&&pX==0&&isNotOver(gameState)) gameState = PLAYEROWON;
        if(pX>2&&pP==0&&pO==0&&isNotOver(gameState)) gameState = PLAYERXWON;

        // Result
        cout << "Case #" << k+1 <<": ";
        if(isNotOver(gameState)&&pPointsEmpty==0) cout << "Draw";
        else if(gameState==PLAYEROWON) cout << "O won";
        else if(gameState==PLAYERXWON) cout << "X won";
        else cout << "Game has not completed";
        cout << endl;

    }

}
