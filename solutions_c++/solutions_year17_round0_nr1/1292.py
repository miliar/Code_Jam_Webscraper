#include <iostream>

using namespace std;

int main() {
    freopen("/Users/vino/Desktop/A-large.in", "r", stdin);
    freopen("/Users/vino/Desktop/A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        string str;
        int k;
        cin >> str >> k;
        int len = str.size();
        bool flag = true;
        int cnt = 0;
        for (int i = 0; i < len; i++) {
            if (str[i] == '-') {
                cnt++;
                for (int j = 0; j < k; j++) {
                    if (i + j >= len) {
                        flag = false;
                        break;
                    }
                    if (str[i + j] == '-') {
                        str[i + j] = '+';
                    } else {
                        str[i + j] = '-';
                    }
                }
            }
        }
        if (flag) {
            printf("%d\n",cnt);
        } else {
            printf("IMPOSSIBLE\n");
        }

    }
    return 0;
}