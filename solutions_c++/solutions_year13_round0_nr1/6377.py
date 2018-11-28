#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(void){

ifstream fin ("A-large.in");
ofstream fout ("tiktaktoe.out");

int T, o_sum, x_sum, col=4, row=4, draw = 0;
char board[4][4] = {0};
string winner;

fin >> T;

for(int i=0; i<T; i++){
//cout << i << endl;
    //populate the gameboard
    for(int j=0; j<row; j++){
        for(int k=0; k<col; k++){
            fin >> board[j][k];
        }
    }


    winner = "";

    //Check horizontally
    for(int j=0; j<row; j++){
        o_sum = 0;
        x_sum = 0;
        for(int k=0; k<col; k++){
            if(board[j][k] == 'O'){
                o_sum++;
            }
            else if(board[j][k] == 'X'){
                x_sum++;
            }
            else if(board[j][k] == 'T'){
                o_sum++;
                x_sum++;
            }
        }///
        if(o_sum == 4){ //end of row, o_winner yet?
            winner = "O won";
            break;
        }
        else if(x_sum == 4){ //end of row, o_winner yet?
            winner = "X won";
            break;
        }
    }
    if(winner == ""){ //Check vertically if no winner yet
        for(int j=0; j<row; j++){
            o_sum = 0;
            x_sum = 0;
            for(int k=0; k<col; k++){
                if(board[k][j] == 'O'){
                    o_sum++;
                }
                else if(board[k][j] == 'X'){
                    x_sum++;
                }
                else if(board[k][j] == 'T'){
                    o_sum++;
                    x_sum++;
                }
            }///
            if(o_sum == 4){
                winner = "O won";
                break;
            }
            else if(x_sum == 4){
                winner = "X won";
                break;
            }
        }
    }
    if(winner == ""){ //Check diagonally down to the right if no winner yet
        o_sum = 0;
        x_sum = 0;

        if(board[0][0] == 'O'){o_sum++;}if(board[1][1] == 'O'){o_sum++;}if(board[2][2] == 'O'){o_sum++;}if(board[3][3] == 'O'){o_sum++;}
        if(board[0][0] == 'X'){x_sum++;}if(board[1][1] == 'X'){x_sum++;}if(board[2][2] == 'X'){x_sum++;}if(board[3][3] == 'X'){x_sum++;}

        if(board[0][0] == 'T'){o_sum++;x_sum++;}if(board[1][1] == 'T'){o_sum++;x_sum++;}
        if(board[2][2] == 'T'){o_sum++;x_sum++;}if(board[3][3] == 'T'){o_sum++;x_sum++;}

        if(o_sum == 4){
            winner = "O won";
        }
        else if(x_sum == 4){
            winner = "X won";
        }
    }
    if(winner == ""){ //Check diagonally down to the left if no winner yet
        o_sum = 0;
        x_sum = 0;

        if(board[0][3] == 'O'){o_sum++;}if(board[1][2] == 'O'){o_sum++;}if(board[2][1] == 'O'){o_sum++;}if(board[3][0] == 'O'){o_sum++;}
        if(board[0][3] == 'X'){x_sum++;}if(board[1][2] == 'X'){x_sum++;}if(board[2][1] == 'X'){x_sum++;}if(board[3][0] == 'X'){x_sum++;}

        if(board[0][3] == 'T'){o_sum++;x_sum++;}if(board[1][2] == 'T'){o_sum++;x_sum++;}
        if(board[2][1] == 'T'){o_sum++;x_sum++;}if(board[3][0] == 'T'){o_sum++;x_sum++;}

        if(o_sum == 4){
            winner = "O won";
        }
        else if(x_sum == 4){
            winner = "X won";
        }
    }

    //count to see if gameboard is full
    draw = 0;
    for(int j=0; j<row; j++){
        for(int k=0; k<col; k++){
            if(board[j][k] != '.'){
                    draw++;
            }
        }
    }

    fout << "Case #" << (i+1) << ": ";
    if(winner == "" && draw == 16){
        fout << "Draw";
    }
    else if(winner == ""){
        fout << "Game has not completed";
    }
    else{
        fout << winner;
    }

    if(i!=(T-1)){
        fout << endl;
    }

}

return 0;
}
