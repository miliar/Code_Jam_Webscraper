#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
#define pi acos(-1)
#define eps 1e-9

long long r,t;
double temp;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    long long left,right,mid,ans;
    int ca,c = 1;
    scanf("%d",&ca);
    while(ca--)
    {
        ans = 0;
        cin >> r >> t;
        left = 0;
        right = 707106780;
        while(left <= right)
        {
            mid = (left + right) >> 1;
            int t1,t2;
            t1 = int(log(r * 1.0) / log(10.0) + 1 - eps);
            t2 = int(log(mid * 1.0) / log(10.0) + 1 - eps);
            if(t1 + t2 > 18 || mid*(2*r+2*mid-1) > t) right = mid - 1;
            else 
            {
                left = mid + 1;
                ans = max(ans,mid);
            }
        }
        printf("Case #%d: %lld\n",c++,ans);
    }
    return 0;
}
