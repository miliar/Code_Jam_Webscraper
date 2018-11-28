#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int cse = 1;
double c, f, x;
double t = 0.0, best_time, tmp_time;
double rate = 2.0;

int main()
{
    int i, j, tst;
    scanf("%d", &tst);
    while(tst--)
    {
              scanf("%lf %lf %lf", &c, &f, &x);
              t = 0.0;
              rate = 2.0;
              best_time = (x / rate);
              tmp_time = best_time;
              
              while(tmp_time <= best_time)
              {
                             best_time = tmp_time;
                             t += (c / rate);
                             rate += f;
                             tmp_time = (t + (x / rate));
              }
              
              printf("Case #%d: %.7f\n", cse++, best_time);
    }
}
