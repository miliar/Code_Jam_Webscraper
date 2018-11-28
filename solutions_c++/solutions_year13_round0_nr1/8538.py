#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

const int numSquares=4;

bool CheckPlayer(char board[][numSquares], char player);


int main (int argc, const char * argv[])
{
    string input;
    int T, nTest, i, j;
    char board[numSquares][numSquares];
    bool win, draw;
    
    ifstream inputFile("/Users/kbrigham/A-small-attempt0.in");
    ofstream outputFile("/Users/kbrigham/output.txt");
    
    if ( inputFile.is_open() ){
        getline(inputFile, input);
        stringstream(input) >> T;   // Number of test cases
        
        // For each test case
        for (nTest=0; nTest<T; nTest++){
            outputFile << "Case #" << nTest+1 << ": ";
            cout << "Case #" << nTest+1 << ": ";
            
            for (i=0; i<numSquares; i++){
                for (j=0; j<numSquares; j++){
                    board[i][j] = inputFile.get();
                }
                inputFile.get();
            }
            inputFile.get();
            
            //Print board
//            for (i=0; i<numSquares; i++){
//                for (j=0; j<numSquares; j++){
//                    cout << board[i][j];
//                }
//                cout << endl;
//            }
            
            win = CheckPlayer(board, 'O');
            if ( win ){
                outputFile << "O won" << endl;
                cout << "O won" << endl;
                continue;
            }
            
            win = CheckPlayer(board, 'X');
            if ( win ){
                outputFile << "X won" << endl;
                cout << "X won" << endl;
                continue;
            }
            
            draw=true;
            for (i=0; i<numSquares; i++){
                for (j=0; j<numSquares; j++){
                    if ( board[i][j] == '.' ){
                        draw = false;
                        break;
                    }
                }
                if ( draw )
                    break;
            }
            
            if ( draw ){
                outputFile << "Draw" << endl;
                cout << "Draw" << endl;
            }
            else{
                outputFile << "Game has not completed" << endl;
                cout << "Game has not completed" << endl;
            }
        }        
    }
    else cout << "Unable to open file." << endl;
    
    
    outputFile.close();
    
    return 0;
}

bool CheckPlayer(char board[][numSquares], char player){
    bool win=true;
    int i, j;
    
    //Check rows
    for (i=0; i<numSquares; i++){
        win=true;
        for (j=0; j<numSquares; j++){
            win = win && ( board[i][j]==player ||  board[i][j]=='T' );
        }
        if ( win ){ return win; }
    }
    
    //Check cols
    for (j=0; j<numSquares; j++){
        win=true;
        for (i=0; i<numSquares; i++){
            win = win && ( board[i][j]==player ||  board[i][j]=='T' );
        }
        if ( win ){ return win; }
    }
    
    //Check diag right
    win=true;
    for (i=0; i<numSquares; i++){
        win = win && ( board[i][i]==player ||  board[i][i]=='T' );
    }
    if ( win ){ return win; }
    
    //Check diag left
    win=true;
    for (i=0; i<numSquares; i++){
        win = win && ( board[i][numSquares-i-1]==player ||  board[i][numSquares-i-1]=='T' );
    }
    if ( win ){ return win; }
    
    return false;
}
