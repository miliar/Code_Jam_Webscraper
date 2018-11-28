#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    string s;
    int len;
    for (int j = 1; j <= T; j++) {
        cin >> s;
        len = s.length();
        int temp = 1;
        int ans = 0;
        for (int i = len - 1; i >= 0; i--) {
            if ((temp == 1 && s[i] == '-') || (temp == -1) && s[i] == '+') {
                temp *= -1;
                ans++;
            }
        }
        printf("Case #%d: %d\n", j, ans);
    }
    return 0;
}
