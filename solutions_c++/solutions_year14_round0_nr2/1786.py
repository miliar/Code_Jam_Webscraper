#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

#define debug if(0)

using namespace std;

int main()
{
    int t,caseno=1;
    double c,f,x,ans,last,cur,rate,now;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        ans = x/2.0;
        rate = 2.0L;
        last=0.0;
        while(1)
        {
            cur = c/rate;
            rate = rate+f;
            now = last+cur+x/rate;
            last = last + cur;
            debug cout<<ans<<" "<<now<<" "<<rate<<endl;
            if(now>ans)
                break;
            else
                ans = now;
        }
        printf("Case #%d: %0.7lf\n",caseno++,ans);
    }
    return 0;
}
