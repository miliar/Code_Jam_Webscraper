#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t, x, c, r;
    cin >> t;
    for (int i=1; i<=t; i++) {
        cin >> x >> r >> c;
        int lo = min(r, c), hi = max(r, c);
        bool flag = false;

        switch(x) {
            case 1:
                flag = true;
                break;
            case 2:
                flag = hi >= 2;
                break;
            case 3:
                flag = lo >= 2 && hi >= 3;
                break;
            case 4:
                flag = lo >= 3 && hi >= 4;
                break;
            case 5:
                flag = lo >= 4 && hi >= 5;
                break;
            case 6:
                flag = lo >= 4 && hi >= 6;
                break;
        }

        if (flag && r * c % x == 0)
            cout << "Case #" << i << ": " << "GABRIEL" << endl;
        else
            cout << "Case #" << i << ": " << "RICHARD" << endl;
    }
    return 0;
}
