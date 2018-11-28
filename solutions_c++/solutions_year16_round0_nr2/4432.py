#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    int t, n;
    cin >> t;
    string s;
    for (int i = 1; i <= t; ++i) {
        cin >> s;
        cout << "Case #" << i << ": ";
        n = s.size();
        int a[n];
        int b[n];
        memset(a, 0, sizeof a);
        memset(b, 0, sizeof b);
        if (s[0] == '-') {
            a[0] = 1;
            b[0] = 0;
        }
        else {
            a[0] = 0;
            b[0] = 1;
        }
        for (int j = 1; j < n; ++j) {
            if (s[j] == '-') {
                a[j] = a[j - 1] + 2;
                b[j] = b[j - 1];
            }
            else {
                a[j] = a[j - 1];
                b[j] = b[j - 1] + 2;
            }
            if (a[j - 1] + 1 < b[j]) {
                b[j] = a[j - 1] + 1;
            }
            if (b[j - 1] + 1 < a[j]) {
                a[j] = b[j - 1] + 1;
            }
        }
        cout << a[n - 1] << endl;
    }
    return 0;
}
