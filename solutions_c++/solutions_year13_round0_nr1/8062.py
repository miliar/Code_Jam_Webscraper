#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int getValue(ifstream& infile)
{
	string line;
	getline(infile,line);
	return atoi(line.c_str());
}

int Winner(string l1,string l2,string l3,string l4,char c)
{
	
	if (l1[0] ==c && l1[1] == c && l1[2] == c && l1[3] == c)//H1
		return 1;
	else if (l2[0] ==c && l2[1] ==c &&l2[2]  ==c && l2[3]== c)//H2
		return 1;
	else if (l3[0]  ==c && l3[1] ==c &&l3[2]  ==c && l3[3]== c)//H3
		return 1;
	else if (l4[0]  ==c && l4[1]  ==c &&l4[2]  ==c && l4[3]== c)//H4
		return 1;
	else if (l1[0] ==c &&l2[0] ==c &&l3[0]  ==c && l4[0]== c)//V1
		return 1;
	else if (l1[1] ==c && l2[1]  ==c &&l3[1] ==c &&l4[1]== c)//V2
		return 1;
	else if (l1[2] ==c && l2[2] ==c && l3[2] ==c && l4[2]== c)//V3
		return 1;
	else if (l1[3]  ==c && l2[3]  ==c && l3[3] ==c && l4[3]== c)//V4
		return 1;
	else if (l1[0]  ==c && l2[1]  ==c && l3[2]  ==c && l4[3]== c)//D1
		return 1;
	else if (l1[3]  ==c && l2[2] ==c && l3[1]  ==c && l4[0]== c)//D2
		return 1;
	return 0;
}
char  CheckX(string l1,string l2,string l3,string l4)
{
	for (int i = 0; i < 4; i++)
	{
		if(l1[i] == 'T')
		{
			l1[i] = 'X';
			break;
		}
		if(l2[i] == 'T')
		{
			l2[i] = 'X';
			break;
		}
		if(l3[i] == 'T')
		{
			l3[i] = 'X';
			break;
		}
		if(l4[i] == 'T')
		{
			l4[i] = 'X';
			break;
		}
	}
	if (1 == Winner(l1,l2,l3,l4,'X'))
		return 'X';
	return 'D';
}
char  CheckO(string l1,string l2,string l3,string l4)
{
	for (int i = 0; i < 4; i++)
	{
		if(l1[i] == 'T')
		{
			l1[i] = 'O';
			break;
		}
		if(l2[i] == 'T')
		{
			l2[i] = 'O';
			break;
		}
		if(l3[i] == 'T')
		{
			l3[i] = 'O';
			break;
		}
		if(l4[i] == 'T')
		{
			l4[i] = 'O';
			break;
		}
	}
	if (1 == Winner(l1,l2,l3,l4,'O'))
		return 'O';
	return 'D';
}



char CheckWin(string l1,string l2,string l3,string l4)
{
	char _win = CheckX(l1,l2,l3,l4);
	if(_win =='X')
		return _win;
	_win = CheckO(l1,l2,l3,l4);
	if(_win =='O')
		return _win;

	for (int i = 0; i < 4; i++)
	{
		if(l1[i] == '.' ||l2[i] == '.'||l3[i] == '.'||l4[i] == '.')
		{
			_win = 'N';
			break;
		}
	}
	if(_win =='N')
		return _win;

	return 'D';
}
void main()
{
	string line;
	ifstream myfile;
	ofstream outfile;
	myfile.open ("C:\\Users\\ahmed\\Documents\\Visual Studio 2012\\Projects\\Tic Tac Toe\\Debug\\A-small-attempt0.in");
	outfile.open ("C:\\Users\\ahmed\\Documents\\Visual Studio 2012\\Projects\\Tic Tac Toe\\Debug\\A-small-attempt0.out");
	
	int TestCases;
	string GameLine[50];
	int counter = 0;

	if(myfile.is_open())
	{		
		TestCases = getValue(myfile);
	
		for (int i = 0; i < TestCases;i++)
		{	

			getline(myfile,GameLine[counter++]);
			getline(myfile,GameLine[counter++]);
			getline(myfile,GameLine[counter++]);
			getline(myfile,GameLine[counter++]);
			//empty line
			getline(myfile,line);
		}

		
		if(outfile.is_open())
		{
			int _lineIndex=0;
			for (int i=0;i<TestCases;i++)
			{
				char Case = CheckWin(GameLine[_lineIndex],GameLine[_lineIndex+1],GameLine[_lineIndex+2],GameLine[_lineIndex+3]);
				_lineIndex = _lineIndex+4;
				switch (Case)
				{
				case 'X':
					outfile << "Case #"<<i+1<<": X won"<<endl;
					break;
				case 'O':
					outfile << "Case #"<<i+1<<": O won"<<endl;
					break;
				case 'D':
					outfile << "Case #"<<i+1<<": Draw"<<endl;
					break;
				case 'N':
					outfile << "Case #"<<i+1<<": Game has not completed"<<endl;
					break;
				default:
					break;
				}
			}
		}
	}
	
	myfile.close();
	outfile.close();
}