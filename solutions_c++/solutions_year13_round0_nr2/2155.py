#include <stdio.h>
#include <iostream>
#define MAX 105
int main()
{
	int T;
	FILE* f = fopen("B.out", "w");
	scanf("%d", &T);
	for( int z = 1; z<=T; z++)
	{
		int X,Y;
		scanf("%d %d", &Y, &X);
		int map[MAX][MAX];
		for(int i = 0; i<Y; i++)
			for(int o = 0; o<X; o++)
				scanf("%d", &map[i][o]);

		bool can = true;
		for(int i = 0; i<Y && can; i++)
		{
			for(int o = 0; o<X && can; o++)
			{
				bool hori = true;
				bool vert = true;

				for(int d = 0; d < X; d++)
				{
					if(map[i][o] < map[i][d])
						hori = false;
				}

				for(int d = 0; d < Y; d++)
				{
					if(map[i][o] < map[d][o])
						vert = false;
				}
				if( vert == false && hori == false)
					can = false;
			}
		}

		if(can == false)
			fprintf(f, "Case #%d: NO\n",z);
		else
			fprintf(f, "Case #%d: YES\n",z);
		
	}
	
	return 0;
}