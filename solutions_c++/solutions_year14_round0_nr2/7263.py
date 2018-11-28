#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

double solve(double c, double f, double x)
{
    double speed = 2;
    double base_time = 0;

    do
    {
        double x_time = x / speed;
        double y_time = x / (speed + f) + c / speed;
        //printf("%lf %lf %lf\n", x_time, y_time, base_time);

        if(y_time < x_time)
        {
            base_time += c / speed;
            speed += f;
        }

        else
        {
            return base_time + x_time;
        }
    }
    while(true);

    return 0;
}

int main()
{

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int nca;
    scanf("%d", &nca);

    for(int ii = 1; ii <= nca; ii++)
    {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        printf("Case #%d: %lf\n", ii, solve(c, f, x));
    }

    return 0;
}