#include <iostream>
#include <cstring>
using namespace std;


char tab[4][4];
int xT, yT;

bool testFor(char k)
{
	bool res = false;
	
	res |= tab[0][0] == k && tab[0][1] == k && tab[0][2] == k && tab[0][3] == k;
	res |= tab[1][0] == k && tab[1][1] == k && tab[1][2] == k && tab[1][3] == k;
	res |= tab[2][0] == k && tab[2][1] == k && tab[2][2] == k && tab[2][3] == k;
	res |= tab[3][0] == k && tab[3][1] == k && tab[3][2] == k && tab[3][3] == k;
	
	res |= tab[0][0] == k && tab[1][0] == k && tab[2][0] == k && tab[3][0] == k;
	res |= tab[0][1] == k && tab[1][1] == k && tab[2][1] == k && tab[3][1] == k;
	res |= tab[0][2] == k && tab[1][2] == k && tab[2][2] == k && tab[3][2] == k;
	res |= tab[0][3] == k && tab[1][3] == k && tab[2][3] == k && tab[3][3] == k;
	
	res |= tab[0][0] == k && tab[1][1] == k && tab[2][2] == k && tab[3][3] == k;
	res |= tab[0][3] == k && tab[1][2] == k && tab[2][1] == k && tab[3][0] == k;
	
	return res;
}

int main()
{
	int nTest;
	cin>>nTest;
	
	
	int test = 0;
	while (nTest--)
	{
		
	bool exT = false;
		test++;
		bool complete = true;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>tab[i][j];
				if (tab[i][j] == 'T') xT = i, yT = j, exT = true;
				if (tab[i][j] == '.') complete = false;
			}
			
		}
		
		string res = "";
		
		bool X, O;
		
		if (exT) tab[xT][yT] = 'X';
		X = testFor('X');
		if (exT) tab[xT][yT] = 'O';
		O = testFor('O');
		
		if (X && O) res = "Draw";
		else
		{
			if (X) res = "X won";
			else if (O) res = "O won";
			else if (complete) res = "Draw"; 
			else res = "Game has not completed";
		} 
		
		
		cout<<"Case #"<<test<<": "<<res<<endl;
	}
	
	return 0;
}
