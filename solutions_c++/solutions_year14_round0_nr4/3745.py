#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    int t, n, p=1, i, w=0, dw=0, j;
    scanf("%d", &t);
    while(t--)
    {
        w=0;dw=0;
        scanf("%d", &n);
        double a[n], b[n];
        for(i=0;i<n;i++)
            scanf("%lf", &a[i]);
        for(i=0;i<n;i++)
            scanf("%lf", &b[i]);
        sort(a, a+n);
        sort(b, b+n);
        i=0;j=0;
        while((i<n) && (j<n))
        {
            if(a[i]>b[j])
            {
                i++;j++;w++;
            }
            else
                i++;
        }
        i=0;j=0;
        while((i<n) && (j<n))
        {
            if(a[i]<b[j])
            {
                dw++;
                i++;
                j++;
            }
            else
                j++;
        }
        dw = n-dw;
        printf("Case #%d: %d %d\n", p, w, dw);
        p++;
    }
    return 0;
}
