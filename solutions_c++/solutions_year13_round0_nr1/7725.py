#include <iostream>
using namespace std;

int res(char board[][4])
{
	char tmp[4];
	bool isfilled = true;
	for (int i=0; i<4; i++)
	{
		for (int j=0; j<4; j++)
		{
			if ('.' == board[i][j])
			{
				isfilled = false;
				break;
			}
			if (!isfilled)
			{
				break;
			}
		}
	}

	int cX, cO, cT;

	//// case 1
	tmp[0] = board[0][0];
	tmp[1] = board[1][1];
	tmp[2] = board[2][2];
	tmp[3] = board[3][3];
	cX = 0;
	cO = 0;
	cT = 0;
	for (int i=0; i<4; i++)
	{
		if ('O' == tmp[i])
		{
			cO ++;
		}
		if ('X' == tmp[i])
		{
			cX ++;
		}
		if ('T' == tmp[i])
		{
			cT ++;
		}
	}
	if (4 == cX || (3 == cX && 1 == cT))
	{
		return 1;		
	}
	if (4 == cO || (3 == cO && 1 == cT))
	{
		return 2;		
	}
	////case 2
	tmp[0] = board[0][3];
	tmp[1] = board[1][2];
	tmp[2] = board[2][1];
	tmp[3] = board[3][0];
	cX = 0;
	cO = 0;
	cT = 0;
	for (int i=0; i<4; i++)
	{
		if ('O' == tmp[i])
		{
			cO ++;
		}
		if ('X' == tmp[i])
		{
			cX ++;
		}
		if ('T' == tmp[i])
		{
			cT ++;
		}
	}
	if (4 == cX || (3 == cX && 1 == cT))
	{
		return 1;		
	}
	if (4 == cO || (3 == cO && 1 == cT))
	{
		return 2;		
	}
	////case 3
	for (int i=0; i<4; i++)
	{
		for (int j=0; j<4; j++)
		{
			tmp[j] = board[i][j];
		}
		cX = 0;
		cO = 0;
		cT = 0;
		for (int j=0; j<4; j++)
		{
			if ('O' == tmp[j])
			{
				cO ++;
			}
			if ('X' == tmp[j])
			{
				cX ++;
			}
			if ('T' == tmp[j])
			{
				cT ++;
			}
		}
		if (4 == cX || (3 == cX && 1 == cT))
		{
			return 1;		
		}
		if (4 == cO || (3 == cO && 1 == cT))
		{
			return 2;		
		}
	}
	////case 4
	for (int i=0; i<4; i++)
	{
		for (int j=0; j<4; j++)
		{
			tmp[j] = board[j][i];
		}
		cX = 0;
		cO = 0;
		cT = 0;
		for (int j=0; j<4; j++)
		{
			if ('O' == tmp[j])
			{
				cO ++;
			}
			if ('X' == tmp[j])
			{
				cX ++;
			}
			if ('T' == tmp[j])
			{
				cT ++;
			}
		}
		if (4 == cX || (3 == cX && 1 == cT))
		{
			return 1;		
		}
		if (4 == cO || (3 == cO && 1 == cT))
		{
			return 2;		
		}
	}
	////other
	if (isfilled)
	{
		return 3;
	}
	else
	{
		return 4;
	}
}
int main()
{
	//freopen("D:\\A-large.in", "r+", stdin);
	//freopen("D:\\A-large.out", "w+", stdout);
	int T;
	cin>>T;
	char board[4][4];

	for (int t=1; t<=T; t++)
	{
		for (int i=0; i<4; i++)
		{
			for (int j=0; j<4; j++)
			{
				cin>>board[i][j];
			}
		}

		cout<<"Case #"<<t<<": ";
		int ans = res(board);
		if (1 == ans)
		{
			cout<<"X won"<<endl;
		}
		if (2 == ans)
		{
			cout<<"O won"<<endl;
		}
		if (3 == ans)
		{
			cout<<"Draw"<<endl;
		}
		if (4 == ans)
		{
			cout<<"Game has not completed"<<endl;
		}
	}

	return 0;
}