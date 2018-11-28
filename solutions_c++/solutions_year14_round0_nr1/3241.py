#include<fstream>
using namespace std;
int main()
{
	int i,j,k,rowa,rowb;
	int testcase;
	int a[4][4];
	int b[4][4];
	int c[4];
	int flag;
	ifstream infile("A-small-attempt2.in");
	ofstream outfile("outfile.out");
	if(infile && outfile)
	{
		infile >> testcase;
		for(i = 0; i < testcase; i++)
		{
			flag = 0;
			infile >> rowa;
			for(j = 0; j < 4; j++)
				for(k = 0; k < 4; k++)
					infile >> a[j][k];
			infile >> rowb;
			for(j = 0; j < 4; j++)
				for(k =0; k < 4; k++)
					infile >> b[j][k];
			for(j = 0; j < 4; j++)
				for(k = 0; k < 4; k++)
				{
					if(a[rowa-1][j] == b[rowb-1][k])
						c[flag++] = a[rowa-1][j];
				}
			if(flag > 1)
			{
				outfile << "Case #" << i+1 << ": "  << "Bad magician!\n";
			}
			if(flag == 0)
			{
				outfile << "Case #" << i+1 << ": "  << "Volunteer cheated!\n";
			}
			if(flag == 1)
			{
				outfile << "Case #" << i+1 << ": "  << c[flag-1] << endl;
			}
		}
		infile.close();
		outfile.close();
	}
	return 0;
}