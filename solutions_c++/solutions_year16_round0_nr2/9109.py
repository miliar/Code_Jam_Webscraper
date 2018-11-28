#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solve(string s) {
    int flips = 0;
    for (int i = 0; i < s.length(); i++) {
        int t = (s[s.length() - 1 - i] == '+' ? 0 : 1);
        t += flips;
        if (t%2) 
            flips++;
    }
    return flips;
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        printf("Case #%d: %d\n", i+1,solve(s));
    }
    return 0;
}
