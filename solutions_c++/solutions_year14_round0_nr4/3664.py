#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    int t, n, p=1, i, x=0, y=0, j;
    scanf("%d", &t);
    while(t--)
    {
        x=0;y=0;
        scanf("%d", &n);
        double na[n], ke[n];
        for(i=0;i<n;i++)
            scanf("%lf", &na[i]);
        for(i=0;i<n;i++)
            scanf("%lf", &ke[i]);
        sort(na, na+n);
        sort(ke, ke+n);
        i=0;j=0;
        while((i<n) && (j<n))
        {
            if(na[i]<ke[j])
            {
                y++;
                i++;
                j++;
            }
            else
                j++;
        }
        i=0;j=0;
        while((i<n) && (j<n))
        {
            if(na[i]>ke[j])
            {
                i++;j++;x++;
            }
            else
                i++;
        }
        y = n-y;
        printf("Case #%d: %d %d\n", p, x, y);
        p++;
    }
    return 0;
}
