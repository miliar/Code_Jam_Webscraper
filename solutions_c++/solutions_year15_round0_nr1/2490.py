#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int n, t;
int main() {
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &t);
    string s;
    for(int cas = 1; cas <= t; cas++) {
        scanf("%d", &n);
        cin >> s;
        long long tmp = s[0] - '0', ans = 0;
        for(int i = 1; i <= n; i++) {
            if(tmp < i) {
                ans += i - tmp;
                tmp = i;
            }
            tmp += s[i] - '0';
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
