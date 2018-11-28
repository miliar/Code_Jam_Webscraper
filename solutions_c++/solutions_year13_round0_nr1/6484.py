#include <iostream>
#include <cstring>
#include <string>
using namespace std;

char board[8][8];
int countX1[4];
int countO1[4];
int countX2[4];
int countO2[4];
int countO3[2];
int countX3[2];


int main (){
    int T, t = 0;
    cin >> T;
    while (T--) {
        memset(board, 0, sizeof (board));
        memset(countO1, 0, sizeof (countO1));
        memset(countX1, 0, sizeof (countX1));
        memset(countO2, 0, sizeof (countO2));
        memset(countX2, 0, sizeof (countX2));
        memset(countO3, 0, sizeof (countO3));
        memset(countX3, 0, sizeof (countX3));
        
        bool finished = true;
        bool knowWinner  = false;
        string winner = "";
        t++;
        for (int i = 0 ; i < 4; i++){
            for (int j = 0 ; j < 4; j++){
                cin >> board[i][j];
                if (board[i][j] == '.')
                    finished = false;
            }
        }
        
        for (int i = 0 ; i < 4; i++){
            for(int j = 0 ;j < 4; j++) {
                if (i==j){
                    if (board[i][j] == 'O' || board[i][j] =='T')
                        countO3[0]++;
                    if (board[i][j] == 'X' || board[i][j] =='T')
                        countX3[0]++;
                }
                if (i+j==3){
                    if (board[i][j] == 'O' || board[i][j] =='T')
                        countO3[1]++;
                    if (board[i][j] == 'X' || board[i][j] =='T')
                        countX3[1]++;
                }
                if (board[i][j] == 'O' || board[i][j] =='T')
                    countO1[i]++;
                if (board[i][j] == 'X' || board[i][j] =='T')
                    countX1[i]++;
            }
        }
        
        for (int j = 0 ; j < 4; j++){
            for(int i = 0 ;i < 4; i++) {
                if (board[i][j] == 'O' || board[i][j] =='T')
                    countO2[j]++;
                if (board[i][j] == 'X' || board[i][j] =='T')
                    countX2[j]++;
            }
        }
        
        
        for (int i= 0; i < 4; i++){
            if (i < 2) {
                if (countO3[i] == 4){
                    finished = true;
                    knowWinner = true;
                    winner ='O';
                }
                if (countX3[i] == 4){
                    finished = true;
                    knowWinner = true;
                    winner = 'X';
                }
            }
            if (countX1[i] == 4 || countX2[i] == 4){
                finished = true;
                knowWinner = true;
                winner = 'X';
            }
            if (countO1[i] == 4 || countO2[i] == 4){
                finished = true;
                knowWinner = true;
                winner ='O';
            }
        }
        
        if (finished){
            if (knowWinner){
                cout << "Case #" << t << ": " << winner <<" won"<<endl;
            }
            else
                cout << "Case #" << t << ": Draw" << endl;
        }
        else
            cout << "Case #" << t << ": Game has not completed" << endl;
        
    }
}