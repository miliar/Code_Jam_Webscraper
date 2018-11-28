#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

vector <string> vec;
bool flag=false;
int sol(char c)
{
	flag=false;
	int cont;
	for(int i=0;i<4;i++)
	{
		cont=0;
		for(int j=0;j<4;j++)
		{
			if(vec[i][j]=='.')
			{
				flag=true;
				break;
			}
			if(vec[i][j]==c || vec[i][j]=='T')
				cont++;
		}
		if(cont==4)
			return 1;
	}
	for(int i=0;i<4;i++)
	{
		cont=0;
		for(int j=0;j<4;j++)
		{
			if(vec[j][i]=='.')
			{
				flag=true;
				break;
			}
			if(vec[j][i]==c || vec[i][j]=='T')
				cont++;
		}
		if(cont==4)
			return 1;
	}
	cont=0;
	for(int i=0,j=0;i<4;i++,j++)
	{
	
		if(vec[i][j]=='.')
		{
			flag=true;
			break;
		}
		if(vec[i][j]==c || vec[i][j]=='T')
			cont++;
	}
	if(cont==4)
		return 1;
	cont=0;
	for(int i=0,j=3;i<4;i++,j--)
	{
		if(vec[i][j]=='.')
		{
			flag=true;
			break;
		}
		if(vec[i][j]==c || vec[i][j]=='T')
			cont++;
	}
	if(cont==4)
		return 1;
	return 0;
}
main()
{
	string aux;
	int n,O,X;
	
	scanf("%d\n",&n);
	for(int k=0;k<n;k++)
	{
		vec.clear();
		for(int i=0;i<4;i++)
		{
			getline(cin,aux);
			vec.push_back(aux);
		}
		getline(cin,aux);
		O=sol('O');
		X=sol('X');
		if(X>O)
			cout << "Case #" << k+1 << ": X won\n";
		if(O>X)
			cout << "Case #" << k+1 << ": O won\n";
		if(O==X)
			if(flag)
				cout << "Case #" << k+1 << ": Game has not completed\n";
			else
				cout << "Case #" << k+1 << ": Draw\n";
	}
}
