#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <conio.h>
#include <stdio.h>
using namespace std;

int number;
int n1,a;
int cases=1;
int grid1[4][4];
int n2;
int grid2[4][4];
int counter=1;


void getNumber()
{
	int x=1;
		if (x==1)
		{
			cin>>number;
			x++;
		}
}
void getInput1()
{
	cin>>n1;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin>>grid1[i][j];
		}
	}
}
void getInput2()
{
	cin>>n2;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin>>grid2[i][j];
		}
	}
}
void comparison()
{
	for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (grid1[n1-1][i]==grid2[n2-1][j])
				{
					counter++;
					a=grid1[n1-1][i];
				}
				//cout<<grid1[n1-1][i]<<'\t'<<grid2[n2-1][j]<<endl;
			}
		}//cout<<counter<<endl;;
}
void check()
{
		if (counter==1)
		{
			cout<<"Case #"<<cases<<": "<<"Volunteer cheated!"<<endl;
		}
		if (counter==2)
		{
			cout<<"Case #"<<cases<<": "<<a<<endl;
		}
		if (counter>=3)
		{
			cout<<"Case #"<<cases<<": "<<"Bad magician!"<<endl;
		}
		//Case #1: 7
}

int main()
{
        freopen("input.txt", "rt", stdin);
        freopen("output.txt", "wt", stdout);
		
		getNumber();
		//cout<<number<<endl;
		
		for (int g = 0; g < number; g++)
		{	
		counter=1;
		getInput1();
		getInput2();
		comparison();
		check();
		cases++;
		}
}