#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);

	for (int i = 1; i <= T; ++i)
	{
		int a;
		scanf("%d",&a);

		int cards[4][4];

		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d",&cards[i][j]);

		int b;
		scanf("%d",&b);

		int cards2[4][4];

		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d",&cards2[i][j]);

		int answer = -1;
		bool bm = false;

		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if(cards[a-1][i] == cards2[b-1][j])
				{
					if(answer != -1)
						bm = true;
					else
						answer = cards2[b-1][j];
				}

		if (bm)
			printf("Case #%d: Bad magician!\n", i);
		else if(answer == -1)
			printf("Case #%d: Volunteer cheated!\n", i);
		else
			printf("Case #%d: %d\n",i,answer);
	}
}