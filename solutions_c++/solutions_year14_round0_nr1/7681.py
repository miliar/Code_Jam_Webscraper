#include <iostream>
#include <cstdlib>
#include <cmath>
#include <fstream>

using namespace std;

int main() {
    int t, i, j, ans1, ans2, z=1, x, num;
    int board1[4][4], board2[4][4];
    ofstream fileoutput("data.txt");

    cin >> t;

    while (t--) {
        cin >> ans1;
        for (i=0;i<4;i++) {
            for (j=0;j<4;j++) {
                cin >> board1[i][j];
            }
        }

        cin >> ans2;
        for (i=0;i<4;i++) {
            for (j=0;j<4;j++) {
                cin >> board2[i][j];
            }
        }

        x = 0;
        num = 0;
        for (i=0;i<4;i++) {
            for (j=0;j<4;j++) {
                if (board1[ans1-1][i] == board2[ans2-1][j]) {
                    x++;
                    num = board1[ans1-1][i];
                }
            }
        }

        fileoutput << "Case #" << z++ << ": ";

        if (x==1) {
            fileoutput << num;
        } else if (x>1) {
            fileoutput << "Bad Magician!";
        } else {
            fileoutput << "Volunteer cheated!";
        }
        fileoutput << "\n";
    }
    fileoutput.close();
    return 0;
}
