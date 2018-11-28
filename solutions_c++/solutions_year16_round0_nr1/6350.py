#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

bool flag[10];
int sum;

void check(int x)
{
	while(x && sum < 10)
	{
		if(!flag[x % 10])
		{
			++sum;
			flag[x % 10] = 1;	
		}
		x /= 10;
	}
}


int main()
{
	int T, N;
	//freopen("A-small-attempt1.in", "r", stdin);
	//freopen("A-small-attempt1.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	while(~scanf("%d", &T))
	{
		for(int i = 0;i < T; ++i)
		{
			scanf("%d", &N);
			if(!N)
				printf("Case #%d: INSOMNIA\n", i + 1);
			else
			{
				memset(flag, 0, sizeof(flag));
				sum = 0;
				int j = 1;
				while(1)
				{
					check(N * j);
					if(sum == 10)
						break;
					++j;
				}
				printf("Case #%d: %d\n", i + 1, N * j);
			}
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
