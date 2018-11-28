#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    int s, t, k, c, tt, n;
    cin >> tt;
    for (int i = 1; i <= tt; ++i) {
        cin >> k >> c >> s;
        cout << "Case #" << i << ":";
        for (int j = 1; j <= s; ++j) {
            cout << " " << j;
        }
        cout << endl;
    }
    return 0;
}
