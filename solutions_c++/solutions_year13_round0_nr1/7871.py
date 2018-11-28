#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int whoWins(vector<string>);
void compareChar(char);
void reset();
void main()
{
	ifstream input;
	ofstream output;
	string i; 
	int caseNumber;
	int c=0;
	int result;
	vector<string>tmp;
	vector<string>lines;
	vector<string>::iterator it;
	vector<vector<string>>cases;
	vector<string>test;

	input.open("A-large.in", ios::in); //be sure to change the name
	output.open("output.txt", ios::out);
	if(!input)
		cerr<<"Error in opening file"<<endl;
	while(!input.eof())
	{
		getline(input,i);
		if(i.compare("")!=0)
		{
			lines.push_back(i);
		}
	}
	caseNumber=atoi(lines[0].c_str());
	cout<<caseNumber<<"\n\n\n"<<endl;
	it=lines.begin();
	lines.erase(it);


	for(int count=0; count<lines.size(); count++)
	{
		if(lines[count].compare("")==0 || lines[count].compare("\n")==0)
			continue;
		tmp.push_back(lines[count]);
		if((count+1)%4==0)
		{
			cases.push_back(tmp);
			tmp.clear();
		}

	}

	for(int count=0; count<cases.size(); count++)
	{
		for(int count2=0; count2<cases[count].size(); count2++)
		{
			cout<<cases[count][count2]<<endl;
		}
		cout<<endl;
	}

	for(int count=0; count<cases.size(); count++) //determine the cases
	{
		result=whoWins(cases[count]);
		output<<"Case #"<<count+1<<": ";
		if(result==1)
			output<<"X won"<<endl;
		else if(result==2)
			output<<"O won"<<endl;
		else if(result==3)
			output<<"Draw"<<endl;
		else if(result==4)
			output<<"Game has not completed"<<endl;
	}
	output.close();


}
int xCount, oCount, tCount;
int whoWins(vector<string> tmp)
{
//	string line;
	reset();
	for(int count=0; count<tmp.size(); count++) //rows
	{
		for(int count2=0; count2<tmp[count].size(); count2++)
		{
			compareChar(tmp[count][count2]);
		}
		if(xCount==4 || (xCount==3 && tCount==1))
			return 1;
		else if(oCount==4 || (oCount==3 && tCount==1))
			return 2;
		reset();
	}
	

	reset();

	for(int count=0; count<tmp.size(); count++) //columns
	{
		for(int count2=0; count2<tmp[count].size(); count2++)
		{
			compareChar(tmp[count2][count]);
		}
		if(xCount==4 || (xCount==3 && tCount==1)) 
			return 1;
		else if(oCount==4 || (oCount==3 && tCount==1))
			return 2;	
		reset();
	}


	reset();

	for(int count=0; count<tmp.size(); count++) //left-down diagonal
	{
		compareChar(tmp[count][count]);
	}
	if(xCount==4 || (xCount==3 && tCount==1))
		return 1;
	else if(oCount==4 || (oCount==3 && tCount==1))
		return 2;

	reset();
	for(int count=0; count<tmp.size(); count++) //right-down diagonal
	{
		compareChar(tmp[count][3-count]);
	}
	if(xCount==4 || (xCount==3 && tCount==1))
		return 1;
	else if(oCount==4 || (oCount==3 && tCount==1))
		return 2;
	reset();

	for(int count=0; count<tmp.size(); count++) //if not finished
	{
		for(int count2=0; count2<tmp[count].size(); count2++)
		{
			if(tmp[count][count2]=='.')
				return 4;

		}
	}
	return 3;


}
void compareChar(char c)
{
	if(c=='X')
		++xCount;
	else if(c=='O')
		++oCount;
	else if(c=='T')
		++tCount;
	else if(c=='.')
		;
	else
		cerr<<"EPIC FAIL"<<endl;
}
void reset()
{
	xCount=0;
	oCount=0;
	tCount=0;
}