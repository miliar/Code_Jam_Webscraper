#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

char s[128];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T, len; scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%s", s);
        len = strlen(s);

        int ans = 0;
        for(int i=len-1; i>=0; i--) {
            if (s[i] == '+') continue;

            ans++;
            while(i!=0 && s[i-1]=='-') i--;
            for(int j=i-1; j>=0; j--) {
                if (s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }

        printf("Case #%d: %d\n", ncase, ans);
    }

    return 0;
}
