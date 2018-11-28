/* 
 * File:   main.cpp
 * Author: Yiting
 *
 * Created on April 13, 2013, 8:52 AM
 */

#include <cstdlib>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;

FILE *fin = fopen("test.in", "rb");
FILE *fout = fopen("test.out", "wb");
int T, N, M, maxN;
int lawn[100][100];
bool num[100];

bool checkUp(int x, int y) {
    //i = x to 0, j = y
    int i, j = y;
    for (i = x; i >= 0; i--) {
        if (lawn[i][j] > lawn[x][y])
            return false;
    }
    return true;
}

bool checkDown(int x, int y) {
    //i = x to N, j = y
    int i, j = y;
    for (i = x; i < N; i++) {
        if (lawn[i][j] > lawn[x][y])
            return false;
    }
    return true;
}

bool checkLeft(int x, int y) {
    // i = x, j = y to 0
    int i = x, j;
    for (j = y; j >= 0; j--) {
        if (lawn[i][j] > lawn[x][y])
            return false;
    }
    return true;
}

bool checkRight(int x, int y) {
    // i = x, j = y to M
    int i = x, j;
    for (j = y; j < M; j++) {
        if (lawn[i][j] > lawn[x][y])
            return false;
    }
    return true;
}

bool check() {
    //i from 1 to N-1, j from 1 to M-1
    int i, j, k;
    for (k = 1; k < maxN; k++) {
        if (num[k])
            for (i = 0; i < N; i++)
                for (j = 0; j < M; j++) {
                    if (lawn[i][j] == k)
                        if (!((checkUp(i, j) && checkDown(i, j)) || (checkLeft(i, j) && checkRight(i, j))))
                            return false;
                }
    }
    return true;
}

int main() {
    int i, j, k;
    bool res;
    fscanf(fin, "%d", &T);
    for (k = 1; k <= T; k++) {
        maxN = 0;
        memset(num, 0, sizeof (num));
        fscanf(fin, "%d %d", &N, &M);
        for (i = 0; i < N; i++) {
            for (j = 0; j < M; j++) {
                fscanf(fin, "%d", &lawn[i][j]);
                num[lawn[i][j]] = true;
                maxN = lawn[i][j] > maxN ? lawn[i][j] : maxN;
            }
        }
        res = check();
        if (res) fprintf(fout, "Case #%d: YES\n", k);
        else fprintf(fout, "Case #%d: NO\n", k);
    }
    return 0;
}

