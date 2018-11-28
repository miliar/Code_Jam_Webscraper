#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int checker(string temp[])
{
	bool win= false;
	bool empty = false;
	int count;
	char winner= ' ';
	int resultCase = 0;

	//For Rows	
	for(int i=0;i<4;i++)
	{
		char buffer=' ';
		count=0;
		char current=' ';
		char next=' ';	
		for(int j=0;j<3;j++)
		{
			buffer = temp[i][j];
			if(buffer=='T')
			{
				count++;
				continue;
			
			}
			current = temp[i][j];
			next = temp[i][j+1];

			if(current==next || next=='T')
			count++;

			if(current=='.' || next=='.')
			empty = true;
			
		}
		if(count==3)
		{
			win = true;
			if(current=='X' || current=='O')
			winner = current;
			else
			winner = next;
			break;
			
		}
	}
	
//For Column
if(win==false)
{
	for(int i=0;i<4;i++)
	{
		char buffer=' ';
		count=0;
		char current=' ';
		char next=' ';
		for(int j=0;j<3;j++)
		{
			buffer = temp[j][i];
			if(buffer=='T')
			{
				count++;
				continue;
			
			}
			current = temp[j][i];
			next = temp[j+1][i];

			if(current==next || next=='T')
			count++;

			if(current=='.' || next=='.')
			empty = true;
			
		}
		if(count==3)
		{
			win = true;
			if(current=='X' || current=='O')
			winner = current;
			else
			winner = next;
			break;
			
		}
	}
}	

//For Dialgonal 1
if(win==false)
{
	count=0;
	char current=' ';
	char next=' ';
	for(int i=0;i<3;i++)
	{
		char buffer=' ';
		buffer = temp[i][i];
		if(buffer=='T')
		{
				count++;
				continue;
			
		}
		current = temp[i][i];
		next = temp[i+1][i+1];

		if(current==next || next=='T')
		count++;

		if(current=='.' || next=='.')
		empty = true;
			
	}
	if(count==3)
	{
		win = true;
		if(current=='X' || current=='O')
		winner = current;
		else
		winner = next;		
	}	
}
//For Diagonal 2
{
	int j;
	count=0;
	char buffer=' ';
	char current=' ';
	char next =' ';
	for(int i=0;i<3;i++)
	{		
		j = 3-i;
		buffer = temp[i][j];

		if(buffer=='T')
		{
			count++;
			continue;
			
		}

		

		 current = temp[i][j];
		 next  = temp[i+1][j-1];

		cout<<current<<" " <<next<<endl;
			

		if(current==next || next=='T')
		count++;

		if(current=='.' || next=='.')
		empty = true;
			
	}
	
	if(count==3)
	{
		win = true;
				
		if(current=='X' || current=='O')
		{

			winner = current;
		}
		else
		{
			winner = next;	
		}
	}		
}
if(win==true)
{
	if(winner=='X')
	resultCase = 1;
	else if(winner=='O')
	resultCase = 2;
}
else
{
	if(empty == false)
	resultCase = 3;
	else
	resultCase = 4;
}
	
return resultCase;
}
int main(int argc,char *argv[])
{
	ifstream in(argv[1]);
	ofstream out("tictac.out");
	int testCases = 0;
	int resultCase;
	int caseCount = 0;
	string temp[4];

	if(in)
	{
		in>>testCases;

		while(testCases > 0)
		{
			caseCount++;
			in>>temp[0];
			in>>temp[1];
			in>>temp[2];
			in>>temp[3];
		
			resultCase  = checker(temp);
		
			if(resultCase==1)
			out<<"Case #"<<caseCount<<": "<<"X won"<<endl;
			else if(resultCase==2)
			out<<"Case #"<<caseCount<<": "<<"O won"<<endl;
			else if(resultCase==3)
			out<<"Case #"<<caseCount<<": "<<"Draw"<<endl;
			else
			out<<"Case #"<<caseCount<<": "<<"Game has not completed"<<endl;
	
			testCases--;
		}		
	}
}
