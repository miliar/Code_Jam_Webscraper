#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  string line;
  ifstream infile ("A-large.in");
  ofstream outfile ("A-large.out");
  if (infile.is_open())
  {
    getline (infile,line);
    int num = atoi(line.c_str());
    for (int i = 0; i < num; i++) {
        char array[5][5];
        for (int j = 0; j < 4; j++) {
            getline (infile,line);
            array[j][0] = line.c_str()[0];
            array[j][1] = line.c_str()[1];
            array[j][2] = line.c_str()[2];
            array[j][3] = line.c_str()[3];
            array[j][4] = '\0';
//            cout << array[j] << endl;
        }
//        cout << endl;
        getline (infile,line);
        outfile << "Case #" << i+1 << ": ";
        int X[5][5];
        int O[5][5];
//        cout << endl;
        for (int n = 0; n < 4; n++) {
            for (int m = 0; m < 4; m++) {
//                cout << array[n][m];
                if ((array[n][m] == 'X') || (array[n][m] == 'T')) {
                   X[n][m] = 1;
                } else {
                   X[n][m] = 0;
                }
                if ((array[n][m] == 'O') || (array[n][m] == 'T')) {
                   O[n][m] = 1;
                } else {
                   O[n][m] = 0;
                }
            }
            X[n][4] = '\0';
            O[n][4] = '\0';
//            cout << endl;
        }
        if ( (X[0][0] && X[0][1] && X[0][2] && X[0][3]) ||
             (X[1][0] && X[1][1] && X[1][2] && X[1][3]) ||
             (X[2][0] && X[2][1] && X[2][2] && X[2][3]) ||
             (X[3][0] && X[3][1] && X[3][2] && X[3][3]) ||
             (X[0][0] && X[1][0] && X[2][0] && X[3][0]) ||
             (X[0][1] && X[1][1] && X[2][1] && X[3][1]) ||
             (X[0][2] && X[1][2] && X[2][2] && X[3][2]) ||
             (X[0][3] && X[1][3] && X[2][3] && X[3][3]) ||
             (X[0][0] && X[1][1] && X[2][2] && X[3][3]) ||
             (X[0][3] && X[1][2] && X[2][1] && X[3][0]) ) {
            outfile << "X won";
        } else if ( (O[0][0] && O[0][1] && O[0][2] && O[0][3]) ||
                    (O[1][0] && O[1][1] && O[1][2] && O[1][3]) ||
                    (O[2][0] && O[2][1] && O[2][2] && O[2][3]) ||
                    (O[3][0] && O[3][1] && O[3][2] && O[3][3]) ||
                    (O[0][0] && O[1][0] && O[2][0] && O[3][0]) ||
                    (O[0][1] && O[1][1] && O[2][1] && O[3][1]) ||
                    (O[0][2] && O[1][2] && O[2][2] && O[3][2]) ||
                    (O[0][3] && O[1][3] && O[2][3] && O[3][3]) ||
                    (O[0][0] && O[1][1] && O[2][2] && O[3][3]) ||
                    (O[0][3] && O[1][2] && O[2][1] && O[3][0]) ) {
            outfile << "O won";
        } else if (array[0][0] == '.' ||
                   array[0][1] == '.' ||
                   array[0][2] == '.' ||
                   array[0][3] == '.' ||
                   array[1][0] == '.' ||
                   array[1][1] == '.' ||
                   array[1][2] == '.' ||
                   array[1][3] == '.' ||
                   array[2][0] == '.' ||
                   array[2][1] == '.' ||
                   array[2][2] == '.' ||
                   array[2][3] == '.' ||
                   array[3][0] == '.' ||
                   array[3][1] == '.' ||
                   array[3][2] == '.' ||
                   array[3][3] == '.') {
           outfile << "Game has not completed";
        } else {
           outfile << "Draw";
        }
        if (i+1 != num) {
           outfile << "\n";
        }
    }
  }

  else cout << "Unable to open file"; 
  system("PAUSE");
  return 0;
}
