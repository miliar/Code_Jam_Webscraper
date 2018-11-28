#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
const double eps = 1e-7;
int main()
{
    int t = 0, T;
    scanf("%d", &T);
    while(t++ < T)
    {
        double time = 0.0, cps = 2.0, C, F, X;
        cin>>C>>F>>X;
        while(1)
        {
            if(X / cps > (C / cps + X / (cps + F) + eps))
            {
                time += (C / cps);
                cps += F;
            }
            else
            {
                time += (X / cps);
                break;
            }
        }
        printf("Case #%d: %.7f\n", t, time);
    }
    return 0;
}