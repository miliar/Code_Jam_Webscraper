#include <iostream>
#include <cstdio>
using namespace std;

void algo() {
    static int caseNo = 0;
    int dot = 0;
    int i, j, flag = 0;

    char a, b, c, d;
    char winner;
    char brd1[4][4];

    for(i=0; i < 4; i++){
        cin >> a >> b >> c >> d;
        if(a == '.' || b == '.' || c == '.' || d == '.')
            dot = 1;

        brd1[i][0] = a;
        brd1[i][1] = b;
        brd1[i][2] = c;
        brd1[i][3] = d;
        }

    for(i=0; i<4; i++) {
        if(((brd1[i][0] == brd1[i][1]) && (brd1[i][1] == brd1[i][2]) && ((brd1[i][2] == brd1[i][3]) || brd1[i][3] == 'T')) ||
           ((brd1[i][0] == brd1[i][1]) && (brd1[i][1] == brd1[i][3]) && ((brd1[i][3] == brd1[i][2]) || brd1[i][2] == 'T')) ||
           ((brd1[i][0] == brd1[i][2]) && (brd1[i][2] == brd1[i][3]) && ((brd1[i][2] == brd1[i][1]) || brd1[i][1] == 'T')) ||
           ((brd1[i][1] == brd1[i][2]) && (brd1[i][2] == brd1[i][3]) && ((brd1[i][1] == brd1[i][0]) || brd1[i][0] == 'T')) ) {
                if(brd1[i][0] == '.')
                    continue;
                if(brd1[i][0] == 'T')
                    winner = brd1[i][1];
               else
                    winner = brd1[i][0];
                cout << "Case #" << ++caseNo <<": "<< winner<< " won" << endl;
                return;
        }
    }

    for(j=0; j<4; j++) {
        if(((brd1[0][j] == brd1[1][j]) && (brd1[1][j] == brd1[2][j]) && ((brd1[2][j] == brd1[3][j]) || brd1[3][j] == 'T')) ||
           ((brd1[0][j] == brd1[1][j]) && (brd1[1][j] == brd1[3][j]) && ((brd1[3][j] == brd1[2][j]) || brd1[2][j] == 'T')) ||
           ((brd1[0][j] == brd1[2][j]) && (brd1[2][j] == brd1[3][j]) && ((brd1[2][j] == brd1[1][j]) || brd1[1][j] == 'T')) ||
           ((brd1[1][j] == brd1[2][j]) && (brd1[2][j] == brd1[3][j]) && ((brd1[1][j] == brd1[0][j]) || brd1[0][j] == 'T')) ) {
                if(brd1[0][j] == '.')
                    continue;
                if(brd1[0][j] == 'T')
                    winner = brd1[1][j];
               else
                    winner = brd1[0][j];
                cout << "Case #" << ++caseNo <<": "<< winner << " won" << endl;
                return;
        }
    }


    if(((brd1[0][0] == brd1[1][1]) && (brd1[1][1] == brd1[2][2]) && ((brd1[2][2] == brd1[3][3]) || brd1[3][2] == 'T')) ||
       ((brd1[0][0] == brd1[1][1]) && (brd1[1][1] == brd1[3][3]) && ((brd1[3][3] == brd1[2][2]) || brd1[2][2] == 'T')) ||
       ((brd1[0][0] == brd1[2][2]) && (brd1[2][2] == brd1[3][3]) && ((brd1[2][2] == brd1[1][1]) || brd1[1][1] == 'T')) ||
       ((brd1[1][1] == brd1[2][2]) && (brd1[2][2] == brd1[3][3]) && ((brd1[1][1] == brd1[0][0]) || brd1[0][0] == 'T')) ) {
           if(brd1[0][0] == '.')
                goto label1;

           else if(brd1[0][0] == 'T')
                winner = brd1[1][1];
           else
                winner = brd1[0][0];
            cout << "Case #" << ++caseNo <<": "<< winner << " won" << endl;
            return;
    }

    label1:
    if(((brd1[0][3] == brd1[1][2]) && (brd1[1][2] == brd1[2][1]) && ((brd1[2][1] == brd1[3][0]) || brd1[3][0] == 'T')) ||
       ((brd1[0][3] == brd1[1][2]) && (brd1[1][2] == brd1[3][0]) && ((brd1[3][0] == brd1[2][1]) || brd1[2][1] == 'T')) ||
       ((brd1[0][3] == brd1[2][1]) && (brd1[2][1] == brd1[3][0]) && ((brd1[2][1] == brd1[1][2]) || brd1[1][2] == 'T')) ||
       ((brd1[1][2] == brd1[2][1]) && (brd1[2][1] == brd1[3][0]) && ((brd1[1][2] == brd1[0][3]) || brd1[0][3] == 'T')) ) {
           if(brd1[0][3] == '.')
                goto label2;
           else if(brd1[0][3] == 'T')
                winner = brd1[1][2];
           else
                winner = brd1[0][3];
            cout << "Case #" << ++caseNo <<": "<< winner << " won" << endl;
            return;
    }
    label2:
    if(dot) {
        cout << "Case #" << ++caseNo <<": "<< "Game has not completed" << endl;
        return;
    }
    cout << "Case #" << ++caseNo <<": "<< "Draw" << endl;

}

int main() {
    int nCases;
    cin >> nCases;
    for(int i=0; i < nCases; i++)
        algo();
    return 0;
}
