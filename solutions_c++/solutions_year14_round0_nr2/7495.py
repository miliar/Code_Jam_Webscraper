#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 1000;

int T;
double C,F,X;


double cur = 0;
double speed = 2;
double ans = 0;

inline double curtime()
{
    return cur + (X/speed);
}
inline double buytime()
{
    return cur + (C/speed) + (X/(speed + F));
}


int main()
{
    scanf("%d",&T);
    // ios::sync_with_stdio(0);
    // cin >> T;
    for (int tt = 1; tt <= T; ++tt)
    {
        // cin >> C >> F >> X;
        scanf("%lf%lf%lf",&C,&F,&X);
        cur = ans = 0;
        speed = 2;
        while(1)
        {
            if( buytime() < curtime() )
            {
                cur += (C/speed);
                speed += F;
                ans = buytime();
            }
            else
            {
                ans = curtime();
                break;
            }
        }

        // cout << "Case #" << tt << ": " << ans << endl;
        printf("Case #%d: %.7lf\n",tt,ans); // 
    }

    return 0;
}