#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("ans.txt");

    int T;
    fin >> T;

    for (int i = 0; i < T; i++) {
        vector<vector<char> > rec(4, vector<char>(4));

        for (int x = 0; x < 4; x++) {
            for (int y = 0; y < 4; y++) {
                fin >> rec[x][y];
            }
        }

        bool flag1 = false;
        bool flag2 = false;
        bool finish = true;

        for (int x = 0; x < 4; x++) {
            int symbol1 = 0;
            int symbol2 = 0;
            bool special = false;
            for (int y = 0; y < 4; y++) {
                if (rec[x][y] == 'X') {
                    symbol1++;
                }
                if (rec[x][y] == 'O') {
                    symbol2++;
                }
                if (rec[x][y] == 'T') {
                    special = true;
                }
                if (rec[x][y] == '.') {
                    finish = false;
                }
            }
            if (symbol1 == 4 || (symbol1 == 3 && special)) {
                flag1 = true;
            }
            if (symbol2 == 4 || (symbol2 == 3 && special)) {
                flag2 = true;
            }
        }

        for (int y = 0; y < 4; y++) {
            int symbol1 = 0;
            int symbol2 = 0;
            bool special = false;
            for (int x = 0; x < 4; x++) {
                if (rec[x][y] == 'X') {
                    symbol1++;
                }
                if (rec[x][y] == 'O') {
                    symbol2++;
                }
                if (rec[x][y] == 'T') {
                    special = true;
                }
            }
            if (symbol1 == 4 || (symbol1 == 3 && special)) {
                flag1 = true;
            }
            if (symbol2 == 4 || (symbol2 == 3 && special)) {
                flag2 = true;
            }
        }

        int symbol1 = 0;
        int symbol2 = 0;
        bool special = false;

        for (int x = 0; x < 4; x++) {
            if (rec[x][x] == 'X') {
                symbol1++;
            }
            if (rec[x][x] == 'O') {
                symbol2++;
            }
            if (rec[x][x] == 'T') {
                special = true;
            }
        }
        if (symbol1 == 4 || (symbol1 == 3 && special)) {
            flag1 = true;
        }
        if (symbol2 == 4 || (symbol2 == 3 && special)) {
            flag2 = true;
        }

        symbol1 = 0;
        symbol2 = 0;
        special = false;

        for (int x = 0; x < 4; x++) {
            if (rec[x][3 - x] == 'X') {
                symbol1++;
            }
            if (rec[x][3 - x] == 'O') {
                symbol2++;
            }
            if (rec[x][3 - x] == 'T') {
                special = true;
            }
        }
        if (symbol1 == 4 || (symbol1 == 3 && special)) {
            flag1 = true;
        }
        if (symbol2 == 4 || (symbol2 == 3 && special)) {
            flag2 = true;
        }

        if (flag1 && !flag2) {
            fout << "Case #" << i + 1 << ": X won" << endl;
        }
        else if (!flag1 && flag2) {
            fout << "Case #" << i + 1 << ": O won" << endl;
        }
        else if (!finish) {
            fout << "Case #" << i + 1 << ": Game has not completed" << endl;
        }
        else{
            fout << "Case #" << i + 1 << ": Draw" << endl;
        }

    }
}
