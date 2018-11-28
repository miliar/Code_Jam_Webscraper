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

vector<int> Tokenize_i(string str) {
    char input [kMaxLineSize];
    strcpy(input, str.c_str());
    char *token = strtok(input, " ");
    vector<int> items;
    while (token != NULL) {
        items.push_back(atoi(token));
        token = strtok(NULL, " ");
    }
    return items;
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
    int ncase = 0;
    int step = 3;
    for(ulong line_i = 1; ncase < numcases; line_i+=step) {
        bool yes = true;
        printf("Case #%i: ", ncase+1);
        ncase++;

        vector<int> size = Tokenize_i(lines[line_i].c_str()); //m n
        int m = size[0];
        int n = size[1];
        step = m + 1;

        vector<vector<int>> mat;
        for (int i = 1; i <= m; ++i)
        {
            mat.push_back(Tokenize_i(lines[line_i + i]));
        }
        for (auto r : mat) {
            int max = 0;
            int j = 0;
            // cout << "COLUMN: " << endl;
            for (auto val : r) {
                if (val > max) {
                    max = val;
                }
            }
            for (auto val : r) {
                if (val < max)
                for (int i = 0; i < m; ++i)
                {
                    auto x_val = mat[i][j];
                    if (x_val != val) {
                        cout << "NO" << endl;
                        yes = false;
                        goto endloop;
                    }
                }
                j++;
            }
        }
        endloop:
        if (yes) {
            cout << "YES" << endl;
        }
    }
    return 0;
}
