#include<cstdio>
#include<algorithm>

int S[10010];

int main()
{
	int T; scanf("%d", &T);
	for(int ii = 0; ii < T; ii++)
	{
		int N, X; scanf("%d%d", &N, &X);
		for(int i = 0; i < N; i++)
			scanf("%d", S+i);
		std::sort(S,S+N);
		int end = N-1;
		int beg = 0;
		int total = 0;
		while(beg <= end)
		{
			total++;
			if(S[end]+S[beg] <= X)
			{
				end--; beg++;
			}
			else
				end--;
		}
		printf("Case #%d: %d\n",ii+1,total);
	}

	return 0;
}
