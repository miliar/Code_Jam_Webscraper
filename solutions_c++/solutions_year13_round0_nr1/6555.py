#include <iostream>
using namespace std;

char mas[4][4]={{0}};
int res[2]={0};

void check1()
{
	for (int i=0; i<4; i++)
		if (mas[i][0]==mas[i][1] && mas[i][1]==mas[i][2] && mas[i][2]==mas[i][3])
		{
			if (mas[i][0] == 'X')
				res[0]=1;
			else
				if (mas[i][0]=='O')
					res[1]=1;
		}
}

void check2()
{
	for (int j=0; j<4; j++)
		if (mas[0][j]==mas[1][j] && mas[1][j]==mas[2][j] && mas[2][j]==mas[3][j])
		{
			if (mas[0][j] == 'X')
				res[0]=1;
			else
				if (mas[0][j]=='O')
					res[1]=1;
		}
}

void check3()
{
	if (mas[0][0]==mas[1][1] && mas[1][1]==mas[2][2] && mas[2][2]==mas[3][3])
	{
		if (mas[0][0] == 'X')
				res[0]=1;
			else
				if (mas[0][0]=='O')
					res[1]=1;
	}
}

void check4()
{
	if (mas[0][3]==mas[1][2] && mas[1][2]==mas[2][1] && mas[2][1]==mas[3][0])
	{
		if (mas[0][3] == 'X')
				res[0]=1;
			else
				if (mas[0][3]=='O')
					res[1]=1;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	char c;
	bool flag = false;
	bool point=false;
	int m=0, n=0;
	for (int i=1; i<=t; ++i)
	{
		res[1]=0, res[0]=0;
		flag = false;
		point=false;
		cout << "Case #" << i << ": ";
		for (int j=0; j<4; j++)
			for (int k=0; k<4; k++)
			{
				cin >> mas[j][k];
				if (mas[j][k] == 'T')
				{
					flag = true;
					m=j;
					n=k;
				}
				if (mas[j][k]=='.')
					point=true;
			}
		//cin >> c >> c;
		if (flag)
		{
			mas[m][n]='X';
			check1();
			check2();
			check3();
			check4();
			mas[m][n]='O';
			check1();
			check2();
			check3();
			check4();
		}
		else
		{
			check1();
			check2();
			check3();
			check4();
		}
		if (res[0]==1 && res[1]==0)
			cout << "X won\n";
		else
		{
			if (res[1]==1 && res[0]==0)
				cout << "O won\n";
			else if (point)
				cout << "Game has not completed\n";
			else
				cout << "Draw\n";
		}

	}
	return 0;
}