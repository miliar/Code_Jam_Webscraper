#include <cstdio>
#include <stdlib.h>

int compare(const void* first, const void* second)
{
	if(*((double*)first) > *((double*)second))
		return 1;
	if(*((double*)first) == *((double*)second))
		return 0;
	if(*((double*)first) < *((double*)second))
		return -1;
}

int main ()
{
	freopen("dd.in", "r",stdin);
	freopen("dd.out", "w", stdout);

	int test_case = 0;
	int case_no = 1;

	scanf("%d", &test_case);
	while(test_case--)
	{
		//double *n = NULL;
		//double *k = NULL;
		double n[1001] = {0};
		double k[1001] = {0};
		int box = 0;
		int scored = 0;
		int score = 0;
		int index_n = 0;
		int index_k = 0;

		scanf("%d", &box);
		//n = new double[256];
		//k = new double[box];

		for(int i = 0; i < box; ++i)
		{
			scanf("%lf", &n[i]);
		}

		for(int i = 0; i < box; ++i)
		{
			scanf("%lf", &k[i]);
		}

		qsort(n, box, sizeof(double),compare);
		qsort(k, box, sizeof(double),compare);

		index_n = box-1;
		index_k = box-1;
		while(1)
		{
			if(n[index_n] > k[index_k])
			{
				scored++;
				index_k--;
				index_n--;
			}
			else
			{
				index_k--;
			}
			if(index_k < 0 || index_n < 0)
			{
				break;
			}
		}

		index_n = box-1;
		index_k = box-1;
		while(1)
		{
			if(n[index_n] < k[index_k])
			{
				score++;
				index_k--;
				index_n--;
			}
			else
			{
				index_n--;
			}
			if(index_k < 0 || index_n < 0)
			{
				break;
			}
		}
		printf("Case #%d: %d %d\n", case_no++, scored, box - score);
		//delete n;
		//delete k;
	}

	return 0;
}