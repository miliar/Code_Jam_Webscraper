#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	  // Process queries.
	int T;
	
	scanf("%d", &T);
	int tmp;
	int lawn[100][100];
	int lawnr[100];
	int lawnc[100];
	for (int prob = 1; prob <= T; prob++)
	{
		int row, col;
		scanf("%d %d", &row, &col);

		for (int rr = 0; rr < row; ++rr)
		{
			lawnr[rr] = 0;
		}

		for (int rr = 0; rr < col; ++rr)
		{
			lawnc[rr] = 0;
		}

		for (int rr = 0; rr < row; ++rr)
		{
			for (int cc = 0; cc < col; ++cc)
			{
				scanf("%d", &tmp);
				lawn[rr][cc] = tmp;
				if (tmp == 1)
				{
					lawnr[rr]++;
					lawnc[cc]++;
				}
			}
		}

		bool no = false;
		for (int rr = 0; rr < row; ++rr)
		{
			for (int cc = 0; cc < col; ++cc)
			{
				if (lawn[rr][cc] == 1)
				{
					if (lawnr[rr] != col && lawnc[cc] != row) 
					{
						no = true;
						break;
					}
				}
			}
			if (no)
			{
				break;
			}
		}

		
		if (no)
		{
			printf("Case #%d: %s\n", prob, "NO");
		}
		else
		{
			printf("Case #%d: %s\n", prob, "YES");
		}
	}



	return 0;
}