#include <bits/stdc++.h>
using namespace std;

char s[1010];
int main() {
    int t;
    scanf("%d", &t);
    for(int ca = 1; ca <= t; ++ca) {
        int range;
        scanf("%s%d", s, &range);
        int cnt = 0;
        for(int cur = 0; cur < strlen(s) - range + 1; ++cur) {
            if(s[cur] != '+') {
                for(int i = 0; i < range; ++i) {
                    s[cur+i] = (s[cur+i] == '+' ? '-' : '+');
                }
                ++cnt;
            }
        }
        bool succ = true;
        for(int i = 0; i < strlen(s); ++i) if(s[i] != '+') {
            succ = false;
            break;
        }
        printf("Case #%d: ", ca);
        if(succ) printf("%d\n", cnt);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}

