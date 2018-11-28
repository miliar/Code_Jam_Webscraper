#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

bool is_solved_sol3(char ingrid[][100], int r, int c)
{
	char grid[100][100];
	bool change_needed = true;

	for (int i=0; i<100; i++)
		for (int j=0; j<100; j++)
			grid[i][j] = ingrid[i][j];


	/* explode click */
	int x = r-1, y = c-1, mines=0;

	/* check neighbours for click neghbours (x-1)(y) */
	if (grid[x-1][y] == '.')
	{
		if (x>=2  && y>=1 && grid[x-2][y-1]=='*')
			mines++;
		if (x >=2 && y>=1 && grid[x-2][y-1]=='*')
			mines++;
		if (x >= 2  && grid[x-2][y]=='*')
			mines++;

		grid[x-1][y] = char ('0' + mines);
	}
	else
		return false;

	/* check neighbours for click neghbours (x)(y-1) */
	if (grid[x][y-1] == '.')
	{
		mines = 0;
		if (y >=2  && grid[x][y-2]=='*')
			mines++;
		if (y >=2 && x>=1 && grid[x-1][y-2]=='*')
			mines++;
		if (x >= 1 && y >=1  && grid[x-1][y-1]=='*')
			mines++;

		grid[x][y-1] = char ('0' + mines);
	}
	else
		return false;

		/* check neighbours for click neghbours (x-1)(y-1) */
	if (grid[x-1][y-1] == '.')
	{
		mines = 0;
		if (y >=2  && grid[x][y-2]=='*')
			mines++;
		if (y >=2 && x>=1 && grid[x-1][y-2]=='*')
			mines++;
		if (x >= 2 && y >=1  && grid[x-2][y-1]=='*')
			mines++;
		if (x >= 2   && grid[x-2][y]=='*')
			mines++;
		if (y >=2 && x>=2 && grid[x-2][y-2]=='*')
			mines++;

		grid[x-1][y-1] = char ('0' + mines);
	}
	else
		return false;

	while (change_needed)
	{

		change_needed = false;

		for (int i=0; i<r; i++)
			for (int j=0; j<c; j++)
			{
				if (grid[i][j] == '.')
				{
					/* check if there is a neighbouring zero */
					if (r>=i+2 && grid[i+1][j]=='0' 
						||
						c>=j+2 && grid[i][j+1]=='0' 
						||
						r>=i+2 && c>=j+2 && grid[i+1][j+1]=='0' 
						||
						r>=i && i >=1 && grid[i-1][j]=='0' 
						||
						c>=j && j>=1 && grid[i][j-1]=='0' 
						||
						r>=i && c>=j && i>=1 && j>=1 && grid[i-1][j-1]=='0' 
						||
						r>=i && i >=1 && c>=2 && grid[i-1][j+1]=='0' 
						||
						r>=2 && c>=j && j>=1  && grid[i+1][j-1]=='0'
						)
					{
						mines = 0;
						if (r>=i+2 && grid[i+1][j]=='*' )
							mines++;
						if (c>=j+2 && grid[i][j+1]=='*' )
							mines++;
						if (r>=i+2 && c>=j+2 && grid[i+1][j+1]=='*' )
							mines++;
						if (r>=i && i >=1 && grid[i-1][j]=='*') 
							mines++;
						if (c>=j && j>=1 && grid[i][j-1]=='*' )
							mines++;
						if (r>=i && c>=j && i>=1 && j>=1 && grid[i-1][j-1]=='*' )
							mines++;
						if (r>=i && i >=1 && c>=2 && grid[i-1][j+1]=='*' )
							mines++;
						if (r>=2 && c>=j && j>=1  && grid[i+1][j-1]=='*')
							mines++;

						grid[i][j] = char ('0' + mines);;
						change_needed = true;
					}



				}
			}
	}

	//printf ("Solution is\n");

	//for (int i=0; i<r; i++)
	//{
	//	for (int j=0; j<c; j++)
	//	{
	//		printf("%c" , grid[i][j]);
	//	}
	//	printf ("\n");
	//}

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
		{
			if (grid[i][j] == '.')
			{
				//printf("NOT SOLVED\n");
				return false;
			}
		}

		//printf("YEAH: SOLVED\n");
			//printf ("Solution is\n");

	//for (int i=0; i<r; i++)
	//{
	//	for (int j=0; j<c; j++)
	//	{
	//		printf("%c" , grid[i][j]);
	//	}
	//	printf ("\n");
	//}
	//printf ("\n");
		return true;

}

