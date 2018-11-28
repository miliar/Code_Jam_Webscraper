/* 
 * File:   main.cpp
 * Author: kingGreed
 *
 * Created on 13 avril 2013, 01:05
 */

#include <cstdlib>
#include <string>
#include <iostream>

char lines [4][4];

using namespace std;

bool hasWonOnColum(int x) {
    int X = 0;
    int O = 0;
    int T = 0;
    for (int y = 0; y < 4; y++) {
        if(lines[x][y] == 'X') { X++; }
        else if(lines[x][y] == 'O') { O++; }
        else if(lines[x][y] == 'T') { T++; }
    }
    
    if((X == 3 && T == 1) || (X == 4) || (O == 3 && T == 1) ||(O == 4)) { return true; }
    return false;
}
bool hasWonOnLine(int y) {
    int X = 0;
    int O = 0;
    int T = 0;
    for (int x = 0; x < 4; x++) {
        if(lines[x][y] == 'X') { X++; }
        else if(lines[x][y] == 'O') { O++; }
        else if(lines[x][y] == 'T') { T++; }
    }
    if((X == 3 && T == 1) || (X == 4) || (O == 3 && T == 1) ||(O == 4)) { return true; }
    return false;
}

int main(int argc, char** argv) {
    int testCases;
    
    cin >> testCases;
    for (int i = 0; i < testCases; i++) {
        for (int x = 0; x < 4; x++) { for (int y = 0; y < 4; y++) { cin >> lines[x][y]; } }
        
        bool completed = true;

        for (int j = 0; j < 4; j++) { for (int k = 0; k < 4; k++) { if (lines[k][j] == '.') { completed = false; } } }
        
        int Xs = 0, Os = 0, Ts = 0;
        for (int k = 0; k < 4; k++) {
            if(lines[k][k] == 'X') { Xs++; }
            else if(lines[k][k] == 'O') { Os++; }
            else if(lines[k][k] == 'T') { Ts++; }
        }
        
        if ((Xs == 3 && Ts == 1) || (Xs == 4))      { cout << "Case #" << (i+1) << ": X won" << endl; continue; }
        else if ((Os == 3 && Ts == 1) ||(Os == 4))  { cout << "Case #" << (i+1) << ": O won" << endl; continue; }

        Xs = 0, Os = 0, Ts = 0;
        for (int k = 0; k < 4; k++) {
            if(lines[k][3 - k] == 'X') { Xs++; }
            else if(lines[k][3 - k] == 'O') { Os++; }
            else if(lines[k][3 - k] == 'T') { Ts++; }
        }
        if ((Xs == 3 && Ts == 1) || (Xs == 4))      { cout << "Case #" << (i+1) << ": X won" << endl; continue; }
        else if ((Os == 3 && Ts == 1) ||(Os == 4)) { cout << "Case #" << (i+1) << ": O won" << endl; continue; }
        
        bool won = false;
        for (int x = 0; x < 4 && !won; x++) {
            for (int y = 0; y < 4 && !won; y++) {
                if(hasWonOnColum(x)) {
                    won = true;
                    if(lines[x][0] == 'T'){ cout << "Case #" << (i+1) << ": " << lines[x][1] << " won" << endl; }
                    else { cout << "Case #" << (i+1) << ": " << lines[x][0] << " won" << endl; }
                } else if(hasWonOnLine(y)) {
                    won = true;
                    if(lines[0][y] == 'T'){ cout << "Case #" << (i+1) << ": " << lines[1][y] << " won" << endl; }
                    else { cout << "Case #" << (i+1) << ": " << lines[0][y] << " won" << endl; }
                }
            }
        }
        if(!won) {
            if (completed) { cout << "Case #" << (i+1) << ": Draw" << endl; }
            else { cout << "Case #" << (i+1) << ": Game has not completed" << endl; }
        }


        
    }

    
    return 0;
}

