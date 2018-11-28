#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool solve(int x, int r, int c) {
    if (r < c) {
        int t;
        t = r;
        r = c;
        c = t;
    }
    int area = r * c;
    if (area % x) {
        cout << "*";
        return false;
    }
    if (x > r) {
        return false;
    }
    if (x / 2 > c) {
        return false;
    }
    return true;
}

int main() {
    ifstream ifs("small");

    int t;
    ifs >> t;

    for (int i = 0; i < t; ++i) {
        int x, r, c;
        ifs >> x >> r >> c;
        cout << x << " " << r << " " << c << "====";
        cout << "Case #" << i + 1 << ": " << (solve(x, r, c) ? "GABRIEL" : "RICHARD") << endl;
    } 
}
