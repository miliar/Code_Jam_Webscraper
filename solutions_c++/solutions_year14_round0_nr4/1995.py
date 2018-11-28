#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    double a[1005], b[1005];
    int T, n, cas = 0, i, j;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        for(i = 0; i < n; i++)
            scanf("%lf",&a[i]);
        for(j = 0; j < n; j++)
            scanf("%lf",&b[j]);
        sort(a, a+n);
        sort(b, b+n);
        i = 0;
        int p = 0, q = n - 1;
        int ans1 = 0, ans2 = 0;
        while(i < n)
        {
            if(a[i] > b[p])
            {
                ans1++;
                p++;
                i++;
            }
            else
            {
                i++;
                q--;
            }
        }
        i = 0, p = 0;
        while(p < n)
        {
            if(a[i] < b[p])
            {
                i++;
                p++;
                ans2++;
            }
            else
                p++;
        }
        printf("Case #%d: %d %d\n",++cas, ans1, n-ans2);
    }
    return 0;
}
