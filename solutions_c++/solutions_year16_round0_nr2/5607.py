#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int T, N, D, n;
string S;

int solve(string cake) {
    cake += '+';
    int res = 0;
    char prev = cake[0];
    for (char c : cake) {
        if (c != prev) { ++res; }
        prev = c;
    }
    return res;
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> S;
        cout << "Case #" << t << ": " << solve(S) << endl;
    }
    return 0;
}