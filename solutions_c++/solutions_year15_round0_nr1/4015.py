#include <cstdio>
#include <cstdlib>

using namespace std;

int solve(void)
{
	int count;
	scanf("%d ", &count);
	//printf("%d\n", count);
	int total = 0;
	int neededToAdd = 0;
	char tmp;
	for (int i = 0; i <= count;++i)
	{
		scanf("%c",&tmp );
		tmp -= '0';
		if (total < i && tmp)
		{
			neededToAdd += i - total;
			total = i + tmp; 
		}else if (tmp)
		{
			total += tmp;
		}
	}

	return neededToAdd;
}

int main(void)
{
	int count;
	scanf("%d ", &count);

	for (int i = 0; i < count;++i)
	{
		printf("Case #%d: %d\n",i+1,solve());
	}
}