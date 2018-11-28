#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T,row1,row2,x1[4][4],x2[4][4],n=0,x;
	ifstream infile;
	ofstream outfile;
	infile.open("A-small-attempt2.in");
	outfile.open("out.txt");
	infile>>T;
	for (int i=0;i<T;i++)
	{
		n=0;
		infile>>row1;
		for (int j=0;j<4;j++)
			for (int k=0;k<4;k++)
				infile>>x1[j][k];
		infile>>row2;
		for (int j=0;j<4;j++)
			for (int k=0;k<4;k++)
				infile>>x2[j][k];
		for (int j=0;j<4;j++)
		{
			for (int k=0;k<4;k++)
			{
				if (x1[row1-1][j] == x2[row2-1][k])
				{
					x = x1[row1-1][j];
					n++;
				}
			}
		}
		if (n==0)
			outfile<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else if (n==1)
			outfile<<"Case #"<<i+1<<": "<<x<<endl;
		else
			outfile<<"Case #"<<i+1<<": Bad magician!"<<endl;
	}

	return 0;
}