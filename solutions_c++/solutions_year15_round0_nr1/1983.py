#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;

char s[1111];
int sm;

int solve() {
    for(int i = 0;i <= sm; i++) {
        int cur = i;
        bool flag = true;
        for(int j = 0;j <= sm; j++) {
            if(cur < j) {
                flag = false;
                break;
            }
            cur += s[j]-'0';
        }
        if(flag)    return i;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 1;
    scanf("%d", &t);
    while(t--) {
        scanf("%d%s", &sm, s);
        printf("Case #%d: %d\n", cas++, solve());
    }
    return 0;
}
