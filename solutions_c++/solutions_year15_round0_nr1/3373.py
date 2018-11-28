#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define LL long long
char s[5000];
int n;

int main()
{
    freopen("test.txt", "w", stdout);
    freopen("test1.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    for(int ii = 1; ii <= T; ii++)
    {
        scanf("%d%s", &n, s);
        LL ans = 0;
        LL add = 0;
        for(int i = 0; i <= n; i++)
            if(s[i] - '0' != 0)
            {
                int p = s[i] - '0';
                if(ans < i) { add += (i - ans); ans += (i - ans);  }
                ans += p;
            }
        printf("Case #%d: %d\n", ii, add);
    }
    return 0;
}
