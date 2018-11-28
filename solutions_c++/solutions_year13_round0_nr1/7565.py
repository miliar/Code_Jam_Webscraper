#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>

#define SIZE 4

char game[SIZE][SIZE];

void readCase();
int solveCase();

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int casesCount;

	std::cin>>casesCount;

	for (int i = 0; i <  casesCount; ++i)
	{
		readCase();

		std::cout<<"Case #"<<(i + 1)<<": ";

		switch (solveCase())
		{
		case 0:
			std::cout<<"X won";
			break;
		case 1:
			std::cout<<"O won";
			break;
		case 2:
			std::cout<<"Draw";
			break;
		case 3:
			std::cout<<"Game has not completed";
			break;
		}
		std::cout<<'\n';
	}

	return 0;
}

bool checkIfWon(char player)
{
	bool c;

	for (int i = 0; i < SIZE; i++)
	{
		c = true;

		for (int j = 0; j < SIZE; ++j)
		{
			if (game[i][j] != player && game[i][j] != 'T')
			{
				c = false;
				break;
			}
		}

		if (c)
			return true;
	}

	for (int i = 0; i < SIZE; i++)
	{
		c = true;

		for (int j = 0; j < SIZE; ++j)
		{
			if (game[j][i] != player && game[j][i] != 'T')
			{
				c = false;
				break;
			}
		}

		if (c)
			return true;
	}

	c = true;

	for (int i = 0; i < SIZE; i++)
	{
		if (game[i][i] != player && game[i][i] != 'T')
		{
			c = false;
			break;
		}
	}

	if (c)
		return true;

	c = true;

	for (int i = 0; i < SIZE; i++)
	{
		if (game[i][SIZE - i - 1] != player && game[i][SIZE - i - 1] != 'T')
		{
			c = false;
			break;
		}
	}

	if (c)
		return true;

	return false;
}

bool checkIfNotFinished()
{
	for (int i = 0; i < SIZE; ++i)
		for (int j = 0; j < SIZE; ++j)
			if (game[i][j] == '.')
				return true;
	return false;
}

int solveCase()
{
	if (checkIfWon('X'))
		return 0;
	if (checkIfWon('O'))
		return 1;
	if (checkIfNotFinished())
		return 3;
	return 2;
}

void readCase()
{
	char str[5];

	for (int i = 0; i < SIZE; ++i)
	{
		scanf("%s", str);
		memcpy(game[i], str, SIZE);
	}
	//scanf("%s", str); // read empty string
}