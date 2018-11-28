#include <iostream>

using namespace std;
static int s_i = 1;

void solveProblem() {
    int firstAns, secondAns;
    int fMat[4][4];
    int sMat[4][4];

    cin >> firstAns;
    for (int i = 0; i < 4; i ++) {
        for (int j = 0; j < 4; j ++) {
            cin >> fMat[i][j];
        }
    }
    cin >> secondAns;
    for (int i = 0; i < 4; i ++) {
        for (int j = 0; j < 4; j ++) {
            cin >> sMat[i][j];
        }
    }
    int *fLine = fMat[firstAns - 1];
    int *sLine = sMat[secondAns - 1];

    int n = 0;
    int g;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (fLine[i] == sLine[j]) {
                n ++;
                g = fLine[i];
            }
        }
    }

    cout << "Case #" << s_i << ": ";
    switch (n) {
    case 0: 
        cout << "Volunteer cheated!";
        break;
    case 1: 
        cout << g;
        break;
    default:
        cout << "Bad magician!";
    }

}

int main () {
    int n;
    cin >> n;
    while (n --) {
        solveProblem();
        s_i ++;
        if (n != 0) {
            cout << endl;
        }
    }
}