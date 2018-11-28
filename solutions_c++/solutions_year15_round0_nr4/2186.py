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

#define X_MAX   (20)
#define R_MAX   (20)
#define C_MAX   (20)



int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32 i, j;
		int32 X, R, C;
		int32 win;

        /* Test Case run once */
        scanf("%u %u %u", &X, &R, &C);
		//printf("X: %u, R: %u, C: %u\n", X, R, C);

		win = 0;
		if ( X == 1 )
		{
			win = 1;	/* must win */
		}
		else if (X == 2)
		{
			if (((R >= 2) || (C >= 2)) && ((R*C)%X == 0))
				win = 1;
		}
		else if (X == 3)
		{
//			if (((((R/3) > 0) && (R%3==0)) && (((C/2) > 0) && (C%2==0))) ||
//				((((C/3) > 0) && (C%3==0)) && (((R/2) > 0) && (R%2==0))))
			if (((R>=3) && (C>=2)) || ((R>=2) && (C>=3)))
			{
				if ((R*C)%X == 0) win = 1;
			}
		}
		else //if (X == 4)
		{
//			if (((((R/3) > 0) && (R%3==0)) && (((C/4) > 0) && (C%4==0))) ||
//				((((C/3) > 0) && (C%3==0)) && (((R/4) > 0) && (R%4==0))))
			if (((R>=4) && (C>=3)) || ((R>=3) && (C>=4)))
			{
				if ((R*C)%X == 0) win = 1;
			}
		}

        /* Print */
        printf("Case #%d: %s\n", Ti, (win)? "GABRIEL" : "RICHARD");
    }

    return 0;
}
