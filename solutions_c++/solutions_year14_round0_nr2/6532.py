/*********************************************************************************
*     File Name           :     B.cpp
*     Created By          :     YIMMON, yimmon.zhuang@gmail.com
*     Creation Date       :     [2014-04-12 09:28]
*     Last Modified       :     [2014-04-12 15:35]
*     Description         :
**********************************************************************************/

#include  <iostream>
#include  <cstdio>
#include  <cstring>
#include  <cmath>
using namespace std;

int T;
double c, f, x;

double solve()
{
    double ret = 0, r = 2;
    for(;;)
    {
        double a = c/r + x/(r+f);
        double b = x/r;
        if(a < b)
            ret += c/r, r+=f;
        else{
            ret += b;
            break;
        }
    }
    return ret;
}

int main(int argc, char *argv[])
{
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        printf("Case #%d: %.7f\n", cas, solve());
    }
    return 0;
}
