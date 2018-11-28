#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int m;
        string s;
        cin >> m >> s;

        int c = 0, q = 0;
        for(int i = 0; i <= m; ++i) {
            if(q >= i) {
                q += s[i]-'0';
            } else {
                int d = i-q;
                q += d+s[i]-'0';
                c += d;
            }
        }

        printf("Case #%d: %d\n", t, c);
    }
    return 0;
}

