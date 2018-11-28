#include <iostream>
#include <cstdio>
#include <set>
#include <cstring>

using namespace std;
const int maxn = 1e4+5;
int cnt[maxn];

int cal(int s)
{
    int sum = 0;
    for(int i = s+1; i <= 1001; ++i) {
        if(cnt[i]) {
            int c = i/s;
            if(i%s == 0) c--;
            sum += c*cnt[i];
        }
    }
     return sum + s;
}
int main()
{
//freopen("in", "r", stdin);
//freopen("out", "w", stdout);
    int T, ca = 1;
    scanf("%d", &T);
    while(T--) {
        int n, a, mx = 0;
        memset(cnt, 0, sizeof(cnt));

        scanf("%d", &n);

        for(int i = 0; i < n; ++i) {
            scanf("%d", &a);
            cnt[a]++;
            mx = max(mx, a);
        }

        int ans = mx, tmp = 0;
        for(int i = 1; i < 1001; ++i) {
            ans = min(cal(i), ans);
            //?if(ans == 4) printf("%d\n", i);
        }
        printf("Case #%d: %d\n", ca++, ans);
    }
    return 0;
}
