#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <utility>
#include <climits>
#include <unordered_set>
#include <set>
using namespace std;

void reverse(string& s, int bottom) {
    int i = 0, j = bottom;
    while (i <= j) {
        if (s[i] == s[j]) {
            if (s[i] == '-') s[i] = s[j] = '+';
            else s[i] = s[j] = '-';
        }
        ++i;
        --j;
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        cin >> s;
        int count = 0;
        int bottom = s.size() - 1, begin = 0;
        while (bottom >= 0) {
            if (s[bottom] == '+') {
                --bottom;
            } else {
                begin = 0;
                while (s[begin] == '+') ++begin;
                if (begin > 0) {
                    reverse(s, begin - 1);
                    ++count;
                }
                reverse(s, bottom);
                ++count;
            }
        }
        cout << "Case #" << t << ": " << count << endl;
    }
    return 0;
}

