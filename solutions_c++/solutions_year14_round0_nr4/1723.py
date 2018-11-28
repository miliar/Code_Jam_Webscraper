
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[10240];

typedef  long long  int64_t;

int N;
struct Weight
{
	long double w;
	int player;
};
Weight W[2000];

bool CompareWeight(Weight a, Weight b)
{
	return a.w < b.w;
}

int main()
{
	fgets(buf, 1024, stdin);
	int ncase = atoi(buf);
	//	printf("%d\n", ncase);

	for(int i=1; i<=ncase; i++)
	{
		scanf("%d", &N);
		//printf("N=%d\n", N);

		for(int j=0; j<N; j++)
		{
			scanf("%lf", &W[j].w);
			W[j].player = 1;  // Naomi
//			printf("%lf ", W[j].w);
		}
//		printf("\n");

		for(int j=0; j<N; j++)
		{
			scanf("%lf", &W[j+N].w);
			W[j+N].player = 2;  // Ken
//			printf("%lf ", W[j+N].w);
		}
//		printf("\n");

		std::sort(W, W + 2*N, CompareWeight);

// 		for(int j=0; j<N; j++)
// 		{
// 			printf("%lf ", W[j].w);
// 		}
// 		for(int j=0; j<N; j++)
// 		{
// 			printf("%lf ", W[j+N].w);
// 		}
// 		printf("\n");

		int ken_point = 0;
		int naomi_stk = 0;
		for(int j=0; j<2*N; j++)
		{
			if (W[j].player == 1)       // Naomi
				naomi_stk++;
			else if (W[j].player == 2)  // Ken
			{
				if (naomi_stk > 0)
				{
					naomi_stk--;
					ken_point++;
				}
			}
		}

		int naomi_point = 0;
		int ken_stk = 0;
		for(int j=0; j<2*N; j++)
		{
			if (W[j].player == 2)       // Ken
				ken_stk++;
			else if (W[j].player == 1)  // Naomi
			{
				if (ken_stk > 0)
				{
					ken_stk--;
					naomi_point++;
				}
			}
		}

		printf("Case #%d: %d %d", i, naomi_point, N-ken_point);
		printf("\n");
	}

	return  0;  
}
