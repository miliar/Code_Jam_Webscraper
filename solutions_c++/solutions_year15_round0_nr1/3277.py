#include <iostream>
#include <cstdio>

using namespace std;
char sa[1005];

int main()
{
//freopen("in", "r", stdin);
//freopen("out", "w", stdout);
    int T, ca = 1;
    scanf("%d", &T);
    while(T--) {
        int n;
        scanf("%d", &n);
        scanf("%s", sa);

        int cnt = 0, ans = 0, a;
        for(int i = 0; i <= n; ++i) {
            a = sa[i]-'0';
            int cc = i-cnt;

            if(cc > 0 && a != 0) {
                ans += cc;
                cnt += cc;
            }
            cnt += a;
        }

        printf("Case #%d: %d\n", ca++, ans);
    }
    return 0;
}
