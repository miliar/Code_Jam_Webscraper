#include <iostream>
#include <string>
#include <cstdint>
#include <queue>
#include <unordered_set>

using namespace std;

// 1 -> 0
// 10 -> 00
// 01 -> 11 -> 00
//    -> 01 -> ..
// 001 -> 111 -> 000
//     -> 
//     -> 011 -> 111 -> 000
// 101010
//     001010
//     101011
//     001011
//     101111
//     001111
//     111111
//     000000
//
// 101010 1
// ^
// 001010 2
// ^^^
// 011010 3
// 111010 4
// 000010 5
// ^^^^^
// 011110 6
// 111110 7
// 000000 8
//
//
// 101010 0
// ^
// 001010 1
//   ^
// 111010 2
// 000010 3
//     ^
// 111110 4
// 000000 5
//
// 1 0
// ^
// 0 1
//
// 11 0
// 00 1
//
// 011 0
// ^
//  ^  2
//    ^2
// 011 -> 111 -> 000
//
// 01011 0
// ^
//  ^    2
// 11011
// 00011
//   ^
//    ^  4
//      ^4
// 11100
// 00000

int solve(string s) {
    int flips = 0;
    for (size_t i = 0; i < s.size(); ) {
        if (s[i] == '-') {
            if (i == 0) {
                flips++;
            } else {
                flips += 2;
            }

            while (s[i] == '-') {
                ++i;
            }
        } else {
            ++i;
        }
    }

    return flips;
}

int main() {
    int tn; cin >> tn;
    string tmp;
    getline(cin, tmp);
    for (int tc = 1; tc <= tn; ++tc) {
        string s;
        getline(cin, s);
        int res = solve(s);
        cout << "Case #" << tc << ": ";
        cout << res << "\n";
    }
    return 0;
}
