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
int T, cs, x, n, m, r;
int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    scanf("%d", &T);
    cs = 0;
    while(T--)
    {
        r = 0;
        cs++;
        scanf("%d%d%d", &x, &n, &m);
        if(n > m)
            swap(n , m);
        if(x > n && x > m)
            r = 0;
        else if((n * m) % x != 0)
            r = 0;
        else if(x == 1)
            r = 1;
        else if(x == 2)
            r = 1;
        else if(x == 3)
        {
            if(n == 1 && m == 3)
                r = 0;
            else
                r = 1;
        }
        else
        {
            if(n == 1 && m == 4)
                r = 0;
            else if(n == 2 && m == 4)
                r = 0;
            else if(n == 3 && m == 4)
                r = 1;
            else
                r = 1;
        }

        if(r == 0)
            printf("Case #%d: RICHARD\n", cs);
        else
            printf("Case #%d: GABRIEL\n", cs);
    }
    return 0;
}
