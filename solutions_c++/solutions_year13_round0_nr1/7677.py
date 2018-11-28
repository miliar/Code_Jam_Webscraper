#include <iostream>
#include <string>

using namespace std;

int count = 0;
int N;
string str;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	scanf("%d", &N);
	getline(cin, str);
	while (N--)
	{
		string strings, substring;
		bool Owin = false, Xwin = false, isDot = false;
		int playerO[16] = {0};
		int playerX[16] = {0};
		count++;
		printf("Case #%d: ", count);
		//getline(cin, strings);
		for (int i=0; i<4; i++)
		{
			getline(cin, substring);
			strings = strings + substring;
		}
		for (int i=0; i<16; i++)
		{
			if (strings[i] == 'O')
				playerO[i] = 1;
			else if (strings[i] == 'X')
				playerX[i] = 1;
			else if (strings[i] == 'T')
				playerO[i] = playerX[i] = 1;
			else if (strings[i] == '.')
				isDot = true;
		}
		if (playerO[0] + playerO[5] + playerO[10] + playerO[15]  == 4 ||
			playerO[3] + playerO[6] + playerO[9] + playerO[12] == 4)
		{
			Owin = true;
			//printf("check 1 ");
		}
		else if (playerX[0] + playerX[5] + playerX[10] + playerX[15] == 4 ||
			playerX[3] + playerX[6] + playerX[9] + playerX[12] == 4)
		{
			Xwin = true;
			//printf("check 2 ");
		}
		for (int i=0; i<4; i++)
		{
			if (playerO[4*i] + playerO[4*i+1] + playerO[4*i+2] + playerO[4*i+3] == 4 || 
				playerO[i] + playerO[i+4] + playerO[i+8] + playerO[i+12] == 4)
			{
				Owin = true;
				//printf("check 3 ");
			}
			else if (playerX[4*i] + playerX[4*i+1] + playerX[4*i+2] + playerX[4*i+3] == 4 || 
				playerX[i] + playerX[i+4] + playerX[i+8] + playerX[i+12] == 4)
			{
				Xwin = true;
				//printf("check 4 ");
			}
		}
		if (Owin)
			printf("O won\n");
		else if (Xwin)
			printf("X won\n");
		else if (isDot == false)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
		getline(cin, strings);
	}
	return 0;
}