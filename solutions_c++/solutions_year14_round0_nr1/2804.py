#include <cstdio>
#include <vector>
#include <algorithm>

std::vector<int> cnt(17, 0);

void read(int row)
{
	for (int i=1; i<=4; ++i)
	{
		for (int j=0; j<4; ++j)
		{
			int dummy;
			scanf("%d", &dummy);
			if (i == row)
			{
				++cnt[dummy];
			}
		}
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; ++c)
	{
		std::fill(cnt.begin(), cnt.end(), 0);

		for (int i=0; i<2; ++i)
		{
			int row;
			scanf("%d", &row);
			read(row);
		}

		int num = std::count(cnt.begin(), cnt.end(), 2);
		printf("Case #%d: ", c);
		if (num == 0)
		{
			printf("Volunteer cheated!\n");
		}
		else if (num > 1)
		{
			printf("Bad magician!\n");
		}
		else
		{
			int num = std::find(cnt.begin(), cnt.end(), 2) - cnt.begin();
			printf("%d\n", num);
		}
	}
	
	return 0;
}
