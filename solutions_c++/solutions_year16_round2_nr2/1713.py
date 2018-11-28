#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

bool match(string s, int x) {
    for (int len = s.size() - 1; len >= 0; len--) {
        if (s[len] == '?' || s[len] - '0' == x % 10) {
        } else {
            return false;
        }
        x /= 10;
    }

    if (x > 0) return false;

    return true;
}

string tos(int x, int len) {
    string res;
    for (int i = 0; i < len; i++) {
        if (x > 0) {
            res.push_back('0' + (x % 10));
        } else {
            res.push_back('0');
        }
        x /= 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main(int argc, char *argv[])
{
    int T = 0;
    cin >> T;

    for (int cas = 1; cas <= T; cas++) {
        string x;
        string y;
        cin >> x;
        cin >> y;

        int rx = 0, ry = 0;
        int mind = 1024000;
        for (int i = 0; i < 1000; i++) {
            if (!match(x, i)) {
                continue;
            }
            for (int j = 0; j < 1000; j++) {
                if (match(y, j)) {
                    int a = abs(i - j);
                    if (a < mind || (a == mind && (i < rx || (i == rx && j < ry)))) {
                        mind = a;
                        rx = i, ry = j;
                    }
                }
            }
        }
        int sz = x.size();

        // cout << "Case #" << cas << ": " << tos(rx, sz) << " " << rx
        // << " " << tos(ry, sz) << " " << ry << " " << mind << endl;
        cout << "Case #" << cas << ": " << tos(rx, sz)
             << " " << tos(ry, sz) << endl;
    }
    
    return 0;
}
