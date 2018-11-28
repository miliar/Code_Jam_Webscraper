#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;
string str;
int len, T;
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        cin >> str >> len;
        int ans = 0;
        for(int i = 0; i <= str.size() - len; ++i) {
            if(str[i] == '-') {
                ans++;
                for(int j = 0; j < len; ++j) {
                    if(str[i + j] == '+')
                        str[i + j] = '-';
                    else
                        str[i + j] = '+';
                }
            }
        }
        for(int i = str.size() - len; i < str.size(); ++i) {
            if(str[i] == '-') {
                ans = -1;
            }
        }
        if(ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", test);
        }
        else {
            printf("Case #%d: %d\n", test, ans);
        }
    }
    return 0;
}