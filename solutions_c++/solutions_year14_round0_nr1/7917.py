#include <iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fout.open("Magic_Answer.in");
	fin.open("A-small-attempt0.in");
	int test,flag,i,j,k;
	int line1,line2,no;
	int sq1[4][4],sq2[4][4];
	fin>>test;
	for(i=0;i<test;i++)
	{
		flag=0;
		fin>>line1;
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				fin>>sq1[j][k];
		fin>>line2;
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				fin>>sq2[j][k];
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(sq1[line1-1][j]==sq2[line2-1][k])
				{
					no = sq1[line1-1][j];
					flag++;
					break;
				}
			}
		}
		if(flag==1)
			fout<<"Case #"<<i+1<<": "<<no<<"\n";
		else if(flag>1)
			fout<<"Case #"<<i+1<<": Bad magician!"<<"\n";
		else if(flag==0)
			fout<<"Case #"<<i+1<<": Volunteer cheated!"<<"\n";
	}
	fin.close();
	fout.close();
	return 0;
}
