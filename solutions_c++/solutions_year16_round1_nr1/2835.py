#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main(void) {
    int t;
    string s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> s;
        cout << "Case #" << i << ": ";
        deque<char> dq;
        dq.push_back(s[0]);
        for (int j = 1; j < s.length(); ++j) {
            if (s[j] >= dq.front()) dq.push_front(s[j]);
            else dq.push_back(s[j]);
        }
        while (!dq.empty()) {
            cout << dq.front();
            dq.pop_front();
        }
        cout << endl;
    }
    return 0;
}
