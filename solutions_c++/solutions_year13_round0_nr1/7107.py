#include <iostream>
#include <cctype>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main(){
    ifstream infile("A-large.in");
    ofstream outfile ("output.out");
    int T;
    infile >> T;
    
    for (int i =0; i<T; i++) {
        vector <string> board;
        bool X = false;
        bool O = false;
        bool empty = false;
        for(int j=0; j<4; j++){
            string input;
            infile >> input;
            //getline(infile, input);
            board.push_back(input);
            if (input == "XXXX" || input == "TXXX" || input == "XTXX" || input == "XXTX" || input == "XXXT"){
                X = true;
            }
            if (input == "OOOO" || input == "TOOO" || input == "OTOO" || input == "OOTO" || input == "OOOT"){
                O = true;
            }
            unsigned found = input.find(".");
            if (found!=std::string::npos)
                empty = true;
        }
        if( !X && !O){
            for (int j =0 ; j <4 ;j++){
                if ((board[0][j] == 'X' && board[1][j] == 'X' && board[2][j] == 'X'&& board[3][j] == 'X')
                || (board[0][j] == 'T' && board[1][j] == 'X' && board[2][j] == 'X'&& board[3][j] == 'X')
                || (board[0][j] == 'X' && board[1][j] == 'T' && board[2][j] == 'X'&& board[3][j] == 'X')
                || (board[0][j] == 'X' && board[1][j] == 'X' && board[2][j] == 'T'&& board[3][j] == 'X')
                || (board[0][j] == 'X' && board[1][j] == 'X' && board[2][j] == 'X'&& board[3][j] == 'T')){
                    X = true;
                    break;
                }
                
                if ((board[0][j] == 'O' && board[1][j] == 'O' && board[2][j] == 'O'&& board[3][j] == 'O')
                || (board[0][j] == 'T' && board[1][j] == 'O' && board[2][j] == 'O'&& board[3][j] == 'O')
                || (board[0][j] == 'O' && board[1][j] == 'T' && board[2][j] == 'O'&& board[3][j] == 'O')
                || (board[0][j] == 'O' && board[1][j] == 'O' && board[2][j] == 'T'&& board[3][j] == 'O')
                || (board[0][j] == 'O' && board[1][j] == 'O' && board[2][j] == 'O'&& board[3][j] == 'T')){
                    O = true;
                    break;
                }
            }
        }
        
        if ((board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X'&& board[3][3] == 'X')
            || (board[0][0] == 'T' && board[1][1] == 'X' && board[2][2] == 'X'&& board[3][3] == 'X')
            || (board[0][0] == 'X' && board[1][1] == 'T' && board[2][2] == 'X'&& board[3][3] == 'X')
            || (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'T'&& board[3][3] == 'X')
            || (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X'&& board[3][3] == 'T')){
            X = true;
        }
        
        if ((board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O'&& board[3][3] == 'O')
            || (board[0][0] == 'T' && board[1][1] == 'O' && board[2][2] == 'O'&& board[3][3] == 'O')
            || (board[0][0] == 'O' && board[1][1] == 'T' && board[2][2] == 'O'&& board[3][3] == 'O')
            || (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'T'&& board[3][3] == 'O')
            || (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O'&& board[3][3] == 'T')){
            O = true;
        }
        
        if ((board[0][3] == 'X' && board[1][2] == 'X' && board[2][1] == 'X'&& board[3][0] == 'X')
            || (board[0][3] == 'T' && board[1][2] == 'X' && board[2][1] == 'X'&& board[3][0] == 'X')
            || (board[0][3] == 'X' && board[1][2] == 'T' && board[2][1] == 'X'&& board[3][0] == 'X')
            || (board[0][3] == 'X' && board[1][2] == 'X' && board[2][1] == 'T'&& board[3][0] == 'X')
            || (board[0][3] == 'X' && board[1][2] == 'X' && board[2][1] == 'X'&& board[3][0] == 'T')){
            X = true;
        }
        
        if ((board[0][3] == 'O' && board[1][2] == 'O' && board[2][1] == 'O'&& board[3][0] == 'O')
            || (board[0][3] == 'T' && board[1][2] == 'O' && board[2][1] == 'O'&& board[3][0] == 'O')
            || (board[0][3] == 'O' && board[1][2] == 'T' && board[2][1] == 'O'&& board[3][0] == 'O')
            || (board[0][3] == 'O' && board[1][2] == 'O' && board[2][1] == 'T'&& board[3][0] == 'O')
            || (board[0][3] == 'O' && board[1][2] == 'O' && board[2][1] == 'O'&& board[3][0] == 'T')){
            O = true;
        }
        
        int counter = i+1;
        if (X)
            outfile << "Case #"<<counter<<": X won\n";
        else if (O)
            outfile << "Case #"<<counter<<": O won\n";
        else if (!X && !O && empty)
            outfile << "Case #"<<counter<<": Game has not completed\n";
        else
            outfile << "Case #"<<counter<<": Draw\n";
        
        string temp;
        //infile >> temp;
        getline(infile, temp);
    }
	return 0;
}
