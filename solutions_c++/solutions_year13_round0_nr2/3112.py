#include <iostream>
#include <stdio.h>

using namespace std;

int N;
int M;
int lawn[100][100];

bool canGoFromHear(int x, int y)
{
	bool higherPointExist = false;
	for(int i = 0; i < N; ++i) 
	{
		if(lawn[x][y] < lawn[i][y])
		{
			higherPointExist = true;
			break;
		}
	}
	if(higherPointExist == false)
	{
		return true;
	}

	higherPointExist = false;
	for(int i = 0; i < M; ++i) 
	{
		if(lawn[x][y] < lawn[x][i])
		{
			higherPointExist = true;
			break;
		}
	}
	if(higherPointExist == false)
	{
		return true;
	}
	return false;
}

bool canCut()
{
	for(int i = 0; i < N; ++i)
	{
		for(int j = 0; j < M; ++j)
		{
			if(canGoFromHear(i,j) == false)
			{
				return false;
			}
		}
	}
	return true;
}

void readLawn()
{
	for(int i = 0; i < N; ++i)
	{
		for(int j = 0; j < M; ++j)
		{
			cin >> lawn[i][j];
		}
	}
}

int main()
{
	int T;
	cin >> T;

	for(int i = 0; i < T; ++i)
	{
		cin >> N;
		cin >> M;
		readLawn();
		if(canCut())
		{
			printf("Case #%d: YES", i+1);
			cout << endl;
		}
		else
		{
			printf("Case #%d: NO", i+1);
			cout << endl;
		}
	}
	return 0;
}

