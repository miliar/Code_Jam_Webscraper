
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <cstdint>
#include <string>

using namespace std;

int solve(const string& s) {
    int m[101];
    memset(m, 0, sizeof(m));
    
    if (s[0] == '-') {
        m[0] = 1;
    }
    
    for (int i = 1; i < s.length(); i++) {
        if (s[i] != s[i-1]  && s[i] == '-') {
            m[i] = m[i-1] + 2;
        } else {
            m[i] = m[i-1];
        }
    }
    return m[s.length() -1];
}


int main() {
    int tCases;
    cin >> tCases;
    for (int c = 1; c <= tCases; c++) {
        string s;
        cin >> s;
        
        cout << "Case #" << c << ": " << solve(s) << "\n";
    }
}
