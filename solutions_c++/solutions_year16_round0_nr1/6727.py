#include <cstdio>
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for(int i = 1; i <= T; ++i)
	{
		int  N;
		scanf("%d", &N);

		if(N)
		{
			bool visited[10];
			for(int j = 0; j < 10; ++j)
				visited[j] = false;

			int num = N;
			while(true)
			{
				int temp = num;
				while(temp)
				{
					int digit = temp%10;
					visited[digit] = true;
					temp = temp/10;
				}
		
				bool flag = true;
				for(int j = 0; j < 10; ++j)
					if(!visited[j])
					{
						flag = false;
						break;
					}

				if(flag)
					break;

				num += N;
			}

			printf("Case #%d: %d\n", i, num);
		}
		else
			printf("Case #%d: INSOMNIA\n", i);
	}
	
	return 0;
}
