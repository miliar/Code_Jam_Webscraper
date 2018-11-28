#include <bitset>
#include <iostream>

using namespace std;

int main() {
    size_t t;
    cin >> t;
    for (size_t i = 0; i < t; i++) {
        string s;
        cin >> s;
        bitset<100> pancakes;
        for (size_t j = 0; j < s.size(); j++) {
            if (s[j] == '-') pancakes.set(j);
        }
        size_t total = 0;
        for (size_t j = s.size(); j <= s.size(); j--) {
            if (pancakes[j] != total % 2) total++;
        }
        cout << "Case #" << i + 1 << ": " << total << endl;
    }
}
