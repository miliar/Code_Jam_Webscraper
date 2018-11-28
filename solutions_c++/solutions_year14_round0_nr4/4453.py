#include <stdio.h>
#include <algorithm>
int main()
{
	int T;
	scanf("%d", &T);
	for(int caseNum = 1; caseNum <= T; caseNum++)
	{
		int N;
		double naomi[1000], ken[1000];
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
			scanf("%lf", naomi + i);
		for(int i = 0; i < N; i++)
			scanf("%lf", ken + i);
		std::sort(naomi, naomi + N);
		std::sort(ken, ken + N);
		printf("Case #%d: ", caseNum);
		int ans = 0;
		for(int i = 0, now = 0; i < N; i++)
			if(naomi[i] > ken[now])
				ans++, now++;
		printf("%d ", ans);
		for(int i = 0, now = -1;; i++)
		{
			if(i == N)
			{
				puts("0");
				break;
			}
			while(++now < N && naomi[i] > ken[now]);
			if(now == N)
			{
				printf("%d\n", N - i);
				break;
			}
		}
	}
}