#include <bits/stdc++.h>
using namespace std;

int main() {
    int tc, x = 1, ans;
    for(scanf("%d", &tc); tc--; printf("Case #%d: %d\n", x++, ans)) {
        char s[102];
        scanf("%s", s);

        ans = 0;
        bool first = true, curr = false;
        for(int i=0; s[i]; i++) {
            if(s[i] == '-') {
                curr = true;
            } else {
                if(curr) {
                    if(first) {
                        ans++;
                    } else {
                        ans += 2;
                    }
                    curr = false;
                }
                first = false;
            }
        }

        if(curr) {
            if(first)
                ans++;
            else
                ans += 2;
        }
    }

    return 0;
}