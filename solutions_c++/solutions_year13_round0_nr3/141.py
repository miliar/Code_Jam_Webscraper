// This solution uses the gmp library for C++ (see gmplib.org).
// To compile/run this solution:
// 1. Download and install the gmp/gmpxx library
// 2. Link the gmpxx library when compiling this source code.
//    e.g.
//        g++ -Wall -o C_extreme C_extreme.cpp -lgmpxx
#include <iostream>
#include <string>
#include <gmpxx.h>
using namespace std;

inline bool greaterOrEqual(string a, string b) {
    if (a.length() > b.length()) {
        return true;
    }
    if (a.length () < b.length()) {
        return false;
    }
    return a >= b;
}

inline string z(int length) {
    return string(length, '0');
}

int countFairAndSquare(const string& limit) {

    int ans = 0;

    string temp;

    // Pattern: 3
    temp = "3";
    ans += (int) greaterOrEqual(limit, temp);

    // Pattern: 2
    temp = "2";
    ans += (int) greaterOrEqual(limit, temp);

    // Pattern: 2x2
    for (int gap = 0; gap <= 50; gap++) {
        temp = "2" + z(gap) + "2";
        ans += (int) greaterOrEqual(limit, temp);
    }

    // Pattern: 2x1x2
    for (int gap = 0; gap <= 25; gap++) {
        temp = "2" + z(gap) + "1" + z(gap) + "2";
        ans += (int) greaterOrEqual(limit, temp);
    }

    // Pattern: 1x2x1
    for (int gap = 0; gap <= 25; gap++) {
        temp = "1" + z(gap) + "2" + z(gap) + "1";
        ans += (int) greaterOrEqual(limit, temp);
    }

    // Pattern: 1x1x2x1x1
    for (int gap1 = 0; gap1 <= 25; gap1++) {
        for (int gap2 = 0; gap1 + gap2 <= 25; gap2++) {
            temp = "1" + z(gap1) + "1" + z(gap2) + "2"
                + z(gap2) + "1" + z(gap1) + "1";
            ans += (int) greaterOrEqual(limit, temp);
        }
    }

    // Pattern: 1
    temp = "1";
    ans += (int) greaterOrEqual(limit, temp);

    // Pattern: 1x1
    for (int gap = 0; gap <= 50; gap++) {
        temp = "1" + z(gap) + "1";
        ans += (int) greaterOrEqual(limit, temp);
    }

    // Pattern: 1x1x1
    for (int gap = 0; gap <= 25; gap++) {
        temp = "1" + z(gap) + "1" + z(gap) + "1";
        ans += (int) greaterOrEqual(limit, temp);
    }

    // Pattern: 1x1x1x1
    for (int gap1 = 0; gap1 <= 25; gap1++) {
        for (int gap2 = 0; 2*gap1 + gap2 <= 50; gap2++) {
            temp = "1" + z(gap1) + "1" + z(gap2) + "1" + z(gap1) + "1";
            ans += (int) greaterOrEqual(limit, temp);
        }
    }

    // Pattern: 1x1x1x1x1
    for (int gap1 = 0; gap1 <= 25; gap1++) {
        for (int gap2 = 0; gap1 + gap2 <= 25; gap2++) {
            temp = "1" + z(gap1) + "1" + z(gap2) + "1" + z(gap2) + "1" + z(gap1) + "1";
            ans += (int) greaterOrEqual(limit, temp);
        }
    }

    // Pattern: 1x1x1x1x1x1
    for (int gap1 = 0; gap1 <= 25; gap1++) {
        for (int gap2 = 0; gap1 + gap2 <= 25; gap2++) {
            for (int gap3 = 0; 2*gap1 + 2*gap2 + gap3 <= 50; gap3++) {
                temp = "1" + z(gap1) + "1" + z(gap2) + "1" + z(gap3) + "1" + z(gap2) + "1" + z(gap1) + "1";
                ans += (int) greaterOrEqual(limit, temp);
            }
        }
    }

    // Pattern: 1x1x1x1x1x1x1
    for (int gap1 = 0; gap1 <= 25; gap1++) {
        for (int gap2 = 0; gap1 + gap2 <= 25; gap2++) {
            for (int gap3 = 0; gap1 + gap2 + gap3 <= 25; gap3++) {
                temp = "1" + z(gap1) + "1" + z(gap2) + "1" + z(gap3) + "1"
                    + z(gap3) + "1" + z(gap2) + "1" + z(gap1) + "1";
                ans += (int) greaterOrEqual(limit, temp);
            }
        }
    }

    // Pattern: 1x1x1x1x1x1x1x1
    for (int gap1 = 0; gap1 <= 25; gap1++) {
        for (int gap2 = 0; gap1 + gap2 <= 25; gap2++) {
            for (int gap3 = 0; gap1 + gap2 + gap3 <= 25; gap3++) {
                for (int gap4 = 0; 2*gap1 + 2*gap2 + 2*gap3 + gap4 <= 50; gap4++) {
                    temp = "1" + z(gap1) + "1" + z(gap2) + "1" + z(gap3) + "1" + z(gap4)
                        + "1" + z(gap3) + "1" + z(gap2) + "1" + z(gap1) + "1";
                    ans += (int) greaterOrEqual(limit, temp);
                }
            }
        }
    }

    // Pattern: 1x1x1x1x1x1x1x1x1
    for (int gap1 = 0; gap1 <= 25; gap1++) {
        for (int gap2 = 0; gap1 + gap2 <= 25; gap2++) {
            for (int gap3 = 0; gap1 + gap2 + gap3 <= 25; gap3++) {
                for (int gap4 = 0; gap1 + gap2 + gap3 + gap4 <= 25; gap4++) {
                    temp = "1" + z(gap1) + "1" + z(gap2) + "1" + z(gap3) + "1" + z(gap4) + "1"
                        + z(gap4) + "1" + z(gap3) + "1" + z(gap2) + "1" + z(gap1) + "1";
                    ans += (int) greaterOrEqual(limit, temp);
                }
            }
        }
    }

    return ans;
}

int main() {

    int tc;
    cin >> tc;

    for (int t = 1; t <= tc; t++) {
        mpz_class a, b;
        cin >> a >> b;

        int ans;
        mpz_class upperLimit = sqrt(b);
        mpz_class lowerLimit = sqrt(a-1);
        ans = countFairAndSquare(upperLimit.get_str()) - countFairAndSquare(lowerLimit.get_str());
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

