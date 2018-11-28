#include <iostream>
#include <stdio.h>
using namespace std;


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n, k1, k2, m1[4][4], m2[4][4], Result, countResult = 0, isBreak = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> k1;
        for (int j = 0; j < 4; j++) {
            for (int f = 0; f < 4; f++) {
                cin >> m1[j][f];
            }

        }
        cin >> k2;
        for (int j = 0; j < 4; j++) {
            for (int f = 0; f < 4; f++) {
                cin >> m2[j][f];
            }

        }
        for (int j = 0; j < 4; j++) {
            for (int f = 0; f < 4; f++) {
              //  cout << m1[k1-1][j] << " " << m2[k2-1][f] << endl;
                if (m1[k1-1][j] == m2[k2-1][f]) {countResult++; Result = m1[k1-1][j];}
                if (countResult > 1) {cout << "Case #" << i + 1 << ':' << " Bad magician!" << endl; isBreak = 1; break;}
            }
            if (isBreak) {break;}
        }

        if (countResult == 0) cout << "Case #" << i + 1 << ':' << " Volunteer cheated!" << endl;
        else if (isBreak == 0) cout << "Case #" << i + 1 << ':' << " " << Result << endl;
        isBreak = 0; countResult = 0;
    }


    return 0;
}
