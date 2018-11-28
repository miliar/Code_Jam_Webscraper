
#include <stdio.h>

char lawn[100][100];
int n, m;

void readLawn()
{
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
		{
			scanf(" %d", &lawn[i][j]);
		}
}

bool noMoreInRowThan(int row, int val)
{
	for(int j=0; j<m; j++)
		if(lawn[row][j] > val) return false;

	return true;
}

bool noMoreInColumnThan(int kol, int val)
{
	for(int i=0; i<n; i++)
		if(lawn[i][kol] > val) return false;

	return true;
}

bool canCut(int i, int j)
{
	return noMoreInRowThan(i, lawn[i][j]) ||
		   noMoreInColumnThan(j, lawn[i][j]);
}

bool canCut()
{
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
		{
			if(!canCut(i, j)) return false;
		}
	return true;
}

int main()
{
	int count;
	scanf("%d", &count);

	for(int i=0; i<count; i++)
	{
		scanf("%d%d", &n, &m);
		readLawn();

		printf("Case #%d: %s\n", i+1, canCut()? "YES" : "NO");
	}
	return 0;
}
