#include<cstdio>
#include<cstdlib>

char tictactoe[4][4];

int main()
{
	int nbTest;
	scanf("%d\n", &nbTest);
	
	for(int i = 1; i <= nbTest; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			for(int k = 0; k < 4; ++k)
			{
				scanf("%c", &tictactoe[j][k]);
			}
			scanf("\n");
		}
		
		bool libre = false;
		int X;
		int O;
		int T;
		
		bool fini = false;
		//ligne
		for(int j = 0; j < 4; ++j)
		{
			X = 0;
			O = 0;
			T = 0;
			for(int k = 0; k < 4; ++k)
			{
				if(tictactoe[j][k] == 'X')
				{
					X++;	
				}
				else if(tictactoe[j][k] == 'O')
				{
					O++;
				}
				else if(tictactoe[j][k] == 'T')
				{
					T++;
				}
				else
				{
					libre = true;
				}
			}
			if(X+T == 4)
			{
				printf("Case #%d: X won\n", i);
				fini = true;
			}
			else if(O+T == 4)
			{
				printf("Case #%d: O won\n", i);
				fini = true;
			}
		}
		if(fini)
			continue;
			
		//column
		for(int j = 0; j < 4; ++j)
		{
			X = 0;
			O = 0;
			T = 0;
			for(int k = 0; k < 4; ++k)
			{
				if(tictactoe[k][j] == 'X')
				{
					X++;	
				}
				else if(tictactoe[k][j] == 'O')
				{
					O++;
				}
				else if(tictactoe[k][j] == 'T')
				{
					T++;
				}
				else
				{
					libre = true;
				}
			}
			if(X+T == 4)
			{
				printf("Case #%d: X won\n", i);
				fini = true;
			}
			else if(O+T == 4)
			{
				printf("Case #%d: O won\n", i);
				fini = true;
			}
		}
		//diag
		if(fini)
			continue;
		X = 0;
		O = 0;
		T = 0;	
		for(int j = 0; j < 4; ++j)
		{
			if(tictactoe[j][j] == 'X')
			{
				X++;	
			}
			else if(tictactoe[j][j] == 'O')
			{
				O++;
			}
			else if(tictactoe[j][j] == 'T')
			{
				T++;
			}
			else
			{
				libre = true;
			}
		}
		if(X+T == 4)
		{
			printf("Case #%d: X won\n", i);
			fini = true;
		}
		else if(O+T == 4)
		{
			printf("Case #%d: O won\n", i);
			fini = true;
		}
		
		if(fini)
			continue;
		X = 0;
		O = 0;
		T = 0;	
		for(int j = 0; j < 4; ++j)
		{
			if(tictactoe[3 - j][j] == 'X')
			{
				X++;	
			}
			else if(tictactoe[3 - j][j] == 'O')
			{
				O++;
			}
			else if(tictactoe[3 - j][j] == 'T')
			{
				T++;
			}
			else
			{
				libre = true;
			}
		}
		if(X+T == 4)
		{
			printf("Case #%d: X won\n", i);
			fini = true;
		}
		else if(O+T == 4)
		{
			printf("Case #%d: O won\n", i);
			fini = true;
		}
		
		if(!fini)
		{
			if(libre)
				printf("Case #%d: Game has not completed\n", i);
			else
				printf("Case #%d: Draw\n", i);
		}
	}
	return 0;
}