bool is_solved(char ingrid[][100], int r, int c)
{
	char grid[100][100];
	bool change_needed = true;

	for (int i=0; i<100; i++)
		for (int j=0; j<100; j++)
			grid[i][j] = ingrid[i][j];


	/* explode click */
	int x = 0, y = 0, mines=0;

	/* check neighbours for click neghbours (x+1)(y) */
	if (grid[x+1][y] == '.')
	{
		if (r >2  && grid[x+2][y]=='*')
			mines++;
		if (r >2 && c>1 && grid[x+2][y+1]=='*')
			mines++;
		if (r > 1 && c >1  && grid[x+1][y+1]=='*')
			mines++;

		grid[x+1][y] = char ('0' + mines);
	}
	else
		return false;

	/* check neighbours for click neghbours (x)(y+1) */
	if (grid[x][y+1] == '.')
	{
		mines = 0;
		if (c >2  && grid[x][y+2]=='*')
			mines++;
		if (r >1 && c>2 && grid[x+1][y+2]=='*')
			mines++;
		if (r > 1 && c >1  && grid[x+1][y+1]=='*')
			mines++;

		grid[x][y+1] = char ('0' + mines);
	}
	else
		return false;

	
	/* check neighbours for click neghbours (x+1)(y+1) */
	if (grid[x+1][y+1] == '.')
	{
		mines = 0;
		if (r>1 && c >2  && grid[x+1][y+2]=='*')
			mines++;
		if (r >2 && c>2 && grid[x+2][y+2]=='*')
			mines++;
		if (r >2  && grid[x+2][y]=='*')
			mines++;
		if ( c>2 && grid[x][y+2]=='*')
			mines++;
		if (r >2 && c>1 && grid[x+2][y+1]=='*')
			mines++;

		grid[x+1][y+1] = char ('0' + mines);
	}
	else
		return false;

	while (change_needed)
	{

		change_needed = false;

		for (int i=0; i<r; i++)
			for (int j=0; j<c; j++)
			{
				if (grid[i][j] == '.')
				{
					/* check if there is a neighbouring zero */
					if (r>=i+2 && grid[i+1][j]=='0' 
						||
						c>=j+2 && grid[i][j+1]=='0' 
						||
						r>=i+2 && c>=j+2 && grid[i+1][j+1]=='0' 
						||
						r>=i && i >=1 && grid[i-1][j]=='0' 
						||
						c>=j && j>=1 && grid[i][j-1]=='0' 
						||
						r>=i && c>=j && i>=1 && j>=1 && grid[i-1][j-1]=='0' 
						||
						r>=i && i >=1 && c>=2 && grid[i-1][j+1]=='0' 
						||
						r>=2 && c>=j && j>=1  && grid[i+1][j-1]=='0'
						)
					{
						mines = 0;
						if (r>=i+2 && grid[i+1][j]=='*' )
							mines++;
						if (c>=j+2 && grid[i][j+1]=='*' )
							mines++;
						if (r>=i+2 && c>=j+2 && grid[i+1][j+1]=='*' )
							mines++;
						if (r>=i && i >=1 && grid[i-1][j]=='*') 
							mines++;
						if (c>=j && j>=1 && grid[i][j-1]=='*' )
							mines++;
						if (r>=i && c>=j && i>=1 && j>=1 && grid[i-1][j-1]=='*' )
							mines++;
						if (r>=i && i >=1 && c>=2 && grid[i-1][j+1]=='*' )
							mines++;
						if (r>=2 && c>=j && j>=1  && grid[i+1][j-1]=='*')
							mines++;

						grid[i][j] = char ('0' + mines);;
						change_needed = true;
					}



				}
			}
	}

	//printf ("Solution is\n");

	//for (int i=0; i<r; i++)
	//{
	//	for (int j=0; j<c; j++)
	//	{
	//		printf("%c" , grid[i][j]);
	//	}
	//	printf ("\n");
	//}

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
		{
			if (grid[i][j] == '.')
			{
				//printf("NOT SOLVED\n");
				return false;
			}
		}

		//printf("YEAH: SOLVED\n");
		//	printf ("Solution is\n");

	//for (int i=0; i<r; i++)
	//{
	//	for (int j=0; j<c; j++)
	//	{
	//		printf("%c" , grid[i][j]);
	//	}
	//	printf ("\n");
	//}
	//printf ("\n");
		return true;

}


