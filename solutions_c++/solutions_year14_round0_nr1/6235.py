/*******************************************\
*                                           *
*   Magic Trick                             *
*   CodeJam 2014                            *
*   Rafael Medina (MedinaSoft)              *
*                                           *
\*******************************************/

#include <iostream>
#include <fstream>
using namespace std;

int main () {
    int LINE = 1, TOT, N;
    int resp[2], table[3][4], pos, nil;
    for (scanf ("%d", &TOT); LINE <= TOT; LINE++)  {
        //capture the responses
        for (int i = 0; i < 2; i++) {
            scanf ("%d", &pos);
            for (int j = 1; j <= 4; j++) {
                if (pos == j) {
                    scanf ("%d %d %d %d", &table[i][0], &table[i][1], &table[i][2], &table[i][3]);
                }
                else {
                    scanf ("%d %d %d %d", &table[2][0], &table[2][1], &table[2][2], &table[2][3]);
                }
            }

        }
        //figure out the result
        int cnt = 0, number;
        for (int i = 0; i < 4; i++) {
            for(int j =0; j < 4; j++) {
                if (table[0][i] == table[1][j]) { cnt++; number = table[0][i]; }
            }
        }
        cout << "Case #" << LINE << ": ";
        if (cnt == 1) {
            cout << number;
        }
        else if (cnt == 0) {
            cout << "Volunteer cheated!";
        }
        else {
            cout << "Bad magician!";
        }
        cout << endl;

    }
    return 0;

}
