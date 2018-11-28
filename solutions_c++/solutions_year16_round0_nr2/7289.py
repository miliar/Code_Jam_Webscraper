#include <algorithm>
#include <iostream>
#include <set>
using namespace std;

typedef long long ll;

int main() {
    int T;
    string s;

    cin >> T;
    for (int j = 1; j <= T; ++j) {
        cin >> s;

        cout << "Case #" << j << ": ";

        int ret = 0;
        char st = '+';

        for (int j = s.size() - 1; j >= 0; --j) {
            if (st != s[j]) {
                ++ret;
                st = s[j];
            }
        }

        cout << ret << endl;
    }
    return 0;
}
