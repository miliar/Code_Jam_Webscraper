#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool valid(const string& pancake) {
    for (char c : pancake) {
        if (c == '-') {
            return false;
        }
    }
    return true;
}

// 1. find as many leading '-'s as you can and flip
// 2. if valid, return
// 3. find as many leading '+'s as you can and flip
int solve(string& pancake) {
    int turns = 0;

    while (!valid(pancake)) {
        // find as many leading '-'s as you can and flip
        bool flip = false;
        for (int i = 0; i < pancake.size() && pancake[i] == '-'; ++i) {
            pancake[i] = '+';
            flip = true;
        }
        turns += flip;

        if (valid(pancake)) {
            break;
        }
        
        // find as many leading '+'s as you can and flip
        flip = false;
        for (int i = 0; i < pancake.size() && pancake[i] == '+'; ++i) {
            pancake[i] = '-';
            flip = true;
        }
        turns += flip;
    }

    return turns;
}

int main() {
    int T;
    string pancake;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> pancake;
        cout << "Case #" << i << ": " << solve(pancake) << endl;
    }
    return 0;
}
