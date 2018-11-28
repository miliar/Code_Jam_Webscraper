/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

bool can_fail(int x, int r, int c) {
    if (r > c) {
        swap(r, c);
    } // Now r <= c
    if ((r * c) % x) {
        return true; // *have to* fail
    }
    if (x >= 8) {
        return true; // Leave 1x1 hole
    }
    if (x > c) {
        return true; // Straight line, will not fit
    }
    if (x >= 2 * r + 1) {
        return true; // L-shaped, (r+1)x(r+1) bounding box size, will not fit
    }
    if (x < 2 * r - 1) {
        return false; // Minimum side at most r-1, cannot split field
    }
    // Now x=2*r or x=2*r-1
    // So r=(x+1)/2
    if (r == 1) { // x: 1, 2
        return false; // Obvious
    }
    // r=2:
    if (x == 3) {
        return false; // L-shaped, can squeeze in one end
    }
    if (x == 4) {
        return true; // T-shaped will leave odd amount on both sides
    }
    // r=3:
    if (x == 5) {
        // c is divisible by 5
        //  # # 1 2 b c
        //  . # # 3 a d
        //  . . # 4 5 e
        return c == 5; // Need at least 10 to fill
    }
    if (x == 6) {
        //  # # #
        //  . # .
        //  # # .
        return true; // Not divisible by 3 on both sides. 1-hole if rotated
    }
    // r = 4:
    if (x == 7) {
        // c is divisible by 7
        //  # # # 1 2 b c 3 4
        //  . . # # 3 a d 2 5
        //  . . . # 4 7 e 1 6
        //  . . . # 5 6 f g 7
        return c == 7; // Need at least 14 to fill
    }
    cerr << "WTF!? (" << x << r << c << ')' << endl;
    return false;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int x, r, c;
        cin >> x >> r >> c;
        cout << "Case #" << T << ": " << (can_fail(x, r, c) ? "RICHARD" : "GABRIEL") << endl;
    }
    return 0;
}
