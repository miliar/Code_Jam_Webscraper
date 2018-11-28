#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <memory.h>

using namespace std;

string solve() {
    int x, y;
    scanf("%d %d", &x, &y);
    string res = "";

    string moveX = "";
    if (x < 0) {
        moveX = "EW";
    } else {
        moveX = "WE";
    }

    string moveY = "";
    if (y < 0) {
        moveY = "NS";
    } else {
        moveY = "SN";
    }

    int deltaX = abs(x);
    for (int i = 0; i < deltaX; i++) {
        res = res + moveX;
    }

    int deltaY = abs(y);
    for (int i = 0; i < deltaY; i++) {
        res = res + moveY;
    }

    return res;
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": " << solve() << endl;
    }

    return 0;
}
