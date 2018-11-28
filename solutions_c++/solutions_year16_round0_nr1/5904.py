#include <iostream>
#include <string>
#include <unordered_set>
#include <cstdint>

using namespace std;

uint64_t solve(uint64_t seed) {
    unordered_set<char> unseen = {
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
    uint64_t n = 0;
    do {
        n += seed;
        string digits = to_string(n);
        //cout << "Seeing number: " << digits << endl;
        for (char c : digits) {
            unseen.erase(c);
            //cout << "Seeing digit: " << c << endl;
        }
    } while (unseen.size());
    return n;
}

string describe(int seed) {
    if (seed) {
        uint64_t n = seed;
        return to_string(solve(n));
    } else {
        return "INSOMNIA";
    }
}

int main() {
    int count;
    cin >> count;
    for (int case_i = 1; case_i <= count; case_i++) {
        int seed;
        cin >> seed;
        cout << "Case #" << case_i << ": " << describe(seed) << endl;
    }
    return 0;
}
