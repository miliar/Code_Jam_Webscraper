#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

const int MAX_N = 100 + 1;

void flip(bool *a, int n) {
    for (int i=0;i<n;i++) {
        a[i] = !a[i];
    }
}

int solve(bool *a, int n) {
    int res = 0;
    
    for (int i=n-1;i>=0;i--) {
        if (a[i]) continue;
        else {
            flip(a, i+1);
            res++;
        }
    }
    
    return res;
}

int main() {
    int t;
    
    cin >> t;
    for (int x=0;x<t;x++) {
        bool a[MAX_N];
        string s;
        cin >> s;
        
        for (int i=0;i<s.length();i++) {
            a[i] = (s[i] == '+');
        }
        
        cout << "Case #" << x+1 << ": " << solve(a, s.length()) << "\n";
    }
    
    return 0;
}

