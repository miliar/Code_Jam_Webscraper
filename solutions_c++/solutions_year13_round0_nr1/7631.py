#include <iostream>
#include <vector>

using namespace std;

int main() {
    int tCases;
    char val;
    bool found;
    int incomplete, xWin, yWin;
    vector < vector <char> > gameConfig;
    for(int i=0; i<4; i++){
        vector <char> tempVec(4);
        gameConfig.push_back(tempVec);
    }

    cin >> tCases;
    for(int cCase=1; cCase<tCases+1; cCase++){
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                cin >> val;
                gameConfig[i][j] = val;
            }
        }
        incomplete = 0;
        found = false;
        for(int i=0; i<4 && !found; i++){
            xWin = 0;
            yWin = 0;
            for(int j=0; j<4; j++){
                //cout << gameConfig[i][j] << endl;
                if(gameConfig[i][j] == 'X'){
                    xWin++;
                }
                else if(gameConfig[i][j] == 'O'){
                    yWin++;
                }
                else if(gameConfig[i][j] == 'T'){
                    xWin++;
                    yWin++;
                }
                else{
                    incomplete++;
                }
            }
            if(xWin == 4){
                cout << "Case #" << cCase << ": " << "X won" << endl;
                found = true;
            }
            else if(yWin == 4){
                cout << "Case #" << cCase << ": " << "O won" << endl;
                found = true;
            }
        }
        if(found == true){
            continue;
        }
        for(int j=0; j<4 && !found; j++){
            xWin = 0;
            yWin = 0;
            for(int i=0; i<4; i++){
                if(gameConfig[i][j] == 'X'){
                    xWin++;
                }
                else if(gameConfig[i][j] == 'O'){
                    yWin++;
                }
                else if(gameConfig[i][j] == 'T'){
                    xWin++;
                    yWin++;
                }
                else{
                    incomplete++;
                }
            }
            if(xWin == 4){
                cout << "Case #" << cCase << ": " << "X won" << endl;
                found = true;
                break;
            }
            else if(yWin == 4){
                cout << "Case #" << cCase << ": " << "O won" << endl;
                found = true;
                break;
            }
        }
        if(found == true){
            continue;
        }
        xWin = 0;
        yWin = 0;
        for(int j=0; j<4 && !found; j++){
            if(gameConfig[j][j] == 'X'){
                xWin++;
            }
            else if(gameConfig[j][j] == 'O'){
                yWin++;
            }
            else if(gameConfig[j][j] == 'T'){
                xWin++;
                yWin++;
            }
            else{
                incomplete++;
            }
        }
        if(xWin == 4){
            cout << "Case #" << cCase << ": " << "X won" << endl;
            continue;
        }
        else if(yWin == 4){
            cout << "Case #" << cCase << ": " << "O won" << endl;
            continue;
        }
        xWin = 0;
        yWin = 0;
        for(int j=0; j<4 && !found; j++){
            if(gameConfig[j][3-j] == 'X'){
                xWin++;
            }
            else if(gameConfig[j][3-j] == 'O'){
                yWin++;
            }
            else if(gameConfig[j][3-j] == 'T'){
                xWin++;
                yWin++;
            }
            else{
                incomplete++;
            }
        }
        if(xWin == 4){
            cout << "Case #" << cCase << ": " << "X won" << endl;
            continue;
        }
        else if(yWin == 4){
            cout << "Case #" << cCase << ": " << "O won" << endl;
            continue;
        }
        if(incomplete > 0){
            cout << "Case #" << cCase << ": " << "Game has not completed" << endl;
        }
        else {
            cout << "Case #" << cCase << ": " << "Draw" << endl;
        }
    }
}
