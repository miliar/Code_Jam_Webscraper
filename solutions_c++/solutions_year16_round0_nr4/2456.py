#include <cstdio>
#include <cstdlib>
#include <vector>

int main()
{
	int Test;
	int K, C, S;
	scanf("%d", &Test);
	std::vector<int> result(Test, 0);
	std::vector<int> len(Test, 0);
	for(int t=0; t<Test; ++t)
	{
		scanf("%d %d %d", &K, &C, &S);
		len[t] = K;
		if(C==1)
		{
			if (S < K)
			{
				result[t] = -1;
			}
			else 
			{
				result[t] = K;
			}
		}
		else {
			if(S < K-1)
			{
				result[t] = -1;
			}
			else 
			{
				result[t] = K-1;
			}
		}
	}
	for(int t=0; t<Test; ++t)
	{
		if(result[t] == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n", t+1);
		}
		else 
		{
			printf("Case #%d:", t+1);
			if(result[t] == len[t] || result[t] == 0)
			{
				printf(" 1");
				result[t] = result[t] - 1;
			}
			for(int i=0; i<result[t]; ++i)
			{
				printf(" %d", i+2);
			}
			printf("\n");
		}
	}
	return 0;
};