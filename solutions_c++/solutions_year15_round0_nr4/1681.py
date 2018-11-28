#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstring>
#include <cmath>
#include <climits>
#include <ctime>
#include <cctype>
#include <fstream>

using namespace std;

typedef long long ll;

string solve(int X, int R, int C) {
    switch (X) {
    case 1:
        return "GABRIEL";
    case 2:
        if (R % 2 == 0 || C % 2 == 0) {
            return "GABRIEL";
        } else {
            return "RICHARD";
        }
    case 3:
        if ((R % 3 == 0 && C >= 2) || (C % 3 == 0 && R >= 2)) {
            return "GABRIEL";
        } else {
            return "RICHARD";
        }
    case 4:
        if ((R == 4 && C >= 3) || (C == 4 && R >= 3)) {
            return "GABRIEL";
        } else {
            return "RICHARD";
        }
    }
    return "RICHARD";
}

//#define LARGE

int main() {

#ifndef LARGE
    ifstream in("D-small-attempt2.in");
    ofstream out("D-small-attempt2.out");
#else
    ifstream in("D-large.in");
    ofstream out("D-large.out");
#endif

    int T; in >> T;
    for (int t = 0; t < T; t++) {
        int X, R, C; in >> X >> R >> C;
        out << "Case #" << t + 1 << ": " << solve(X, R, C) << endl;
        cout << "Case #" << t + 1 << ": " << solve(X, R, C) << endl;
    }
    getchar();
    return 0;
}
