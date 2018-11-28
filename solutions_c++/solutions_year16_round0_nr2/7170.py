#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream input;
	input.open("quest2.in");
	ofstream output;
	output.open("answer.in");
	int t=0,i=0,j=0,count=0;
	char pile[102];
	input>>t;
	for(j=0;j<t;j++)
	{
		count=0;
		input>>pile;
		if(pile[1]==0)
		{
			if(pile[0]=='-')
			{
				output<<"Case #"<<j+1<<": "<<1;
			}
			else
			{
				output<<"Case #"<<j+1<<": "<<0;
			}
			output<<endl;
			continue;
		}
		i=1;
		while(pile[i]!=0)
		{
			if(pile[i-1]!=pile[i])
			{
				count++;
			}
			i++;
		}
		if(pile[i-1]=='-')
		{
			count++;
		}
		output<<"Case #"<<j+1<<": "<<count<<endl;
	}
	return 0;
}
