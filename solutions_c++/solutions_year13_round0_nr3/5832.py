#include <iostream>
#include <stdio.h>
#include <math.h>

static char buf[1000];

static inline int check_palindrom(unsigned long long n)
{
	snprintf(buf, 1000, "%llu", n);
	char *str = buf;
	while(*str) str++;
	str--;
	char *p = buf;
	while(p <= str && *p == *str)
	{
		p++;
		str--;
	}	
	if(p > str)
		return 1;
	else
		return 0;	
}

using namespace std;

int main()
{
	FILE *fp = fopen("C-small-attempt0.in", "r");
	if(!fp)
		return printf("Can't open file\n");
	int t;
	int c = 0;
	unsigned long long min, max;

 	if(fscanf(fp, "%d", &t) != 1)
		return printf("Can't read number of test cases\n");
	for(int i = 1; i <= t; i++)
	{
		c = 0;
		cout<<"Case #"<<i<<": ";
		fscanf(fp, "%llu %llu", &min, &max);
		//printf("min : %llu , max : %llu\n", min, max);
		while(min <= max)
		{
			if( check_palindrom(min) )
			{
				double temp = sqrt((double)min);
				if( (temp - (int)temp == 0) && check_palindrom((unsigned long long)temp))
					c++;
			}
			min++;
		}
		cout<<c<<"\n";	
	}	
	
	return 0;
}
