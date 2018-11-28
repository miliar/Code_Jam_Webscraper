#include <iostream>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <limits.h>
#include <set>
#include <stack>
using namespace std;
int main()
{
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("B-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i =1;i<=t;i++)
    {
        int a,b,k;
        long long win=0;
        scanf("%d %d %d",&a,&b,&k);
        for(int j =0;j<a;j++)
        {
            for(int s=0;s<b;s++)
            {
                if((s&j)<k)
                {
                    win++;
                }
            }
        }
        printf("Case #%d: %lld\n",i,win);
    }
    return 0;
}



