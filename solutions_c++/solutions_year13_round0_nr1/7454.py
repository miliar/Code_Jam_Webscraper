#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    int T; //test cases
    scanf("%d",&T);
    
    string xwon = "X won";
    string owon = "O won";
    string draw = "Draw";
    string incomplete = "Game has not completed";
    string board[4];
    
    for (int t=1; t<=T; t++) {        
        vector<int> rowX(4,0);
        vector<int> rowO(4,0);
        vector<int> colX(4,0);
        vector<int> colO(4,0);
        vector<int> diagX(2,0);
        vector<int> diagO(2,0);
        bool isDraw = true;       
        
        bool foundT = false;
        for (int i=0; i<4; i++) {
            cin >> board[i];
            if (foundT) {
                continue;
            }
            
            for (int j=0; j<4; j++) {
                if (board[i][j] == 'T') {
                    foundT = true;
                    rowX[i]++;
                    colX[j]++;
                    rowO[i]++;
                    colO[j]++;
                    if (i == j) {
                        diagX[0]++;
                        diagO[0]++;
                    } else if (i+j == 3) {
                        diagX[1]++;
                        diagO[1]++;
                    }
                }
            }
        }
        
        printf("Case #%d: ", t);
        for (int r=0; r<4; r++) {
            for (int c=0; c<4; c++) {
                char sym = board[r][c];
                if (sym == 'X') {
                    if (rowX[r] == 3 || colX[c] == 3 || (r == c && diagX[0] == 3) || (r+c == 3 && diagX[1] == 3)) {
                        cout << xwon << endl;
                        goto done;
                    } else {
                        rowX[r]++;
                        colX[c]++;
                        if (r == c) {
                            diagX[0]++;
                        }
                        if (r+c == 3) {
                            diagX[1]++;
                        }
                    }                        
                } else if (sym == 'O') {
                    if (rowO[r] == 3 || colO[c] == 3 || (r == c && diagO[0] == 3) || (r+c == 3 && diagO[1] == 3)) {
                        cout << owon << endl;
                        goto done;
                    } else {
                        rowO[r]++;
                        colO[c]++;
                        if (r == c) {
                            diagO[0]++;
                        }
                        if (r+c == 3) {
                            diagO[1]++;
                        }
                    }
                } else if (sym == '.') {
                    //do nothing
                    isDraw = false;
                }
            }
        }
        
        if (isDraw) {
            cout << draw << endl;
        } else {
            cout << incomplete << endl;
        }
        
        done:;    
    }
    
    return 0;
}
