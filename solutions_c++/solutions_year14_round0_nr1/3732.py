#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int check,num;
	int i,j,k;
	int size,r1,r2;
	int x[4][4];
	int y[4][4];
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	fin>>size;
	for(k=0;k<size;k++)
	{
		check=0;
		fin>>r1;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				fin>>x[i][j];
		fin>>r2;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				fin>>y[i][j];

		for (i=0;i<4;i++)
		{
			for (j=0;j<4;j++)
			{
				if (x[r1-1][i]==y[r2-1][j])
				{
					num=x[r1-1][i];
					check++;
				}
			}
		}

		fout<<"Case #"<<k+1<<": ";
		if(check==0)
			fout<<"Volunteer cheated!\n";
		else if(check==1)
			fout<<num<<"\n";
		else if(check>1)
			fout<<"Bad magician!\n";
	}
	fin.close();
	fout.close();
	return 0;
}