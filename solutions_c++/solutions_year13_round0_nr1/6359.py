#include <iostream>
#include <string>
#include <fstream>


#define X_won "X won";
#define O_won "O won";
#define Draw "Draw";
#define Go_on "Game has not completed";

using namespace std;




string gameDetermine(int status[4][4])
{
	string result = "";
	bool IsDotExist = false;
	bool IsDraw = true;
	int tenlines[10];
	for(unsigned int i =0;i<4;i++)
	{
		tenlines[i]=status[i][0]+status[i][1]+status[i][2]+status[i][3];
	}
	for(unsigned int i =0;i<4;i++)
	{
		tenlines[i+4]=status[0][i]+status[1][i]+status[2][i]+status[3][i];
	}
	tenlines[8]=status[0][0]+status[1][1]+status[2][2]+status[3][3];
	tenlines[9]=status[0][3]+status[1][2]+status[2][1]+status[3][0];

	for(unsigned int i=0;i<10;i++)
	{
		if(tenlines[i]>=97)
			IsDotExist = true;
		else
		{
			if(tenlines[i]==4 || tenlines[i]==3)
			{
				result = X_won;
				IsDraw = false;
				break;
			}
			
			if(tenlines[i]==-4 || tenlines[i]==-3)
			{
				result = O_won;
				IsDraw = false;
				break;
			}	
		}
	}
	
	if(IsDraw)
	{
		if(IsDotExist)
		{result = Go_on;}
		else
		{result = Draw;}
	}

	return result;
}

int main()
{
	//string inputfilename="input.txt";
	//string outputfilename="output.txt";

	ifstream infile;
	ofstream outfile;
	infile.open("D:\A-large.in");
	outfile.open("D:\A-large.out");
	//infile.open(inputfilename.c_str());
	//outfile.open(outputfilename.c_str());	
	if(!infile.is_open())
		cout<<"can not open input file"<<endl;
	if(!outfile.is_open())
		cout<<"can not open output file"<<endl;
	
	int status[4][4];
	long numCases = 0;
	string aline;
	//get the number of cases
	getline(infile, aline);
	//infile>>aline;
	numCases = ::atol(aline.c_str());

	//store the cases

	//process
	for(unsigned int i=1;i<=numCases;i++)
	{
		unsigned j=0;
		for(;j<4;j++)
		{
			getline(infile,aline);
			unsigned k=1;
			for(unsigned k=0;k<4;k++)
			{
				if(aline[k]=='T')
					status[j][k]=0;
				else if(aline[k]=='X')
					status[j][k]=1;
				else if(aline[k]=='O')
					status[j][k]=-1;
				else
					status[j][k]=100;//"."
				//cout<<status[j][k];
			}
			//cout<<endl;

		}

		getline(infile,aline);//process the blank line
		//cout<<endl;

		//process each case
		string result = gameDetermine(status);
		outfile<<"Case #"<<i<<": "<<result<<endl;
		//cout<<"Case #"<<i<<": "<<result<<endl;
	}

	infile.close();
	outfile.close();
	return 0;
}