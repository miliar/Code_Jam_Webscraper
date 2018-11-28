
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

typedef  long long  int64_t;

long double C, F, X;

int main()
{
	fgets(buf, 1024, stdin);
	int ncase = atoi(buf);
	//	printf("%d\n", ncase);

	for(int i=1; i<=ncase; i++)
	{
		fgets(buf, 1024, stdin);
		sscanf(buf, "%lf %lf %lf", &C, &F, &X);

		//printf("%f %f %f\n", C, F, X);

		int k = ceill((X-C)/C - 2.0/F);
		if (k < 0)
			k = 0;
		//printf("k=%d\n", k);
		long double ans = 0.0;

		for (int j=0; j<k; j++)
		{
			ans += C / (2 + j*F);
		}
		ans += X / (2 + k*F);
		
		printf("Case #%d: %.7lf", i, ans);
 		printf("\n");
 	}

	return  0;  
}
