#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long ll;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    char s[105];
    for (int it = 1; it <= t; ++it) {
        scanf("%s", s);
        int n = strlen(s), ans = 0;
        for (int j = 0; j < n;) {
            if (s[j] == '+') {
                ++j;
                continue;
            }
            int sv = j;
            while (j < n && s[j] == '-') ++j;
            if (sv == 0) ans++;
            else ans += 2;
        }
        printf("Case #%d: %d\n", it, ans);
    }
    return 0;
}