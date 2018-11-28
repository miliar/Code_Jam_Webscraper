#include <cstdio>

char str[1010];

int main()
{
	int t;
	scanf("%d", &t);
	for (int c=1; c<=t; ++c)
	{
		int m;
		scanf("%d %s", &m, str);

		int standing = 0;
		int additional = 0;
		for (int shyness=0; shyness<=m; ++shyness)
		{
			int peopleCount = str[shyness] - '0';
			if (peopleCount == 0)
				continue;

			if (standing < shyness)
			{
				int needPeopleCount = shyness - standing;
				additional += needPeopleCount;
				standing += peopleCount + needPeopleCount;
			}
			else
			{
				standing += peopleCount;
			}
		}
		
		printf("Case #%d: %d\n", c, additional);
	}
	
	return 0;
}