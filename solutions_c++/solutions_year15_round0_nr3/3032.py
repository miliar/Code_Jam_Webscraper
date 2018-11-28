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

#define	DBG(...)

#define T_MAX   (100)
#define L_MAX   (10000)

//#define X_MAX   (10000000000000000)
#define X_MAX   (10000)


char str[X_MAX+1];

int multiply(int sign, char a, char b, int *nSign, char *c)
{
	if (a == 'i')
	{
		if (b == 'i')
		{
			*nSign = sign * -1;
			*c = '1';
		}
		else if (b == 'j')
		{
			*c = 'k'; 
		}
		else if (b == 'k')
		{
			*nSign = sign * -1;
			*c = 'j';
		}
		else
			return -1;
	}
	else if (a == 'j')
	{
		if (b == 'i')
		{
			*nSign = sign * -1;
			*c = 'k';
		}
		else if (b == 'j')
		{
			*nSign = sign * -1;
			*c = '1';
		}
		else if (b == 'k')
		{
			*c = 'i';
		}
		else
			return -1;
	}
	else if (a == 'k')
	{
		if (b == 'i')
		{
			*c = 'j';
		}
		else if (b == 'j')
		{
			*nSign = sign * -1;
			*c = 'i';
		}
		else if (b == 'k')
		{
			*nSign = sign * -1;
			*c = '1';
		}
		else
			return -1;
	}
	else if (a =='1')
	{
		if (b == 'i')
		{
			*c = 'i';
		}
		else if (b == 'j')
		{
			*c = 'j';
		}
		else if (b == 'k')
		{
			*c = 'k';
		}
		else
			return -1;
	}
	else
		return -1;

	DBG("sign = %d, *pSign = %d\n", sign, *nSign);

	return 0;	/* OK */
}


int find(char f, uint64 *pOffset, int *pSign, char *pCurrent, uint64 maxLength)
{
	int ret;

	DBG("[DBG] f = %c, offset = %llu, sign = %d, current = %c, maxLength = %llu\n", f, *pOffset, *pSign, *pCurrent, maxLength);

	if (f != '1')
	{
		if (*pCurrent == f)
		{
			*pOffset += 1;
			*pCurrent = '1';
			return 1;	/* found */
		}

		while (((*pCurrent != f) || (*pSign != 1)) && (*pOffset < maxLength))
		{
			DBG("sign = %d, *pCurrent = %c, *pOffset = %llu\n", *pSign, *pCurrent, *pOffset);
			DBG("str[(*pOffset)] = %c\n", str[(*pOffset)]);
			ret = multiply(*pSign, *pCurrent, str[(*pOffset)], pSign, pCurrent);
			if (ret == -1) return 0;	/* failed */
			*pOffset += 1;
		}
	}
	else	/* find to end */
	{
		while (*pOffset < maxLength)
		{
			DBG("sign = %d, *pCurrent = %c, *pOffset = %llu\n", *pSign, *pCurrent, *pOffset);
			DBG("str[(*pOffset)] = %c\n", str[(*pOffset)]);
			ret = multiply(*pSign, *pCurrent, str[(*pOffset)], pSign, pCurrent);
			if (ret == -1) return 0;	/* failed */
			*pOffset += 1;
		}
	}

	if (*pCurrent == f)
	{
		*pCurrent = '1';
		DBG("Found: *pOffset = %llu, sign = %d\n", (*pOffset), *pSign);
		return 1;	/* found */
	}
	else if ((f == '1') && (*pCurrent == '1') && (*pOffset == maxLength))
	{
		DBG("Found: *pOffset = %llu, sign = %d\n", (*pOffset), *pSign);
		return 1;
	}		
	else
		return 0;	/* failed */

}


int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32 i, j;
        uint64 L, X;
		int32 sign;
		char cur;
		uint64 offset;
		char end;

        /* Test Case run once */
        scanf("%llu %llu\r\n", &L, &X);
		DBG("L = %u, X = %u\n", L, X);

        /* load data */
	    for (i=0; i<L; i++)
	    {
	    	scanf("%c", &str[i]);
			DBG("<%u:%c>\n", i, str[i]);
	    }
		scanf("\r\n");

		for (j=1; j<X; j++)
		{
		    for (i=(j*L); i<((j+1)*L); i++)
		    {
				str[i] = str[(i - (j*L))];
				DBG("<%u:%c>\n", i, str[i]);
		    }
		}

		offset = 0; /* begin */
		sign = 1;	/* 1 or -1 */
		cur = '1';
		if (find('i', &offset, &sign, &cur, (L*X)) &&
			find('j', &offset, &sign, &cur, (L*X)) &&
			find('k', &offset, &sign, &cur, (L*X)) &&
			find('1', &offset, &sign, &cur, (L*X)) &&
			(sign == 1))
		{
			DBG("offset = %llu, (L*X) = %llu\n", offset, (L*X));
			/* Print */
			printf("Case #%d: %s\n", Ti, "YES");
		}
		else
		{
			/* Print */
			printf("Case #%d: %s\n", Ti, "NO");
		}
    }

    return 0;
}
