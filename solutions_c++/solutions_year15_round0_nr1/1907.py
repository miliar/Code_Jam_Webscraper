#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
const int N = 1100;
char s[N];

int main() {
    int o, n, cas = 0;
    scanf("%d", &o);
    while (o--) {
        scanf("%d", &n);
        scanf("%s", s);
        int res = 0, now = 0;
        for (int i = 0; i <= n; i++)
            if (s[i] != '0') {
                if (now < i) {
                    res += i - now;
                    now = i;
                }
                now += s[i] - '0';
            }
        printf("Case #%d: %d\n", ++cas, res);
    }
    return 0;
}