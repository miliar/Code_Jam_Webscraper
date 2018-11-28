#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

double s1[1002], s2[1002];

int main()
{
    int cases;
    scanf("%d", &cases);
    for( int tt = 1; tt <= cases; tt++ )
    {
        int n, cnt1 = 0, p1, p2, cnt2 = 0;
        scanf("%d", &n);
        p1 = p2 = n - 1;
        for( int i = 0; i < n; i++ ) scanf("%lf", &s1[i]);
        for( int i = 0; i < n; i++ ) scanf("%lf", &s2[i]);
        sort(s1, s1 + n);
        sort(s2, s2 + n);
        for( int i = n - 1; i >= 0; i-- )
        {
            if( s1[p1] > s2[i] )
            {
                cnt1++;
                p1--;
            }
            if( s2[p2] > s1[i] )
            {
                cnt2++;
                p2--;
            }
        }
        printf("Case #%d: %d %d\n", tt, cnt1, n - cnt2);
    }
    return 0;
}
