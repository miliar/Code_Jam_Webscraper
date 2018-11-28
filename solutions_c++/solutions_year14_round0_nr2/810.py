#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{

    int t;
    scanf("%d",&t);
    for (int l=1;l<=t;l++)
    {
        double c,f,x;
        printf("Case #%d: ",l);
        scanf("%lf %lf %lf",&c,&f,&x); 

        double seconds = 0.0;
        double rate = 2.0;
        double ans = x/2;
        while ( 1 )
        {
            ans = min(ans,seconds + x/rate );
            seconds += c/rate;
            rate += f;
            if ( seconds > ans ) break;

        }
        printf("%.7lf\n",ans);
    }
    return 0;
}
