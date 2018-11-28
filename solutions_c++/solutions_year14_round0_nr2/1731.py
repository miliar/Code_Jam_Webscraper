#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int T,ii;
    freopen("B-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    cin>>T;
    for(ii = 1; ii <= T;++ii)
    {
        double x,c,f,ans,sum = 0.0;
        cin>>c>>f>>x;
        ans = x / 2.0;
        sum = ans;
        double speed = 2.0;
        while(true)
        {
            sum -= x/speed;
            sum += c/speed;
            speed += f;
            sum += x/speed;
            if(ans < sum)
                break;
            ans = min(ans, sum);
        }
        printf("Case #%d: %.7f\n", ii, ans);
    }
    return 0;
}