bool sol6(char grid[][100], int r, int c, int m)
{

	for (int i=0; i<100; i++)
	for (int j=0; j<100; j++)
		grid[i][j]='?';

	grid[0][0] = 'c';

	int free = r*c - m - 1;

	/* fill diagonal first */
		for (int j =1; j<c-1 && free > 0; j++)
		{
				grid[0][j]='.';
				free --;
		}

		for (int i =1; i<r && free > 0; i++)
			for (int j =0; j<c-1 && free > 0; j++)
			{
					grid[i][j]='.';
					free --;
			}

	if (free>0) return false;


	/* put the rest as mines */

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
		{
			if ( 
				grid[i][j] == '?'
				)
			{
				grid[i][j] = '*';
				free--;
			}

		}

		//printf("Solution 2\n");
		return is_solved(grid, r, c);
}





bool sol5(char grid[][100], int r, int c, int m)
{

	for (int i=0; i<100; i++)
	for (int j=0; j<100; j++)
		grid[i][j]='?';

	grid[0][0] = 'c';

	/* fill line by line first */

	for (int j=c-1; j>=0 && m > 0; j--)
	{
		for (int i =r-1; i>=0 && m > 0; i--)
		{
			
			
				grid[i][j]='*';
				m --;
			
		}
	}

	/* put the rest as hidden */

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
		{
			if ( 
				grid[i][j] == '?'
				)
			{
				grid[i][j] = '.';
			}

		}

		//printf("Solution 3\n");
		return is_solved(grid, r, c);
}



bool sol4(char grid[][100], int r, int c, int m)
{

	for (int i=0; i<100; i++)
	for (int j=0; j<100; j++)
		grid[i][j]='?';

	grid[0][0] = 'c';

	/* fill line by line first */

		for (int i =r-1; i>=0 && m > 0; i--)
		{
			for (int j=0; j<c && m > 0; j++)
			{
				grid[i][j]='*';
				m --;
			}
		}

	/* put the rest as hidden */

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
		{
			if ( 
				grid[i][j] == '?'
				)
			{
				grid[i][j] = '.';
			}

		}

		//printf("Solution 3\n");
		return is_solved(grid, r, c);
}



bool sol3(char grid[][100], int r, int c, int m)
{

	for (int i=0; i<100; i++)
	for (int j=0; j<100; j++)
		grid[i][j]='?';

	grid[r-1][c-1] = 'c';

	if (m>0)
	{
		grid[0][0] = '*';
		m--;
	}

	/* fill diagonal first */

		for (int i =1; i<min(c, r) && m > 0; i++)
		{
			for (int j=0; j<=i && m > 0; j++)
			{
				grid[i-j][j]='*';
				m --;
			}
		}

	/* continue filling */
	if (m > 0)
	{
		if (r >= c)
		{
			for (int i=0; i<r && m > 0; i++)
				for (int j=0; j<c && m > 0; j++)
				{
					if ( 
						grid[i][j] == '?'
						)
					{
						grid[i][j] = '*';
						m--;
					}

				}
		}
		else
		{
			for (int j=0; j<c && m > 0; j++)
				for (int i=0; i<r && m > 0; i++)
				{
					if ( 
						grid[i][j] == '?'
						)
					{
						grid[i][j] = '*';
						m--;
					}

				}
		}
	}

	/* put the rest as hidden */

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
		{
			if ( 
				grid[i][j] == '?'
				)
			{
				grid[i][j] = '.';
			}

		}

		//printf("Solution 3\n");
		return is_solved_sol3(grid, r, c);
}



bool sol2(char grid[][100], int r, int c, int m)
{

	for (int i=0; i<100; i++)
	for (int j=0; j<100; j++)
		grid[i][j]='?';

	grid[0][0] = 'c';

	int free = r*c - m - 1;

	/* fill diagonal first */
		for (int i =1; i<min(c, r) && free > 0; i++)
		{
			for (int j=0; j<=i && free > 0; j++)
			{
				grid[i][j]='.';
				free --;
			}

			for (int j=0; j<i && free > 0; j++)
			{
				grid[j][i]='.';
				free --;
			}


		}

	/* continue filling */
	if (free > 0)
	{
		if (r >= c)
		{
			for (int i=0; i<r && free > 0; i++)
				for (int j=0; j<c && free > 0; j++)
				{
					if ( 
						grid[i][j] == '?'
						)
					{
						grid[i][j] = '.';
						free--;
					}

				}
		}
		else
		{
			for (int j=0; j<c && free > 0; j++)
				for (int i=0; i<r && free > 0; i++)
				{
					if ( 
						grid[i][j] == '?'
						)
					{
						grid[i][j] = '.';
						free--;
					}

				}
		}
	}

	/* put the rest as mines */

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
		{
			if ( 
				grid[i][j] == '?'
				)
			{
				grid[i][j] = '*';
				free--;
			}

		}

		//printf("Solution 2\n");
		return is_solved(grid, r, c);
}



