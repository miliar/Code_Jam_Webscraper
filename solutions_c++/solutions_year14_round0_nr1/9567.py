#include <iostream>
#include <fstream>
using namespace std;

struct cases
{
	int firstQ;
	int firstArrang[4][4];
	int secondQ;
	int secondArrang[4][4];
};

void main()
{
	int noOfCases;
	ifstream fin("A-small-attempt0.in");
	fin>>noOfCases;
	cases *c=new cases[noOfCases];
	for(int i=0; i<noOfCases; i++)
	{
		fin>>c[i].firstQ;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++)
				fin>>c[i].firstArrang[j][k];
		}
		
		fin>>c[i].secondQ;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++)
				fin>>c[i].secondArrang[j][k];
		}
	}
	fin.close();

	ofstream fout("output.txt");
	int check=0;
	int num;
	for(int i=0; i<noOfCases; i++)
	{
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++)
			{
				if(c[i].firstArrang[c[i].firstQ-1][j]==c[i].secondArrang[c[i].secondQ-1][k])
				{
					num=c[i].firstArrang[c[i].firstQ-1][j];
					check++;
				}
			}
		}

		if(check==0)
			fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else if(check>1)
			fout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		else if(check==1)
			fout<<"Case #"<<i+1<<": "<<num<<endl;

		check=0;
	}

	fout.close();
}
