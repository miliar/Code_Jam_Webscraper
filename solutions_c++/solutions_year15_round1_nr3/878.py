#include <stdio.h>
#include <algorithm>
using namespace std;


typedef struct pp
{
    long long int  x;
    long long int y;
}Pointa;


Pointa p[10000000];

int ccw(Pointa a, Pointa b, Pointa c) {
    long long int area = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    if (area > 0)
        return -1;
    else if (area < 0)
        return 1;
    return 0;
}


void solve()
{

    int n;
    scanf("%d",&n);
    printf("\n");
    for (int i=0;i<n;i++) 
    {
        scanf("%lld %lld",&p[i].x, &p[i].y);
    }
    if ( n==1) { printf("0\n"); return; }
    if ( n==2) {printf("0\n");printf("0\n");return; }
    for (int i=0;i<n;i++)
    {
        int ans = 100000000;

        for (int j=0;j<n;j++)
        {
           if ( i == j ) continue;
           
            int a1 = 0 ,a2=0;
            for (int k=0;k<n;k++)
            {
                int X = ccw(p[i], p[j], p[k]); 
                if ( X > 0 ) a1++;
                if ( X < 0 ) a2++;

            }
            if ( a1 < ans ) ans = a1;
            if ( a2 < ans ) ans = a2;
        }
        printf("%d\n",ans);
    }
    
}

int main()
{
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }

    return 0;
}
