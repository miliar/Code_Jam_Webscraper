#include <iostream>
#include <string>

using namespace std;

void test() {
    string s;
    bool flipped = false;
    int flips = 0;
    cin >> s;

    for (int i = s.length() - 1; i >=0; i--) {
        if ((s[i] == '+' && flipped) || (s[i] == '-' && !flipped)) {
            flips++;
            flipped = !flipped;
        }
    }

    cout << flips << "\n";
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        test();
    }
}
