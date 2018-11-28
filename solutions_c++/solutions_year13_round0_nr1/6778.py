#include <string>
#include <cstdio>

using namespace std;

char board[4][5];

int main ()
{
	//freopen("salidaA.txt","w",stdout);

	int T;
	scanf("%d",&T);

	for (int t = 1; t <= T; ++t)
	{
		char linea;
		for (int i = 0; i < 4; ++i)
			scanf("%s",board[i]);

		scanf("%c",&linea);

		int O=0,X=0,W=0, N = 0;
		for (int i = 0; i < 4; ++i)
		{
			if (board[i][i] == 'X')
				++X;
			else if (board[i][i] == 'O')
				++O;
			else if (board[i][i] == 'T')
				++W;
			else
				++N;
		}

		int winner = 0;

		if ( O + W == 4 )
			winner = 1;
		else if (X + W == 4)
			winner = -1;

		if (!winner)
		{
			O=0;X=0;W=0;N = 0;
			for (int i = 0; i < 4; ++i)
			{
				if (board[3-i][i] == 'X')
					++X;
				else if (board[3-i][i] == 'O')
					++O;
				else if (board[3-i][i] == 'T')
					++W;
				else
					++N;
			}

			if ( O + W == 4 )
				winner = 1;
			else if (X + W == 4)
				winner = -1;
		}

		if (!winner)
		{
			N = 0;
			for (int i = 0; i < 4; ++i)
			{
				int O1=0,X1=0,W1=0;
				int O2=0,X2=0,W2=0;

				for (int j = 0; j < 4; ++j)
				{
					if (board[i][j] == 'X')
						++X1;
					else if (board[i][j] == 'O')
						++O1;
					else if (board[i][j] == 'T')
						++W1;
					else
						++N;

					if (board[j][i] == 'X')
						++X2;
					else if (board[j][i] == 'O')
						++O2;
					else if (board[j][i] == 'T')
						++W2;
				}

				if ( O1 + W1 == 4 )
					winner = 1;
				else if (X1 + W1 == 4)
					winner = -1;

				if ( O2 + W2 == 4 )
					winner = 1;
				else if (X2 + W2 == 4)
					winner = -1;

				if (winner)
					break;
			}
		}

		if (winner)
			printf("Case #%d: %c won\n",t, winner == 1 ? 'O' : 'X');
		else
		{
			if (N)
				printf("Case #%d: Game has not completed\n",t);
			else
				printf("Case #%d: Draw\n",t);
		}	
	}
	return 0;
}
