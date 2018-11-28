#include <stdio.h>

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
	int T;

	int N;
	bool check[10];

	int num, tmp, cnt;

	scanf("%d", &T);
	for(int test_case=1;test_case<=T;test_case++)
	{
		scanf("%d", &N);
		for(int i=0;i<10;i++)
			check[i] = false;

		printf("Case #%d: ", test_case);
		if(N==0)
			printf("INSOMNIA\n");
		else
		{
			num = 0;
			cnt = 0;
			while(cnt<10)
			{
				num += N;
				tmp = num;
				while(tmp>0)
				{
					if(check[tmp%10] == false)
					{
						cnt++;
						check[tmp%10] = true;
					}
					tmp /= 10;
				}
			}
			printf("%d\n", num);
		}
	}

	return 0;
}