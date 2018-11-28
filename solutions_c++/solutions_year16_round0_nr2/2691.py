#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int ca;
    freopen("/Users/leo/Development/py/codejam/data.in", "r", stdin);
    freopen("/Users/leo/Development/py/codejam/data.out", "w", stdout);
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        string s;
        int count = 0;
        cin >> s;
        char pre = s[0];
        s.erase(0, 1);
        for (auto cur: s) {
            if (cur == pre) continue;
            pre = cur;
            count ++;
        }
        if (pre == '-') count ++;
        cout << "Case #" << i + 1 << ": " << count << endl;
    }
}