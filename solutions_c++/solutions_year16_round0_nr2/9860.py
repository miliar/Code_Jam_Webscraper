#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int maxn = 120;
char s[maxn];
int len, v[maxn];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T, kase = 0; scanf("%d", &T);
    while(T--) {
        scanf("%s", s);
        int len = strlen(s);
        for(int i = 0; i < len; ++i)
            v[i] = s[i] == '+';
        int tot = 0, pre = 0;
        for(int i = len-1; i >= 0; --i) {
            int cur = (v[i] + pre) % 2;
            if(cur == 0) {
                int j = i;
                while(j >= 0 && (v[j]+pre)%2 == 0)
                    --j;
                ++pre;
                ++tot;
                i = j+1;
            }
        }
        printf("Case #%d: %d\n", ++kase, tot);
    }
    return 0;
}
