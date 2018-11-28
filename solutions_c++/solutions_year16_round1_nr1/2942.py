#include <iostream>
#include <cstdio>
#include <string>
#include <deque>

using namespace std;

int main() {
    int T;
    cin >> T;
    string input;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        cin >> input;
        deque<char> ans;
        for (auto ch : input) {
            if (ans.size() == 0 || ch < ans.front()) ans.push_back(ch);
            else ans.push_front(ch);
        }

        for (auto ch : ans) {
            cout << ch;
        }
        cout << endl;
    }
}
