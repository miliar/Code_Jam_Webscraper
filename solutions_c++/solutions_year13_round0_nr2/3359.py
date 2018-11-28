//on way to exit it must all be equal or lower

#include <stdio.h>

int main()
{
    int T, C;
    int game[100][100], blank;
	int M, N;
	int result; //0 is ok, 1 is not ok
	int tl, tr, tu, td; //temp left right up and down
	int sx, sy;

    scanf("%i\n", &T);

    for (C = 1;C <= T;C++)
    {
		result = 0;//clear result
		scanf("%i %i", &N, &M);
			
        for (int y = 0;y < N;y++)//read shit
        {
			for (int x = 0;x < M;x++)
			{
                scanf("%d", &game[y][x]);
			}
        }
		
		//ok, check to see if in either one of the rows, there is an exit path where all the grass is the same or lower level
		for (sy = 0;sy < N;sy++)
		{
			for (sx = 0;sx < M;sx++)
			{
				tl = 0;
				tr = 0;
				tu = 0;
				td = 0;
				//sx sy is the seed value
				//check left 
				for (int x = 0;x < sx;x++)
				{
					if (game[sy][x] > game[sy][sx]) //this means that one of the block in the line is bigger
						tl++;
				}
				//check left 
				for (int x = sx;x < M;x++)
				{
					if (game[sy][x] > game[sy][sx]) //this means that one of the block in the line is bigger
						tr++;
				}
				//check up
				for (int y = 0;y < sy;y++)
				{
					if (game[y][sx] > game[sy][sx]) //this means that one of the block in the line is bigger
						tu++;
				}
				//check down
				for (int y = sy;y < N;y++)
				{
					if (game[y][sx] > game[sy][sx]) //this means that one of the block in the line is bigger
						td++;
				}
				
				if (((tu + td) != 0) && ((tl + tr) != 0)) //this means that there is path where it is valid
					result = 1;
			}
		}
		
       printf("Case #%i: ", C);
	   if (result == 0) printf("YES\n");
		else printf("NO\n");

    }

    return 0;
}
