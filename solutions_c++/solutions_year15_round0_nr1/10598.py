#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    int i, t, j, count, ans, n;
    string s;
    scanf("%d", &t);

    for (j = 1; j <= t; j++) {
        scanf("%d", &n);
        cin >> s;
        ans = 0;
        count = 0;
        count = s[0]-48;
        for (i = 1; i <= n; i++) {
          //      cout << count << "  " << ans  << endl;
           if (count >= n) {
                break;
           }
            if (i > count) {
                ans += i - count;
                count = i;
                }
            count += s[i] - 48;

            }
        printf("Case #%d: %d\n", j, ans);
        }
    return 0;
    }
