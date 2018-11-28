#include <cstdio>

const int MAX_SIZE=100;

short map[MAX_SIZE][MAX_SIZE];
int nbRows, nbCols;

bool checkSquare(const int& row, const int& col)
{
	bool ok1=true, ok2=true;
	// checking col
	for(int cRow=0; cRow < nbRows; cRow++)
	{
		if(map[cRow][col] > map[row][col])
		{
			ok1=false;
			break;
		}
	}
	if(ok1)
		return true;

	// checking row
	for(int cCol=0; cCol < nbCols; cCol++)
	{
		if(map[row][cCol] > map[row][col])
		{
			ok2=false;
			break;
		}
	}
	return ok1 | ok2;
}

bool doTest()
{
	for(int row=0; row < nbRows; row++)
	{
		for(int col=0; col < nbCols; col++)
		{
			if(!checkSquare(row,col))
				return false;
		}
	}
	return true;
}

int main(void)
{
	int nbTests;
	scanf("%d", &nbTests);

	for(int test=0; test < nbTests; test++)
	{
		scanf("%d %d", &nbRows, &nbCols);
		for(int row=0; row < nbRows; row++)
			for(int col=0; col < nbCols; col++)
				scanf("%hd", &map[row][col]);

		printf("Case #%d: ", test+1);
		if(doTest())
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}

