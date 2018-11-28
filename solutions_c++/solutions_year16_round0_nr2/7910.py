
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

int solve(string s) {
    int i = s.length() - 1;
    int c = 0;
    bool inv = false;
    
    while (i >= 0) {
        if ((!inv && s[i] == '-') || (inv && s[i] == '+')) {
            c++;
            inv ^= true;
        } 
        i--;
    }
    
    return c;
}

int main(void) {
    int t;
    string s;
    
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cin >> s;
        cout << "Case #" << i << ": " << solve(s) << endl;
    }
    
    return 0;
}
