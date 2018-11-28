#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <memory.h>


using namespace std;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int a;
		set<int> s;
		vector<int> v;
		scanf("%d", &a);
		a--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int b;
				scanf("%d", &b);
				if (a ==i)
					s.insert(b);
			}
		}

		scanf("%d", &a);
		a--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int b;
				scanf("%d", &b);
				if (a ==i && s.find(b) != s.end())
					v.push_back(b);
			}
		}
		printf("Case #%d: ", t+1);
		if (v.size() == 0)
			printf("Volunteer cheated!");
		else if (v.size() > 1)
			printf("Bad magician!");
		else
			printf("%d", v[0]);
		printf("\n");
	}

	return 0;
}