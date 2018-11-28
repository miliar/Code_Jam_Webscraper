#include<stdio.h>
#include<algorithm>
using namespace std;
#define nmax 10005
int t, ii, n, k, v[nmax], i, p1, p2, rez;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%ld",&t);
    for (ii=1;ii<=t;ii++)
    {
        scanf("%ld %ld",&n,&k);
        for (i=1;i<=n;i++)
            scanf("%ld",&v[i]);
        sort(v+1,v+1+n);
        p2=n;   rez=n;
        for (p1=1;p1<=n;p1++)
        {
            while ((v[p1]+v[p2]>k)&&(p2>p1))
                p2--;
            if (p1<p2)
            {   rez--;  p2--;   }
            else
                break;
        }
        printf("Case #%ld: %ld\n",ii,rez);
    }
    return 0;
}
