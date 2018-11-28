//
//  pancake.cpp
//  
//
//  Created by John Nevard on 4/9/16.
//
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int flip(const string& s) {
    bool neg = (s[0] == '-');
    int n = 1;
    char prev = s[0];
    for (int i = 1; i < s.size(); ++i)
        if (s[i] != prev) {
            ++n;
            prev = s[i];
        }
    return n - ((n & 1) != neg);
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string s;
        cin >> s;
        int nf = flip(s);
        cout << "Case #" << i << ": ";
        cout << nf << '\n';
    }
    return 0;
}