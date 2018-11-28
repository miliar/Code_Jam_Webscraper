/*
5
-
-+
+-
+++
--+-
*/
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main() {
    int T;
    char str[200];
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%s", str);
        int len = strlen(str), flip = 0, cnt = 0;
        for (int i = len - 1; i >= 0; --i) {
            if ((str[i] == '-') ^ flip) {
                cnt++;
                flip ^= 1;
            }
        }
        printf("Case #%d: %d\n", ca, cnt);
    }
    return 0;
}
