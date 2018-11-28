#include <bits/stdc++.h>

using namespace std;

int T;
string line;

bool state(char ch) {
    if (ch == '+') {
        return true;
    }
    return false;
}

int solve(string s) {
    deque<bool> flip;
    bool cur = state(line[0]);
    flip.push_back(cur);
    for (int i = 1; i < s.length(); ++i) {
        if (state(line[i]) != cur) {
            cur = state(line[i]);
            flip.push_back(cur);
        }
    }

    int ctr = flip.size();
    if (flip.back()) {
        ctr--;
    }
    return ctr;

    /*
    for (bool b : flip) {
        cout << b << " ";
    }
    cout << endl;
    */

}

int main() {
    cin >> T;
    for (int Q = 1; Q <= T; ++Q) {
        cin >> line;
        printf("Case #%d: %d\n", Q, solve(line));
    }
    
    
    return 0;
}
