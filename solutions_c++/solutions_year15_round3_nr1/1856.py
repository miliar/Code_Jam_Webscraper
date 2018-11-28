#include <cmath>
#include <cstdio>
#include <algorithm>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <cstring>
#include <sstream>
#include <iostream>



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
#define	R_MAX	(20)
#define	C_MAX	(20)



int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
    	uint32 R;
		uint32 C;
		uint32 W;
		uint32	L;
		int32 i,j;
		uint32 ans;

        /* Test Case run once */
		scanf("%u %u %u", &R, &C, &W);

		ans=0;
		L = C;
		while (L > (2*W))
		{
			L -= W;
			ans+=1;
		}
		if (L == W)
		{
			ans+=W;
		}
		else
		{
			ans+= (1 + W);
		}

        /* Print */
        printf("Case #%d: %u\n", Ti, ans);
    }

    return 0;
}

