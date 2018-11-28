/*
 * .cpp -- Sergio Gonzalez
 */

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <array>
#include <unordered_set>

#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace std;

typedef unsigned long ulong;

const ulong kMaxLineSize = 1 << 20;

bool won = false;

void check_line(char *line) {
    if (won) return;
    // cout << "======" << endl;
    bool t = false;
    int c_x = 0;
    int c_o = 0;
    for(int i =0; i < 4; i++) {
        char c = line[i];
        // cout << "c: " << c << endl;
        if (c == 'X') {
            c_x++;
        }
        if (c == 'O') {
            c_o++;
        }
        if (c == 'T') {
            t = true;
        }
    }
    if ((c_o == 3 && t) || c_o == 4) {
        cout << "O won\n";
        won = true;
    }
    if ((c_x == 3 && t) || c_x == 4) {
        cout << "X won\n";
        won = true;
    }
}

int main(int argc, char const *argv[]) {
    FILE *file = fopen("in", "r");
    if(!file) {
        printf("No file\n");
        exit(-1);
    }
    char str[kMaxLineSize];

    ulong numlines = 0;
    vector<string> lines;

    while (fgets(str, kMaxLineSize, file)) {
        lines.push_back(string(str));
        numlines++;
    }

    ulong numcases = atoi(lines[0].c_str());
    int ncase = 1;
    const ulong linespercase = 5;
    for(ulong i = 1; i < numcases * linespercase; i+=linespercase) {
        won = false;
        printf("Case #%i: ", ncase);
        ncase++;
        // printf("=======\n");

        char board[4][4];
        bool incomplete = false;

        for (int x =0; x < 4; x++) {
            char vert[4];
            for (int y =0; y<4; y++) {
                board[x][y] = lines[i + y].c_str()[x];
                vert[y] = board[x][y];
            }
            check_line(vert);
        }
        for (int y = 0; y < 4; ++y) {
            char hor[4];
            for (int x = 0; x < 4; ++x) {
                hor[x] = board[x][y];
                if (board[x][y] == '.') {
                    incomplete = true;
                }
            }
            check_line(hor);
        }
        char diag1[4];
        char diag2[4];
        for (int i = 0; i < 4; ++i)
        {
            diag1[i] = board[i][i];
            diag2[i] = board[3 - i][i];
            check_line(diag2);
            check_line(diag1);
        }

        if (!won && incomplete) {
            cout << "Game has not completed\n";
        }
        if(!won && !incomplete) {
            cout << "Draw\n";
        }


    }
    return 0;
}
