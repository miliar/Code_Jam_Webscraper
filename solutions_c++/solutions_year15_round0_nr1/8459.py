#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
#include "delete_this.hpp"
#define t(...) debug(#__VA_ARGS__, __VA_ARGS__);
#else
#define t(...)
#endif

void sol() {
    int smax;
    string s;
    scanf("%d", &smax);
    cin >> s;
    int org = 0;
    int ans = 0;
    if (s[0] == '0') {
        org = 1;
        ans++;
    } else {
        org += s[0] - '0';
    }
    for (int butuh = 1; butuh <= smax; butuh++) {
        if (butuh <= org) {
            org += s[butuh] - '0';
        } else {
            int baru = butuh - org;
            ans += baru;
            org += baru;
            org += s[butuh] - '0';
        }   
    }
    printf("%d", ans);
}

int main() {
    int qwe;
    cin >> qwe;
    for (int i = 0; i <= qwe - 1; i++) {
        printf("Case #%d: ", i + 1);
        sol();
        puts("");
    }
    return 0;
}