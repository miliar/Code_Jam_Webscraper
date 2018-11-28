#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>

#define ll long long int

using namespace std;

vector<string> board(5);
int T;

int main(){

    cin >> T;
    for(int i = 0; i < T; i++){
        for(int j = 0; j < 4; j++){
            cin >> board[j];
        }
        char winner = ' ';
        for(int a = 0; a < 4; a++){
            for(int b = 0; b < 4; b++){
                if( board[a][b] == '.'){
                    winner = '0';
                    board[a][b] = '0';
                }else if(board[a][b] == 'X'){
                    board[a][b] = '1';
                }else if(board[a][b] == 'T'){
                    board[a][b] = '2';
                }else{
                    board[a][b] = '3';
                }
            }

        }
        bool cflag = false;
        
        for( int a = 0; a < 4; a++){
            
            if( board[a][0] != '0' && board[a][1] != '0' && board[a][2] != '0' && board[a][3] != '0' && ((board[a][0] <= '2' && board[a][1] <= '2' && board[a][2] <= '2' && board[a][3] <= '2') || (board[a][0] >= '2' && board[a][1] >= '2' && board[a][2] >= '2' && board[a][3] >= '2'))){
                cflag = true;
                if(board[a][0] != '2'){
                    winner = board[a][0];
                }else{
                    winner = board[a][1];
                }
                break;
            }
            if( a == 0 && board[a][0] != '0' && board[a+1][1] != '0' && board[a+2][2] != '0' && board[a+3][3] != '0' && ((board[a][0] <= '2' && board[a+1][1] <= '2' && board[a+2][2] <= '2' && board[a+3][3] <= '2') || (board[a][0] >= '2' && board[a+1][1] >= '2' && board[a+2][2] >= '2' && board[a+3][3] >= '2'))){
                cflag = true;
                if(board[a][0] != '2'){
                    winner = board[a][0];
                }else{
                    winner = board[a+1][1];
                }
                break;
            }
            if(a == 3 && board[a][0] != '0' && board[a-1][1] != '0' && board[a-2][2] != '0' && board[a-3][3] != '0' && ((board[a][0] <= '2' && board[a-1][1] <= '2' && board[a-2][2] <= '2' && board[a-3][3] <= '2') || (board[a][0] >= '2' && board[a-1][1] >= '2' && board[a-2][2] >= '2' && board[a-3][3] >= '2'))){
                cflag = true;
                if(board[a][0] != '2'){
                    winner = board[a][0];
                }else{
                    winner = board[a-1][1];
                }
                break;
            }
        }if(!cflag){
            for( int b = 0; b < 4; b++){
                if( board[0][b] != '0' && board[1][b] != '0' && board[2][b] != '0' && board[3][b] != '0' && ((board[0][b] <= '2' && board[1][b] <= '2' && board[2][b] <= '2' && board[3][b] <= '2') || (board[0][b] >= '2' && board[1][b] >= '2' && board[2][b] >= '2' && board[3][b] >= '2'))){
                    cflag = true;
                    if(board[0][b] != '2'){
                        winner = board[0][b];
                    }else{
                        winner = board[1][b];
                    }
                    break;
                }
            }
        }
        cout << "Case #" << i+1 << ": ";
        if(winner == ' '){
            cout << "Draw" << endl;
        }else if( winner == '1'){
            cout << "X won" << endl;
        }else if( winner == '3'){
            cout << "O won" << endl;
        }else{
            cout << "Game has not completed" << endl;
        }
    }
    return 0;
}