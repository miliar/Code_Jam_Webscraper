#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<cstdlib>
using namespace std;

void solve()
{
    double c,f,x; // c cost f extra cookie x win fee
    scanf("%lf%lf%lf",&c,&f,&x);
    double _cookit_rate = 2;
    double ans = 0;
    for(;;)
    {
        double no_farm_time = (x)/_cookit_rate;
        double yes_farm_time = (x)/(_cookit_rate+f) + c/_cookit_rate;
       // printf("%.5lf %.5lf\n",yes_farm_time,no_farm_time);
        if(yes_farm_time<no_farm_time)
        {
            ans += c/_cookit_rate;
            _cookit_rate += f;
        }
        else
        {
            ans += no_farm_time;
            break;
        }
    }
    printf("%.10lf\n",ans);
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
