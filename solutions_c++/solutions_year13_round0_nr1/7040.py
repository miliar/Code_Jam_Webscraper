#include <stdio.h>
#include <iostream>
using namespace std;

int solve(const string line[]) {
    bool finish = true;
    int x,y,t;
    for (int i=0; i<4; ++i) {
        x=y=t=0;
        for (int j=0; j<4; ++j) {
            if (line[i][j] == 'X') ++x;
            else if (line[i][j] == 'O') ++y;
            else if (line[i][j] == 'T') ++t;
            else {
                finish = false;
                break;
            }
        }
        if (x+t == 4) return -1;
        if (y+t == 4) return 1;
    }

    for (int i=0; i<4; ++i) {
        x=y=t=0;
        for (int j=0; j<4; ++j) {
            if (line[j][i] == 'X') ++x;
            else if (line[j][i] == 'O') ++y;
            else if (line[j][i] == 'T') ++t;
            else break;
        }
        if (x+t == 4) return -1;
        if (y+t == 4) return 1;
    }

    x=y=t=0;
    for (int i=0; i<4; ++i) {
        if (line[i][i] == 'X') ++x;
        else if (line[i][i] == 'O') ++y;
        else if (line[i][i] == 'T') ++t;
        else break;
    }
    if (x+t == 4) return -1;
    if (y+t == 4) return 1;

    x=y=t=0;
    for (int i=3; i>=0; --i) {
        if (line[3-i][i] == 'X') ++x;
        else if (line[3-i][i] == 'O') ++y;
        else if (line[3-i][i] == 'T') ++t;
        else break;
    }
    if (x+t == 4) return -1;
    if (y+t == 4) return 1;

    return finish?0:2;
}

int main(int argc, char * argv[]) {
    int T;
    scanf("%d\n", &T);
    for (int i=1; i<=T; ++i) {
        string tmp, line[4];
        for (int j=0; j<4; ++j) {
            while (getline(cin, tmp) && tmp.size() < 4);
            line[j] = tmp;
        }
        switch (solve(line)) {
            case -1: printf("Case #%d: X won\n", i);
                     break;
            case 0: printf("Case #%d: Draw\n", i);
                    break;
            case 1: printf("Case #%d: O won\n", i);
                    break;
            default: printf("Case #%d: Game has not completed\n", i);
        }
    }
    return 0;
}
