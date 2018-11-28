#include <iostream>
#include <fstream>

using namespace std;

char v[4][4];

inline int isWin(){
	int a = 0, b = 0, i = 0, j = 0;
	bool cond = false;
	
	for(i = 0; i < 4; i++)
	{
		for(a = 0, b = 0, j = 0; j < 4; j++)
		{
			if(v[i][j] == 'X')
				a++;
			else if(v[i][j] == 'O')
				b++;
			else if(v[i][j] == 'T')
			{
				a++;
				b++;
			} else
				cond = true;
		}
		if(a == 4)
			return 1;
		if(b == 4)
			return 2;
	}
	
	for(i = 0; i < 4; i++)
	{
		for(a = 0, b = 0, j = 0; j < 4; j++)
		{
			if(v[j][i] == 'X')
				a++;
			else if(v[j][i] == 'O')
				b++;
			else if(v[j][i] == 'T')
			{
				a++;
				b++;
			}
		}
		if(a == 4)
			return 1;
		if(b == 4)
			return 2;
	}
	
	for(a = 0, b = 0, j = 0; j < 4; j++)
	{
		if(v[j][j] == 'X')
			a++;
		else if(v[j][j] == 'O')
			b++;
		else if(v[j][j] == 'T')
		{
			a++;
			b++;
		}
	}
	if(a == 4)
		return 1;
	if(b == 4)
		return 2;
	
	for(a = 0, b = 0, j = 0; j < 4; j++)
	{
		if(v[j][3 - j] == 'X')
			a++;
		else if(v[j][3 - j] == 'O')
			b++;
		else if(v[j][3 - j] == 'T')
		{
			a++;
			b++;
		}
	}
	if(a == 4)
		return 1;
	if(b == 4)
		return 2;
	
	if(cond)
		return 3;
	return 0;
}


int main()
{
	int t = 0, i = 0, j = 0, k = 0;
	ofstream fcout("resultado.txt");
	ifstream fcin("entrada.txt");
	
	fcin>>t;
	for(i = 1; i <= t; i++)
	{
		for(j = 0; j < 4; j++)
			fcin>>v[j];
		k = isWin();
		if(k == 0)
			fcout<<"Case #"<<i<<": Draw"<<endl;
		else if(k == 1)
			fcout<<"Case #"<<i<<": X won"<<endl;
		else if(k == 2)
			fcout<<"Case #"<<i<<": O won"<<endl;
		else
			fcout<<"Case #"<<i<<": Game has not completed"<<endl;
	}
	
	return 0;
}