bool sol1(char grid[][100], int r, int c, int m)
{

	for (int i=0; i<100; i++)
	for (int j=0; j<100; j++)
		grid[i][j]='?';

	grid[0][0] = 'c';

	int free = r*c - m - 1;

	/* fill diagonal first */

		for (int i =1; i<min(c, r) && free > 0; i++)
		{
			for (int j=0; j<=i && free > 0; j++)
			{
				grid[i-j][j]='.';
				free --;
			}
		}

	/* continue filling */
	if (free > 0)
	{
		if (r >= c)
		{
			for (int i=0; i<r && free > 0; i++)
				for (int j=0; j<c && free > 0; j++)
				{
					if ( 
						grid[i][j] == '?'
						)
					{
						grid[i][j] = '.';
						free--;
					}

				}
		}
		else
		{
			for (int j=0; j<c && free > 0; j++)
				for (int i=0; i<r && free > 0; i++)
				{
					if ( 
						grid[i][j] == '?'
						)
					{
						grid[i][j] = '.';
						free--;
					}

				}
		}
	}

	/* put the rest as mines */

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
		{
			if ( 
				grid[i][j] == '?'
				)
			{
				grid[i][j] = '*';
				free--;
			}

		}

		//printf("Solution 1\n");
		return is_solved(grid, r, c);
}


int main() {
	int t, case_num=0;
	int r, c, m;
	bool impossible;
	scanf("%d", &t);
	while (t--) {
		char grid[100][100];
		case_num++;
		scanf("%d %d %d", &r, &c, &m);
		printf("Case #%d:\n", case_num);
		//printf("%d %d %d\n", r, c, m);

		impossible = false;
		/* Possible means at least 4 free (or exactly one) if (R&C>1), 
		or at least one free if (R or C == 1) */
		if ( 
			(r*c-m<4 && r*c-m!=1 && r>1 && c>1) 
			||
			( (r==1 || c==1) && r*c-m<1 )
			)
			printf("Impossible\n");
		else if (r*c-m==1 && r>1 && c>1)
		{

			for (int i=0; i<100; i++)
				for (int j=0; j<100; j++)
					grid[i][j]='?';

			grid[0][0] = 'c';
			for (int i=0; i<r; i++)
				for (int j=0; j<c; j++)
				{
					if ( 
						grid[i][j] == '?'
						)
					{
						grid[i][j] = '*';
					}

				}

				for (int i=0; i<r; i++)
				{
					for (int j=0; j<c; j++)
					{
						printf("%c" , grid[i][j]);
					}
					printf ("\n");
				}
		}
		else
		{

			for (int i=0; i<100; i++)
				for (int j=0; j<100; j++)
					grid[i][j]='?';


			if (r==1)
			{
				int i,j;
				grid[0][0]='c';
				for (i=c-1; m>0; i--)
				{
					grid[0][i] = '*';
					m--;
				}
				for (j=i; j>0; j--)
					grid[0][j] = '.';
			}
			else if (c==1)
			{
				int i,j;
				grid[0][0]='c';
				for (i=r-1; m>0; i--)
				{
					grid[i][0] = '*';
					m--;
				}
				for (j=i; j>0; j--)
					grid[j][0] = '.';
			}
			else
			{
				if (!sol1(grid, r, c, m))
				{
					if(!sol2(grid, r, c, m))
						if(!sol3(grid, r, c, m))
							if(!sol4(grid, r, c, m))
								if(!sol5(grid, r, c, m))
									if(!sol6(grid, r, c, m))
									impossible = true;
				}
				
				if (!impossible)
				{
					/*check */
					int count = 0;
					for (int i=0; i<r; i++)
						for (int j=0; j<c; j++)
							if (grid[i][j]=='*')
								count++;

					if (count!=m)
						printf("HHHHHHHHHHHHHHHHHHHHHHHHHHHH errror\n");
				}
			}









			if (!impossible)
			{
			for (int i=0; i<r; i++)
			{
				for (int j=0; j<c; j++)
				{
					printf("%c" , grid[i][j]);
				}
				printf ("\n");
			}
			}
			else
			{
				printf("Impossible\n");
			}

			//is_solved(grid, r, c);
		}
	}
	return 0;
}
