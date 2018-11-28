#include <iostream>
#include <conio.h>
#include <fstream>

using namespace std;

int main()
{
	int T=0;
	int row=0;
	int first[4];
	int second[4];
	int answer[4];
	ifstream input;
	ofstream output;
	output.open("output.txt");
	input.open("input.in");
	
	input>>T;

	for(int i=1; i<=T; i++)
	{
		input>>row;
		//skip to correct line
		for(int j=0; j<row; j++)
		{
			input.ignore(256, '\n');
		}
		//get the line
		for(int j=0; j<4; j++)
		{
			input>>first[j];
		}
		//skip the remaining lines
		for(int j=0; j<=4-row; j++)
		{
			input.ignore(256, '\n');
		}
		input>>row;
		//skip to correct line
		for(int j=0; j<row; j++)
		{
			input.ignore(256, '\n');
		}
		//get the line
		for(int j=0; j<4; j++)
		{
			input>>second[j];
		}
		//skip the remaining lines
		for(int j=0; j<=4-row; j++)
		{
			input.ignore(256, '\n');
		}
		int p=0;
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				if(first[j]==second[k])
				{
					answer[p]=first[j];
					p++;
				}
			}
		}

		output<<"Case #"<<i<<": ";
		if(p==1)//found only one match = give card number
			output<<answer[0]<<endl;
		else if(p==0)//found no matches = cheater
			output<<"Volunteer cheated!"<<endl;
		else//found multiple matches = bad magician
			output<<"Bad magician!"<<endl;

	}

	input.close();
	output.close();

	cout<<"Done.";
	_getch();
}