#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;
int n;

long long lowest(long long pos) {
	long long leave = 1 << n;
	long long rank = 0;
	for (int i = 1; i <= n; i++){
	    if (pos == 0) break;
        rank += leave / 2;
        pos = (pos - 1) >> 1;
        leave = leave / 2;
	}
	return rank + 1;
}


long long highest(long long p)
{
    long long ans = (1 << n);
    long long temp = (1 << n) / 2;
    p = (1 << n) - p - 1;
    while (p != 0)
    {
        ans -= temp;
        p = (p - 1) /2;
        temp = temp / 2;
    }
    return ans;
}
int main()
{
    int times;
    int p;
    long long l,r,mid;
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    scanf("%d",&times);
    for (int t = 0; t < times; t++)
    {
        scanf("%d %d",&n,&p);
        l = 0; r = (1 << n) - 1;

        while (r-l > 1)
        {
            mid = (l+r) / 2;
            if (lowest(mid) <= p) l = mid;
            else r = mid;
        }
        int i;
        if (lowest(r) <= p) l = r;
        printf("Case #%d: %d ",t+1,l);
        l = 0; r = (1 << n) -1;
        while (r-l > 1)
        {
            mid = (l+r) / 2;
            if (highest(mid) <= p) l = mid;
            else r = mid;
        }
        if (highest(r)<= p) l = r;
        printf("%d\n",l);
    }
}
