#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int s[10002];

int main()
{
    int cases;
    scanf("%d", &cases);
    for( int tt = 1; tt <= cases; tt++ )
    {
        int n, m, ans = 0, p1, p2;
        scanf("%d %d", &n, &m);
        for( int i = 0; i < n; i++ ) scanf("%d", &s[i]);
        sort(s, s + n);
        p1 = 0; p2 = n - 1;
        while( p1 <= p2 )
        {
            int cnt = 0, files = 0;
            while( files < 2 && p1 <= p2 && s[p2] + cnt <= m )
            {
                cnt += s[p2--];
                files++;
            }
            while( files < 2 && p1 <= p2 && s[p1] + cnt <= m )
            {
                cnt += s[p1++];
                files++;
            }
            ans++;
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
