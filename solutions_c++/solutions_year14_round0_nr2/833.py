#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define T_MAX   (100)

#define C_MAX   (10000.0)
#define F_MAX   (100.0)
#define X_MAX   (100000.0)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32 i, j;
        double C, F, X;
        double rate, total_time;
        double evl_time;
        double buy_time;

        /* Test Case run once */
        rate = 2.0; /*init*/
        total_time = 0.0;

        scanf("%lf %lf %lf", &C, &F, &X);

        while (1)
        {
            evl_time = X / rate;
            buy_time = C / rate;
            if ((evl_time - buy_time) * (rate + F) > X)
            {
                total_time += buy_time;
                rate += F;
            }
            else
            {
                total_time += evl_time;
                break;
            }
        }


        /* Print */
        printf("Case #%d: %.7f\n", Ti, total_time);
    }

    return 0;
}
