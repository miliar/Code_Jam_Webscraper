#include <algorithm>
#include <string>
#include <iostream>

#define MAX_LEN 100

using namespace std;

int read(istream &is, bool *buf) {
    string facesStr;
    is >> facesStr;

    auto iBuf = 0u;
    buf[iBuf++] = (facesStr[0] == '+');

    const auto rawSize = facesStr.size();
    for (auto i = 1u; i < rawSize; ++i) {
        const auto face = (facesStr[i] == '+');
        if (buf[iBuf - 1] != face)
            buf[iBuf++] = face;
    }

    return iBuf;
}

int solve(bool *pancakes, int len, bool face) {
    if (len == 0) return 0;
    if (len == 1) return pancakes[0] == face ? 0 : 1;

    if (pancakes[len - 1] == face) {
        return solve(pancakes, len - 1, face);
    } else {
        return solve(pancakes, len - 1, !face) + 1;
    }
}

int main() {
    int numberOfCases;
    cin >> numberOfCases;
    bool pancakes[MAX_LEN];
    for (int i = 1; i <= numberOfCases; ++i) {
        // read input
        auto len = read(cin, pancakes);
        // write output
        auto solution = solve(pancakes, len, true);
        cout << "Case #" << i << ": " << solution << endl;
    }

    return 0;
}
