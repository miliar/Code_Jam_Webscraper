#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long LL;

bool vis[10];

int main()
{
//    freopen("A-large.in", "r", stdin);
//    freopen("out.out", "w", stdout);
    int T;

    cin>>T;
    int Case = 0;
    while (T--) {
        memset(vis, false, sizeof(vis));
        ++Case;
        LL N;
        cin>>N;
        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", Case);
        } else {
            int Count = 0;
            int i = 1;
            while (Count < 10) {
                LL t = N*i;
                while (t) {
                    if (!vis[t%10]) {
                        vis[t%10] = true;
                        ++Count;
                    }
                    t /= 10;
                }
                ++i;
            }
            LL ans = N *(i-1);
            printf("Case #%d: %I64d\n", Case, ans);
        }
    }
    return 0;
}
