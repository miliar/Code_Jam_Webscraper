#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int ti;scanf("%d",&ti);
    for(int ca=1; ca<=ti; ca++)
    {
        double c,f,x;scanf("%lf%lf%lf",&c,&f,&x);
        double ans = x/2;
        double time = 0;
        double speed = 2;
        for(int buy = 0; time <= ans; buy ++)
        {
            ans = min(ans, time + x/speed);
            time += c/speed;
            speed += f;
        }
        printf("Case #%d: %.7f\n",ca,ans);
    }
}
