#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
const int inf = 1e4+5;
int m[1005];

int main()
{
//freopen("in", "r", stdin);
//freopen("out", "w", stdout);
    int T, ca = 1;
    scanf("%d", &T);
    while(T--) {
        memset(m, 0, sizeof(m));
        int n;
        scanf("%d", &n);
        int tmp = -inf;
        for(int i = 0; i < n; ++i) {
            scanf("%d", &m[i]);
            if(i != 0) {
                if(m[i] <= m[i-1])
                    tmp = max(tmp, m[i-1]-m[i]);
            }
        }
        int ans1 = 0, ans2 = 0;
        for(int i = 1; i < n; ++i) {
            if(m[i] < m[i-1]) {
                ans1 += m[i-1]- m[i];
            }
            ans2 += min(tmp, m[i-1]);
        }

        printf("Case #%d: %d %d\n", ca++, ans1, ans2);
    }
    return 0;
}
