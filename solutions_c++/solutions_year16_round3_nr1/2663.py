#include<stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

#define MAX (26+1)

struct cand
{
	char c;
	int count;
};
struct cand s[MAX];


int comp_cand (const void *a, const void*b, void* arg)
{
	return -(((struct cand*)a)->count - ((struct cand*)b)->count);
}

char rem[1000+1000] = {'\0'};


int main()
{
	int k;
	int T;
	scanf("%d", &T);
	for (k = 0; k < T; k++)
	{
		int N;
		scanf("%d", &N);
		memset(s, 0, N*sizeof(struct cand));
		int count = 0;
		for (int i = 0; i < N; i++)
		{
			s[i].c = 'A'+i;
			scanf("%d",&s[i].count);
			count+= s[i].count; 
		}
		
#if 0
		for (int i = 0; i < N; i++)
		{
			prob[i] = s[i]/count;
		}
#endif
		//q_sort(prob, N, sizeof(double), comp_double, NULL);
		

		//printf("count = %d\n", count);
		/* Removing 2 candidates from max */
		int iter = 0;
		int orig_n = N;
		memset(rem, 0, sizeof(rem));
		while (count > 0)
		{
			qsort_r(s, orig_n, sizeof(struct cand), comp_cand, NULL);
			struct cand *cur = &s[0];
			struct cand *next = &s[1];
			if (cur->count >=2)
			{
				if (next->count >=1)
				{
					if ((count - 2) != 0 && (float)next->count/(count-2) < 0.50000)
					{
						cur->count -=2;
						rem[iter++] = cur->c;
						rem[iter++] = cur->c;
						rem[iter++] = ' ';
						count -= 2;
					}
					else if ((count -1) != 0 && (float) next->count/(count-1) < 0.50000)
					{
						cur->count -=1;
						rem[iter++] = cur->c;
						rem[iter++] = ' ';
						count -= 1;

					}
					else //if ((count -2) != 0 /*&& (float) cur->count/(count-2) < 0.50000 */&& (float) next->count/(count-2) < 0.50000)
					{
						cur->count -=1;
						next->count -=1;
						rem[iter++] = cur->c;
						rem[iter++] = next->c;
						rem[iter++] = ' ';
						count -= 2;
					}

					if (next->count == 0)
					{
						N = N-1;
					}
				}	
				if (cur->count == 0)
				{
					N = N -1;
				}
			}

			else if (cur->count <= 1)
			{
				if (next->count <= 1)
				{
					if ((count-1) != 0 && next->count/(count-1) < 0.50000)
					{
						cur->count -=1;
						rem[iter++] = cur->c;
						rem[iter++] = ' ';
						count -= 1;
					}
					else /*if ((count -2) != 0 && cur->count/(count-2) < 0.50000 && next->count/(count-2) < 0.50000) */
					{
						cur->count -=1;
						next->count -=1;
						rem[iter++] = cur->c;
						rem[iter++] = next->c;
						rem[iter++] = ' ';
						count -= 2;
					}
					if (next->count == 0)
					{
						N = N-1;
					}
				}
	
				if (cur->count == 0)
				{
					N = N -1;
				}
			}
		}
		printf("Case #%d: %s\n", (k+1), rem);
	}
	return 0;
}
