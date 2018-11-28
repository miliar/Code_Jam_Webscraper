#include <cstdio>
#include <cstdlib>
#include <exception>
#include <iostream>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

using namespace std;

bool is_square(uint64_t x);
bool is_fair(uint64_t x);

void parse_input(void);

void parse_input(void)
{
	int T;
	uint64_t min, max;
	scanf("%d\n", &T);
	for(int i=0; i<T; i++)
	{
		scanf("%lld %lld\n", &min, &max);
		uint64_t min_base=sqrtl(min);
		uint64_t max_base=sqrtl(max);
		int numbers=0;
		for(int j=min_base; j<=max_base; j++)
		{
			if( is_fair(j))
			{
				uint64_t square=j*j;
				if( (square>=min) && (square <= max) && is_fair(square) )
				{
					numbers++;
				}
			}
		}
		printf("Case #%d: %d\n", i+1, numbers);
	}
}

bool is_fair(uint64_t x)
{
	char buf[25];
	sprintf(buf, "%llu", x);

	//printf("%s\n", buf);
	char *start=buf;
	char *end=buf+strlen(buf)-1;

	while(*start++ == *end--)
	{
		if(start >= end)
			return true;
	}
	return false;
}
		
bool is_square(uint64_t x)
{
	uint64_t sq=sqrtl(x);
	printf("%llu\n", sq);
}

int main(void)
{
	uint64_t x=0;
	parse_input();
	return 0;
}

