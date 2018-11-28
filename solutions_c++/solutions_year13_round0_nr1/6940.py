#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>

using namespace std;

int t;
string s;

int a[4][4];
bool finished = true;

int getInt (char c) {
    if (c =='X') 
        return 1;
    if (c == 'T')
        return 2;
    if (c == 'O')
        return -1;
    if (c == '.')
        return 0;
}

void checkDiagonals(bool & O, bool & X) {
    bool specialL = false, specialR = false;
    int l = 0, r = 0;
    for (int i = 0; i < 4; i ++) {
        if (a[i][i] == 2) {
            specialL = true;
        } else
            l += a[i][i];
        if (a[i][3-i] == 2) {
            specialR = true;
        } else
            r += a[i][3-i];
    }
    if ((abs(l) == 4 || (abs(l) == 3 && specialL))){
        if (l < 0) {
//            cout << "left Diagonal: O wins" << endl;
            O = true;
        }
        else {
            X = true;
//            cout << "left Diagonal: X wins" << endl;
        }
    } else if ((abs(r) == 4 || (abs(r) == 3 && specialR))) {
        if (r < 0) {
            O = true;
//            cout << "right Diagonal: O wins" << endl;
        }
        else {
            X = true;
//            cout << "right Diagonal: X wins" << endl;
        }
    }
}

int getState() {
    bool O = false, X = false;
    for (int i = 0; i < 4; i ++) {
        bool specialVert = false;
        bool specialHor = false;
        int vertSum = 0, horSum = 0;
        for (int j = 0; j < 4; j ++) {
            if (a[i][j] == 2)
                specialHor = true;
            else
                horSum += a[i][j];
            if (a[j][i] == 2)
                specialVert = true;
            else
                vertSum += a[j][i];
        }
  //      cout << i+1 << ": vertSum=" << vertSum << " horSum=" << horSum << " specialHor=" << specialHor << " specialVert=" << specialVert <<  endl;
        if ((abs(horSum) == 4 || (abs(horSum) == 3 && specialHor))){
            if (horSum < 0) {
                O = true;
 //               cout << "horizonatal: " << i+1 << " O wins" << endl;
            }
            else {
                X = true;
//                cout << "horizonatal: " << i+1 << " X wins" << endl;
            }
        } else if ((abs(vertSum) == 4 || (abs(vertSum) == 3 && specialVert))) {
            if (vertSum < 0) {
                O = true;
//                cout << "vertical: " << i+1 << " O wins" << endl;
            }
            else {
                X = true;
//                cout << "vertical: " << i+1 << " X wins" << endl;
            }
        }
    }
    checkDiagonals(O, X);
    if (!O && !X)
        return finished?2:0;
    if (O)
        return -1;
    if (X)
        return 1;
}

string getString(int state) {
    switch (state) {
        case -1:
            return "O won";
        case 1:
            return "X won";
        case 0:
            return "Game has not completed";
        case 2:
            return "Draw";
    }
    return "";
}

void output(int cs, int state) {
    cout << "Case #" << cs << ": " << getString(state) << endl;
}

int main () {
    scanf("%d\n", &t);
    
    for (int i = 0; i < t; i ++ ){
        finished = true;
        for (int j = 0; j < 4; j ++) {
            getline(cin, s);
            for (int k = 0; k < 4; k ++) {
                if (s[k] == '.') {
                    finished = false;
                }
                a[j][k] = getInt(s[k]);
//                cout << a[j][k];
            }
//            cout << endl;
        }
//        cout << finished << endl;
        output(i+1, getState());
        getline (cin, s);
    }

    return 0;
}
