/* 
 * File:   main.cpp
 * Author: mfatihuslu
 *
 * Created on April 13, 2013, 7:40 AM
 */

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
using namespace std;
#define AND &&
#define OR ||

fstream inputFile, outputFile, logFile;
int caseNumber;
int N,M;
int **board;

int printBoard(){
    
    for(int j=0;j<N;j++){
        for(int k=0;k<M;k++){
                
            logFile << board[j][k];
        }
        logFile << endl;
    }
    logFile << endl;
}

bool valueBoard(){
    
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
        
            int vertical = 1;
            int horizontal = 1;
            
            for(int k=0;k<M;k++){
                
                if(board[i][k] > board[i][j]){
                    
                    horizontal = 0;
                    break;
                }
            }
            for(int k=0;k<N;k++){
                
                if(board[k][j] > board[i][j]){
                    
                    vertical = 0;
                    break;
                }
            }
            if(horizontal == 0 and vertical == 0)
                return false;
        }
    }
    return true;
}

int main(int argc, char** argv) {

    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);
    logFile.open("log",ios::out);
    
    inputFile >> caseNumber;
    

    
    for(int i=1; i<=caseNumber; i++) {
        
        inputFile >> N >> M;
        
        board = new int*[N];
    
        for(int j=0;j<N;j++)
            board[j] = new int[M];
        
        for(int j=0;j<N;j++){
            for(int k=0;k<M;k++){
                
                inputFile >> board[j][k];
            }
        }
        printBoard();
        
        outputFile << "Case #"<<i<<": ";
        bool result = valueBoard();
        
        if(result == true)
            outputFile << "YES";
        else
            outputFile << "NO";
        
        outputFile << endl;
    }
    return 0;
}

