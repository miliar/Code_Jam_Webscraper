#include <iostream>
#include <string>
#include <cstdio>
#include <list>
#include <vector>

using namespace std;

int main ()
{
    int testCaseNumber;
    string boardLine;
    
    cin >> testCaseNumber;
    
    char board[4][4];
    
    int symbolNumber[20];   // 0 - line1X, line2X, line3X, line4X, line1O, line2O, line3O, line4O - 7
                            // 8 - column1X, column2X, column3X, column4X, column1O, column2O, column3O, column4O - 15
                            // 16 - diagTopBotX, diagBotTopX, diagTopBotO, diagBotTopO - 19

    int emptyCells;

    for(int i = 0 ; i < testCaseNumber; i++) {
    
        emptyCells = 16;
        
        for( int x = 0 ; x < 20 ; x++)
            symbolNumber[x] = 0;
        
        for(int line = 0; line < 4 ; line++) {
            boardLine.clear();
            cin >> boardLine;
            for(int column = 0; column < 4 ; column++) {
                board[line][column] = boardLine[column];
                if(board[line][column] == 'X') {
                    emptyCells--;
                    symbolNumber[line]++;
                    symbolNumber[column+8]++;
                    if(line == 0) {
                        if(column == 0)
                            symbolNumber[16]++;
                        else if(column == 3)
                            symbolNumber[17]++;
                    } else if(line == 1) {
                        if(column == 1)
                            symbolNumber[16]++;
                        else if(column == 2)
                            symbolNumber[17]++;
                    } else if(line == 2) {
                        if(column == 1)
                            symbolNumber[17]++;
                        else if(column == 2)
                            symbolNumber[16]++;
                    } else if(line == 3) {
                        if(column == 0)
                            symbolNumber[17]++;
                        else if(column == 3)
                            symbolNumber[16]++;
                    }
                    
                } else if(board[line][column] == 'O') {
                    emptyCells--;
                    symbolNumber[line+4]++;
                    symbolNumber[column+12]++;
                    if(line == 0) {
                        if(column == 0)
                            symbolNumber[18]++;
                        else if(column == 3)
                            symbolNumber[19]++;
                    } else if(line == 1) {
                        if(column == 1)
                            symbolNumber[18]++;
                        else if(column == 2)
                            symbolNumber[19]++;
                    } else if(line == 2) {
                        if(column == 1)
                            symbolNumber[19]++;
                        else if(column == 2)
                            symbolNumber[18]++;
                    } else if(line == 3) {
                        if(column == 0)
                            symbolNumber[19]++;
                        else if(column == 3)
                            symbolNumber[18]++;
                    }
                } else if(board[line][column] == 'T') {
                    emptyCells--;
                    symbolNumber[line]++;
                    symbolNumber[line+4]++;
                    symbolNumber[column+8]++;
                    symbolNumber[column+12]++;
                    if(line == 0) {
                        if(column == 0) {
                            symbolNumber[16]++;
                            symbolNumber[18]++;
                        } else if(column == 3) {
                            symbolNumber[17]++;
                            symbolNumber[19]++;
                        }
                    } else if(line == 1) {
                        if(column == 1) {
                            symbolNumber[16]++;
                            symbolNumber[18]++;
                        } else if(column == 2) {
                            symbolNumber[17]++;
                            symbolNumber[19]++;
                        }
                    } else if(line == 2) {
                        if(column == 1) {
                            symbolNumber[17]++;
                            symbolNumber[19]++;
                        } else if(column == 2) {
                            symbolNumber[16]++;
                            symbolNumber[18]++;
                        }
                    } else if(line == 3) {
                        if(column == 0) {
                            symbolNumber[17]++;
                            symbolNumber[19]++;
                        } else if(column == 3) {
                            symbolNumber[16]++;
                            symbolNumber[18]++;
                        }
                    }
                }
                
            }
        }
        
        bool gameWinner = false;
        
        for( int x = 0 ; x < 20 ; x++) {
        
            if(symbolNumber[x] == 4) {
            
                if((x >= 0 && x <= 3) || (x >= 8 && x <= 11) || (x >= 16 && x <= 17))
                    cout << "Case #" << i+1 << ": X won" << endl;
                else
                    cout << "Case #" << i+1 << ": O won" << endl;
            
                gameWinner = true;
                break;
            }

        }
        if (gameWinner == false) {
            if(emptyCells == 0)
                cout << "Case #" << i+1 << ": Draw" << endl;
            else
                cout << "Case #" << i+1 << ": Game has not completed" << endl;
        }
    
    }


}
