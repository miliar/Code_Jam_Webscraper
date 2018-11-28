#include <bits/stdc++.h>
using namespace std;

void flip_string(string& s, int begin, int end) {
    for(int i = begin; i <= end; ++i) {
        if(s[i] == '-') {
            s[i] = '+';
        }
        else {
            s[i] = '-';
        }
    }
}

int main() {
    int T;
    cin >>T;
    
    for(int i = 1; i <= T; ++i) {
        string s;
        cin >> s;
        string output = "Case #" + to_string(i) + ": ";
        
        int count = 0;
        for(int j = s.size() - 1; j >= 0; --j) {
            if(s[j] == '-') {
                ++count;
                flip_string(s, 0, j);
            }
        }
        cout << output << count << '\n';
    }
}
