#include <cassert>
#include <cmath>
#include <cstdint>
#include <bitset>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int T, N, J;
string S;


string solve(string word) {
    string last = "";
    for (char c : word) {
        if (last.length() == 0) last += c;
        else if (c >= last[0]) last = c + last;
        else last = last + c;
    }
    return last;
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> S;
        cout << "Case #" << t << ": " << solve(S) << endl;
    }
    return 0;
}