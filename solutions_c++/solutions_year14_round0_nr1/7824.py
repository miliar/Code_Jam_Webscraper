#include <iostream>
#include <conio.h>
#include <fstream>
using namespace std;

ifstream input("A-small.in");
ofstream output("A-small.out");

void main()
{
	int T;
	int firstM[4][4];
	int secondM[4][4];
	int firstA, secondA;
	int firstR[4];
	int secondR[4];

	input>>T;

	for(int t=0; t<T; t++)
	{
		input>>firstA;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				input>>firstM[i][j];
			}
		}

		input>>secondA;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				input>>secondM[i][j];
			}
		}

		for(int i=0; i<4; i++)
		{
			firstR[i]=firstM[firstA-1][i];
			secondR[i]=secondM[secondA-1][i];
		}


		int match=0, num;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(firstR[i]==secondR[j])
				{
					num=firstR[i];
					match++;
				}
			}
		}

		if(match==0) output<<"Case #"<<t+1<<": "<<"Volunteer cheated!"<<endl;
		if(match==1) output<<"Case #"<<t+1<<": "<<num<<endl;
		if(match>1) output<<"Case #"<<t+1<<": "<<"Bad magician!"<<endl;
	}

	_getch();
}