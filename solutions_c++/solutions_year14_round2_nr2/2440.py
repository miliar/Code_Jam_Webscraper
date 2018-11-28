#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,a,b,k;
    scanf("%d",&t);
    int cas = 1;
    while(t--)
    {
        scanf("%d %d %d",&a,&b,&k);
        int ans = 0;
        for(int i=0;i<a;i++)
            for(int j=0;j<b;j++)
                if( (i&j) < k)
                    ans++;
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
