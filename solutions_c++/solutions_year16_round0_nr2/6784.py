#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    int t, i;
    cin >> t;
    for (i = 0; i < t; i++) {
        string s;
        cin >> s;
        cout << "Case #" << i + 1 << ": ";

        auto count = 0;
        auto lastChar = s[0];
        for (auto c : s) {
            if (c != lastChar) {
                count++;
            }
            lastChar = c;
        }
        if (lastChar == '-') {
            count++;
        }

        cout << count;

        cout << endl;
    }
    return 0;
}
