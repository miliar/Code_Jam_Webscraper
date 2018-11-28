#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++)
    {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double time = 0, speed = 2;
        while (1)
        {
            double needTime1 = X / speed;
            double needTime2 = C / speed + X / (speed + F);
            if (needTime2 < needTime1)
            {
                time += C / speed;
                speed += F;
            }
            else
            {
                time += needTime1;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", cases, time);
    }
    return 0;
}
