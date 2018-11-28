#include <bits/stdc++.h>
#define rep(i,a,b) for(int i=a; i<b; ++i)
#define clr(a,b) memset(a,b,sizeof(a))

using namespace std;

const int N = 1010;

char s[N];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("gcj-qualification-a.txt", "w", stdout);

    int n;
    scanf("%d", &n);
    for(int cas = 1; cas <= n; ++ cas) {
        int m;
        scanf("%d", &m);
        scanf("%s", s);
        int sum = 0;
        int ans = 0;
        for(int i=0; s[i]; ++i) {
            if(sum < i) {
                ans += i - sum;
                sum = i;
            }
            sum += s[i] - '0';
        }
        printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}
