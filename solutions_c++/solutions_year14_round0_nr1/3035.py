#include <stdio.h>
#include <set>

using std::set;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T;
	
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		int r1, r2, count = 0, res = 1;
		set<int> S;
		
		scanf("%d", &r1);
		
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
			{
				int v;
				
				scanf("%d", &v);
				if(i == r1)
					S.insert(v);
			}
		
		scanf("%d", &r2);
		
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
			{
				int v;
				
				scanf("%d", &v);
				if(i == r2 && S.count(v))
				{
					count++;
					res = v;
				}
			}
		
		printf("Case #%d: ", t);
		if(count == 1)
			printf("%d\n", res);
		if(count == 0)
			printf("Volunteer cheated!\n");
		if(count > 1)
			printf("Bad magician!\n");
	}
	return 0;
}

