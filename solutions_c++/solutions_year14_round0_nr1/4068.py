#include <iostream>
#include <string>
#include <fstream>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;

int main()
{
	cout<<"Please input file name: ";
	string infilename;
	cin >> infilename;
	ifstream infile(infilename.c_str());
	if(!infile)
	{
		cout<<"error: unable to open input file"<<endl;
		return -1;
	}
	ofstream outfile("out.txt");
	int T;
	int count;
	int result;
	infile>>T;
	count=0;
	for(int i=1;i<=T;i++)
	{
		count=0;
		int rn1;
		int temp;
		infile>>rn1;
		int grid1[4];
		for(int j=1;j<5;j++)
		{
			if(j!=rn1)
				infile>>temp>>temp>>temp>>temp;
			else
				infile>>grid1[0]>>grid1[1]>>grid1[2]>>grid1[3];

		}

		int rn2;
		infile>>rn2;
		int grid2[4];
		for(int j=1;j<5;j++)
		{
			if(j!=rn2)
				infile>>temp>>temp>>temp>>temp;
			else
				infile>>grid2[0]>>grid2[1]>>grid2[2]>>grid2[3];

		}
		
		for(int k=0; k<4; k++)
		{
			for(int h=0; h<4; h++)
			{
				if(grid1[k]==grid2[h])
				{
					count++;
					result=grid1[k];
				}

			}
		}

		if(count==0)
		{
			outfile<<"Case #"<<i<<": Volunteer cheated!"<<'\xA';
		}
		else if(count==1)
		{
			outfile<<"Case #"<<i<<": "<<result<<'\xA';
		}
		else
		{
			outfile<<"Case #"<<i<<": Bad magician!"<<'\xA';
		}

	}

	infile.close();
	outfile.close();

	return 0;
}