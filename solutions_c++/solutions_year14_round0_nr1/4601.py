/**
 * jerrym
 * A.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;

int gInt () {
    int i;
    scanf("%d", &i);
    return i;
}

lli gLong () {
    lli i;
    scanf("%lld", &i);
    return i;
}

double gDouble () {
    double i;
    scanf("%lf", &i);
    return i;
}

void quit () {
    fflush(stdout);
    exit(0);
}

int mata[4][4], matb[4][4];

void solve (int nC) {
    int rowa = gInt() - 1;
    for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) mata[i][j] = gInt();
    int rowb = gInt() - 1;
    for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) matb[i][j] = gInt();
    int matching = 0;
    int matched = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (mata[rowa][i] == matb[rowb][j]) {
                ++matching;
                matched = mata[rowa][i];
            }
        }
    }
    printf("Case #%d: ", nC + 1);
    if (!matching) {
        printf("Volunteer cheated!\n");
    } else if (matching == 1) {
        printf("%d\n", matched);
    } else {
        printf("Bad magician!\n");
    }
}

int main (int argc, char ** argv) {
    int nC = gInt();
    for (int i = 0; i < nC; ++i) {
        solve(i);
    }
    quit();
}
