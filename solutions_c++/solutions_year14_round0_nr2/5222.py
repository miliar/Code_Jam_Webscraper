#include <cstdio>
using namespace std;

int main()
{
    double c, f, x, t;

    scanf("%lf", &t);
    for(int i=1; i<=t; i++)
    {
        double total = 0;
        double cps = 2;
        bool ok = true;

        scanf("%lf%lf%lf", &c, &f, &x);

        while(ok)
        {
            double time = x/cps;
            double buytime = c/cps + x/(cps+f);

            if(buytime < time)
            {
                total += c/cps;
                cps += f;
            }
            else ok = false;
        }
        printf("Case #%d: %.7lf\n", i, total + x/cps);
    }
    return 0;
}
