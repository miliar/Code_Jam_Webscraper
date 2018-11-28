#include <iostream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <memory>
#include <ctime>

#define FILE

using namespace std;

char s[100];
char s1[100];
char s2[100];

void solve() {
    scanf("%s", s);
    int l = strlen(s);

    long long ans = 0;
    long long n;
    sscanf(s, "%I64d", &n);
    if (n % 10 == 0) {
        n--;
        ans++;
        sprintf(s, "%I64d", n);
        l = strlen(s);
    }

    if (l == 1) {
        printf("%I64d\n", n + ans);
        return;
    }

    if (l == 2) {
        if (s[0] > '1') {
            printf("%I64d\n", 10 + s[1] - '0' + s[0] - '0' + ans);
        } else {
            printf("%I64d\n", n + ans);
        }
        return;
    }
    int l1 = l / 2;
    int l2 = l - l1;
    memcpy(s1, s, l1);
    s1[l1] = 0;
    memcpy(s2, s + l1, l2);
    s2[l2] = 0;

    bool b = true;
    if (s1[0] != '1')
        b = false;
    for (int i = 1; i < l1; i++)
        if (s1[i] != '0')
            b = false;

    reverse(s1, s1 + l1);
    int n1, n2;
    sscanf(s1, "%d", &n1);
    sscanf(s2, "%d", &n2);
    long long o[100];
    o[0] = 1;
    for (int i = 1; i < 100; i++)
        o[i] = o[i - 1] * 10;
    long long c = 0;
    for (int i = 2; i < l; i++) {
        int i1 = i / 2;
        int i2 = i - i1;
        c += o[i1] - 1 + o[i2] - 1;
    }
    c += l - 3;
    ans += c + 11 + n1 + n2 - b;
    printf("%I64d\n", ans);
}

int main() {
#ifdef FILE
    freopen("E:/1.in", "r", stdin);
    freopen("E:/1.out", "w", stdout);
#endif // FILE

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
