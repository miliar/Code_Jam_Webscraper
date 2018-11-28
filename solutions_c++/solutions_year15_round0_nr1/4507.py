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
#define S_MAX   (1000)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
		int32 s_max;
    	char str[S_MAX+1];
		int32 sum_of_s;
        int32 i, j;
		int32 num_invite;

        /* Test Case run once */
        scanf("%d %s", &s_max, &str);
		sum_of_s = 0;
		num_invite = 0;
		for (i=0; i <= s_max; i++)
		{
			if ((str[i] > '0') && (sum_of_s < i))
			{
				num_invite += (i - sum_of_s);
				sum_of_s += num_invite;
			}
			sum_of_s += (str[i] - '0');
		}

        /* Print */
        printf("Case #%d: %u\n", Ti, num_invite);
    }

    return 0;
}
