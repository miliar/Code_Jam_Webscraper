#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>

#define INF (1<<30)
#define mod 666013

using namespace std;
int T, cs, x, y, r, i, n;
char s[2005];
int main()
{
    //freopen("1.in", "r", stdin);
    //freopen("1.out", "w", stdout);
    scanf("%d", &T);
    cs = 0;
    while(T--)
    {
        cs++;
        scanf("%d ", &n);
        gets(s);
        x = r = 0;
        for(i = 0; i <= n; i++)
        {
            y = s[i] - '0';
            if(!y)
                continue;
            if(i > x)
            {
                r += i - x;
                x = i;
            }
            x += y;
        }
        printf("Case #%d: %d\n", cs, r);
    }
    return 0;
}
