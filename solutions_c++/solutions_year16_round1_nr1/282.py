#include <iostream>
#include <string>
#include <list>
using namespace std;

int main() {
    long T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        list<char> ans;
        ans.push_back(s[0]);
        for (int i = 1; i < s.size(); i++) {
            if (s[i] >= ans.front()) ans.push_front(s[i]);
            else ans.push_back(s[i]);
        }
        cout << "Case #" << t << ": " << string(ans.begin(), ans.end()) << endl;
    }
}
