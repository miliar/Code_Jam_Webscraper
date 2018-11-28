#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int t, n, x, y, ptr, ptr2;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++)
    {
        scanf("%d", &n);
        double a[n];
        double b[n];
        for(int j = 0; j<n;j++)
            scanf("%lf", &a[j]);
        for(int j = 0; j<n;j++)
            scanf("%lf", &b[j]);
        sort(a, a + n);
        sort(b, b + n);

        x =  y = 0;
        ptr = n - 1;
        for(int j = n - 1;j >= 0;j--)
        {
            if(b[ptr] < a[j])
            {
                y++;
            }
            else
                ptr--;
        }
        ptr = 0;
        ptr2 = n - 1;
        for(int j = 0;j < n; j++)
        {
            if(b[ptr] > a[j])
            {
                    ptr2--;
            }
            else
            {
                if(a[j] > b[ptr2])
                {
                    x += n - j;
                    break;
                }
                else
                {
                    x++;
                    ptr++;
                }
            }
        }
        printf("Case #%d: %d %d\n", i, x, y);
    }
    return 0;
}
