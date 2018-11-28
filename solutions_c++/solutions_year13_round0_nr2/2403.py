#include <stdio.h>

int n, m;
int data[106][106];

void inputData()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++ i)
	{
		for (int j = 0; j < m; ++ j)
		{
			scanf("%d", &data[i][j]);
		}
	}
}

bool checkRow(int row, int tag)
{
	for (int i = 0; i < m; ++ i)
	{
		if (data[row][i] > tag)
		{
			return false;
		}
	}
	
	return true;
}

bool checkCol(int col, int tag)
{
	for (int i = 0; i < n; ++ i)
	{
		if (data[i][col] > tag)
		{
			return false;
		}
	}
	
	return true;
}

void process(int cases)
{
	bool ret = true;
	for (int i = 0; i < n; ++ i)
	{
		for (int j = 0; j < m; ++ j)
		{
			if (!checkRow(i, data[i][j]) && !checkCol(j, data[i][j]))
			{
				ret = false;
				break;
			}
		}
	}
	
	printf("Case #%d: %s\n", cases, ret ? "YES" : "NO");
}

int main()
{
	//freopen("E:\\codejam\\B\\B\\B-large.in", "r", stdin);
	//freopen("E:\\codejam\\B\\B\\out.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; ++ i)
	{
		inputData();
		process(i);
	}
	return 0;
}