#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <queue>
#include <sstream>
#include <bitset>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int g = 1; g <= T; g++) {
        unsigned long long r, t;
        cin >> r >> t;

        unsigned long long curwhiteradius = r;
        unsigned long long numblackdrawn = 0;
        unsigned long long paintleft = t;
        // takes (pi * (r + 1)^2  - (pi * r^2)) cm^2 to paint an area
        // pi*(r^2 + 2r + 1) - pi*r^2
        // pi * (r^2 + 2r + 1 - r^2)
        // pi * (2r + 1)
        while (paintleft >= ((2 * curwhiteradius) + 1)) {
            paintleft -= 2 * curwhiteradius + 1;
            curwhiteradius = curwhiteradius + 2;
            numblackdrawn++;
        }
        cout << "Case #" << g << ": " << numblackdrawn << "\n";
    }
}
