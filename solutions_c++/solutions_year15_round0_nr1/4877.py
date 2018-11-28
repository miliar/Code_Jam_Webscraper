#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

int solve(const string& s) {
    int sum = 0;
    int needed = 0;
    for (int i=0; i<s.length(); i++) {
        sum += (int) s[i] - '0';
        if (i >= sum+needed) {
            needed += 1;
        }
    }

    return needed;
}

int main(void) {
    /* number of test cases */
    int t;
    cin >> t;

    for(int i=1; i <= t; i++) {
        int max;
        cin >> max;
        string s;
        cin >> s;

        cout << "Case #" << i << ": " << solve(s) << endl;
    }

    return 0;
}
