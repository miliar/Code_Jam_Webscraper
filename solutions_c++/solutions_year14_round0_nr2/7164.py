#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

#define N 10000005
#define M
#define LL __int64
#define INF 0x3f7f7f7f


int main(void)
{
//    freopen("in.in", "r", stdin);
//    freopen("out.out", "w", stdout);
    int TC, tc;
    double x, c, f, ans, sum, bon, temp, reac;
    scanf("%d", &TC);
    for(tc = 1; tc <= TC; tc++)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        ans = x / 2.0;  temp  = 0;  bon = 2.0;
       // printf("%f %f \n", c, bon);
        while(true)
        {
            reac = (c / bon);
            //printf("%f\n", reac);   system("pause");
            temp += reac;   bon += f;   sum = 0;
            if(ans > temp + x / bon)    ans = temp + x / bon;
            else break;

        }
        printf("Case #%d: %.7f\n", tc, ans);
    }
    return 0;
}
