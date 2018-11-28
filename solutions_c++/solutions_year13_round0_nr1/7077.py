#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void){
    char table[4][4];
    char *count;
    string temp;
    ifstream inputFile;
    ofstream outputFile;
    int xLine;
    int oLine;
    int xRow;
    int oRow;
    int caseNum;
    bool gameComplete;
    bool winner;

    caseNum = 1;
    inputFile.open("input.txt");
    outputFile.open("output.txt");
    getline(inputFile,temp);
    count = new char[temp.length()];
    for(unsigned int i=0;i<temp.length();i++){
        count[i] = temp.at(i);
    }

    for(int i=0;i<atoi(count);i++){
        gameComplete = true;
        winner = false;

        for(int j=0;j<4;j++){
            getline(inputFile,temp);
            for(int k=0;k<4;k++){
                table[j][k] = temp.at(k);
                if(temp.at(k) == '.'){gameComplete = false;}
            }
        }
        getline(inputFile,temp);

        for(int j=0;j<4;j++){
            xLine = 0;
            oLine = 0;
            xRow = 0;
            oRow = 0;
            for(int k=0;k<4;k++){
                if(table[j][k] == 'X'){xLine++;}
                else if(table[j][k] == 'O'){oLine++;}
                else if(table[j][k] == 'T'){xLine++;oLine++;}

                if(table[k][j] == 'X'){xRow++;}
                else if(table[k][j] == 'O'){oRow++;}
                else if(table[k][j] == 'T'){xRow++;oRow++;}
            }

            if(xLine == 4 || xRow == 4){
                winner = true;
                outputFile << "Case #" << caseNum << ": X won" << endl;
                cout << "Case #" << caseNum++ << ": X won" << endl;
                break;
            }else if(oLine == 4 || oRow == 4){
                winner = true;
                outputFile << "Case #" << caseNum << ": O won" << endl;
                cout << "Case #" << caseNum++ << ": O won" << endl;
                break;
            }
        }

        if(!winner){
            int xLeftDiagonal = 0;
            int xRightDiagonal = 0;
            int oLeftDiagonal = 0;
            int oRightDiagonal = 0;

            if(table[0][0] == 'X'){xLeftDiagonal++;}
            else if(table[0][0] == 'O'){oLeftDiagonal++;}
            else if(table[0][0] == 'T'){oLeftDiagonal++;xLeftDiagonal++;}
            if(table[1][1] == 'X'){xLeftDiagonal++;}
            else if(table[1][1] == 'O'){oLeftDiagonal++;}
            else if(table[1][1] == 'T'){oLeftDiagonal++;xLeftDiagonal++;}
            if(table[2][2] == 'X'){xLeftDiagonal++;}
            else if(table[2][2] == 'O'){oLeftDiagonal++;}
            else if(table[2][2] == 'T'){oLeftDiagonal++;xLeftDiagonal++;}
            if(table[3][3] == 'X'){xLeftDiagonal++;}
            else if(table[3][3] == 'O'){oLeftDiagonal++;}
            else if(table[3][3] == 'T'){oLeftDiagonal++;xLeftDiagonal++;}

            if(table[3][0] == 'X'){xRightDiagonal++;}
            else if(table[3][0] == 'O'){oRightDiagonal++;}
            else if(table[3][0] == 'T'){oRightDiagonal++;xRightDiagonal++;}
            if(table[2][1] == 'X'){xRightDiagonal++;}
            else if(table[2][1] == 'O'){oRightDiagonal++;}
            else if(table[2][1] == 'T'){oRightDiagonal++;xRightDiagonal++;}
            if(table[1][2] == 'X'){xRightDiagonal++;}
            else if(table[1][2] == 'O'){oRightDiagonal++;}
            else if(table[1][2] == 'T'){oRightDiagonal++;xRightDiagonal++;}
            if(table[0][3] == 'X'){xRightDiagonal++;}
            else if(table[0][3] == 'O'){oRightDiagonal++;}
            else if(table[0][3] == 'T'){oRightDiagonal++;xRightDiagonal++;}

            if(xLeftDiagonal == 4 || xRightDiagonal == 4){
                outputFile << "Case #" << caseNum << ": X won" << endl;
                cout << "Case #" << caseNum++ << ": X won" << endl;
            }else if(oLeftDiagonal == 4 || oRightDiagonal == 4){
                outputFile << "Case #" << caseNum << ": O won" << endl;
                cout << "Case #" << caseNum++ << ": O won" << endl;
            }else{
                if(gameComplete){
                    outputFile << "Case #" << caseNum << ": Draw" << endl;
                    cout << "Case #" << caseNum++ << ": Draw" << endl;
                }else{
                    outputFile << "Case #" << caseNum << ": Game has not completed" << endl;
                    cout << "Case #" << caseNum++ << ": Game has not completed" << endl;
                }
            }
        }
    }

    inputFile.close();
    outputFile.close();
    return 0;
}
