/**
 * Jerry Ma
 * B.cpp
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

int ht;
int wt;
int desired[105][105];
int grid[105][105];

inline bool equals () {
    for (int i = 0; i < ht; i ++) {
        for (int j = 0; j < wt; j ++) {
            if (desired[i][j] != grid[i][j])
                return false;
        }
    }
    return true;
}

inline bool doMove () {
    for (int i = 0; i < ht; i ++) {
        bool canDo = true;
        int maxH = 0;
        for (int j = 0; j < wt; j ++)
            maxH = max(maxH, grid[i][j]);
        maxH --;
        for (int j = 0; j < wt; j ++) {
            if (desired[i][j] > maxH) {
                canDo = false;
                break;
            }
        }
        if (canDo) {
            for (int j = 0; j < wt; j ++)
                grid[i][j] = maxH;
            return true;
        }
    }
    for (int j = 0; j < wt; j ++) {
        bool canDo = true;
        int maxH = 0;
        for (int i = 0; i < ht; i ++)
            maxH = max(maxH, grid[i][j]);
        maxH --;
        for (int i = 0; i < ht; i ++) {
            if (desired[i][j] > maxH) {
                canDo = false;
                break;
            }
        }
        if (canDo) {
            for (int i = 0; i < ht; i ++)
                grid[i][j] = maxH;
            return true;
        }
    }
    return false;
}

void solve (int nC) {
    printf("Case #%d: ", nC);
    ht = gInt();
    wt = gInt();
    for (int i = 0; i < ht; i ++) {
        for (int j = 0; j < wt; j ++) {
            desired[i][j] = gInt();
            grid[i][j] = 100;
        }
    }
    while (!equals()) {
        if (!doMove()) {
            printf("NO\n");
            return;
        }
    }
    printf("YES\n");
}

int main (int argc, char ** argv) {
    int nC = gInt();
    for (int i = 1; i <= nC; i ++)
        solve(i);
    quit();
}