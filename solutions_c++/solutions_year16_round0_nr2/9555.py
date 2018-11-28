#include <iostream>
#include <unordered_set>

using namespace std;

int pancake_flip(string s) {
    int down_transitions = 0;
    int start_minus = 0;

    for (int i = 0; i < s.size(); i++) {
        if (i == 0) {
            if (s[i] == '-')
                start_minus = 1;
         } else if (s[i - 1] == '+' and s[i] == '-') {
             down_transitions++;
         }
    }
    return ((down_transitions * 2) + start_minus);
}

int main() {
    int t;
    string s;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        cin >> s;
        cout << "Case #" << i << ": " << pancake_flip(s) << endl;
    }
}
