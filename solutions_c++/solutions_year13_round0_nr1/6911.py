#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
using namespace std;

char b[10][10];

int check(char c) {
    int i, j;
    for (i=0; i<4; i++) {
        for (j=0; j<4; j++) {
            if (b[i][j] != c && b[i][j] != 'T') break;
        }
        if (j == 4) return 1;
        for (j=0; j<4; j++) {
            if (b[j][i] != c && b[j][i] != 'T') break;
        }
        if (j == 4) return 1;
    }
    for (i=0; i<4; i++) {
        if (b[i][i] != c && b[i][i] != 'T') break;
    }
    if (i == 4) return 1;
    for (i=0; i<4; i++) {
        if (b[i][3-i] != c && b[i][3-i] != 'T') break;
    }
    if (i == 4) return 1;
    for (i=0; i<4; i++) {
        for (j=0; j<4; j++) {
            if (b[i][j] == '.') return -1;
        }
    }
    return 0;
}

int main() {
    freopen("/Users/fengyelei/Desktop/A-small.in", "r", stdin);
    freopen("/Users/fengyelei/Desktop/out", "w", stdout);
    int T, t=1;
    int i, j, k, n, m;
    for (scanf("%d", &T); t<=T; t++) {
        for (i=0; i<4; i++) scanf("%s", b[i]);
        getchar();
        printf("Case #%d: ", t);
        int cx = check('X'), co = check('O');
        if (cx > 0) printf("X won\n");
        else if (co > 0) printf("O won\n");
        else if (cx == 0 && co == 0) printf("Draw\n");
        else printf("Game has not completed\n");
    }
}
