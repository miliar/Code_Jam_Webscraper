#include <iostream>
#include <cstdio>
#define eps 0.00000001
using namespace std;
double c, f, x;
bool judge(double rate)
{
    double t1 = x/rate;
    double t2 = c/rate + (x)/(rate+f);
    if (t1<=t2) return false;
    else return true;
}
int main()
{
    int t, n=1;
    freopen("B-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    cin>>t;
    while (t--)
    {
        cout<<"Case #"<<n++<<": ";
        scanf("%lf%lf%lf", &c, &f, &x);
        double rate = 2.0, ans = 0;
        while (1)
        {
            if (judge(rate))
            {
                ans += c/rate;
                rate += f;
            }
            else
            {
                ans += x/rate;
                break;
            }
        }
        printf("%.7lf\n", ans);
    }
    return 0;
}
