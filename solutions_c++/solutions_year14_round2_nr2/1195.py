#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


void solve()
{

    int a ,b,k;
    scanf("%d %d %d",&a,&b,&k);

    long long int ans = 0;
    for (int i=0;i<a;i++)
        for (int j=0;j<b;j++)
        {
            int x = i&j;
            if ( x < k ) 
            {
                ans++;
            }
        }
    printf("%lld\n",ans);
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

}
