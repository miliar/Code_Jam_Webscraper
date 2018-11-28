#include<iostream>
#include<fstream>
#include<string>

using namespace std;
int win(int matrix [][4]);
int main() {

    ifstream ifile("A-large.in");
    ofstream ofile("example.txt");
    if (ifile.is_open()) {
        int test;
        ifile >> test;

        for(int k= 0; k < test; k++){
            string board[4];
            for(int i = 0; i < 4; i++)
                ifile >> board[i];
            int matrix[4][4];
            for(int i = 0; i < 4; i++){
                for(int j = 0; j < 4; j++){
                    switch(board[i][j]){
                    case 'X':
                        matrix[i][j] = -1;
                        break;
                    case 'O':
                        matrix[i][j] = 1;
                        break;
                    case 'T':
                        matrix[i][j] = 0;
                        break;
                    default:
                        matrix[i][j] = 20;
                    }
                }
            }
            int result = win(matrix);

            if(result == 1)
                ofile << "Case #" << k+1 << ": " << "O won" << endl;
            else if(result == -1)
                ofile << "Case #" << k+1 << ": " << "X won" << endl;
            else if(result == 50)
                ofile << "Case #" << k+1 << ": " << "Game has not completed" << endl;
            else
                ofile << "Case #" << k+1 << ": " << "Draw" << endl;
        }
        ifile.close();
    }
    return 0;
}

int win(int matrix [][4]){
    for(int i = 0; i < 4; i++) {
        int sumRow = 0;
        for(int j = 0 ; j < 4; j++){
            sumRow += matrix[i][j];
        }
        if( sumRow == -4 ||  sumRow== -3){
            return -1;
        } else if( sumRow == 4 || sumRow ==3){
            return 1;
        }

        int sumCol = 0;
        for(int j = 0 ; j < 4; j++){
            sumCol += matrix[j][i];
        }
        if( sumCol == -4 || sumCol == -3){
            return -1;
        } else if( sumCol == 4 ||sumCol == 3){
            return 1;
        }
    }
    int sumdia1 = matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[3][3];
    if( sumdia1 == -4 || sumdia1 == -3){
        return -1;
    } else if( sumdia1 == 4 || sumdia1 == 3){
        return 1;
    }
    int sumdia2 = matrix[0][3] + matrix[1][2] + matrix[2][1] + matrix[3][0];
    if(sumdia2 == -4 || sumdia2 == -3){
        return -1;
    } else if( sumdia2 == 4 || sumdia2 == 3){
        return 1;
    }
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(matrix[i][j] == 20){
                return 50;
            }
        }
    }
    return 100;
}
