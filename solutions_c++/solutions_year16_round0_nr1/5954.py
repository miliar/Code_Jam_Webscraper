#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        int n;
        cin >> n;

        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }

        set<char> digits;

        int count = 0;
        while (digits.size() < 10) {
            count += n;
            string s = to_string(count);

            for (int i = 0; i < s.size(); i++) {
                digits.insert(s[i]);
            }
        }

        cout << count << endl;
    }
}