#include <string>
#include <iostream>
#include <fstream>
using namespace std;
void main () 
{
	ifstream infile ("infile.txt");
	ofstream outfile ("result.txt");
	int cases;
	int c,good,flag;
	int m,n,i,j,k;
	int map[100][100];

	infile >> cases;
	for (c=1; c<cases+1; c++)
	{
		flag = 1;
		infile >> m >> n;
		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
				infile >> map[i][j];

		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
			{
				good = 1;
				for (k=0;k<m;k++)
				{
					if (map[k][j]>map[i][j])
						good = 0;
				}
				if (!good)
				{
					good = 1;
					for (k=0;k<n;k++)
					{
						if (map[i][k] > map[i][j])
							good = 0;
					}
				}
				if (!good)
					flag = 0;
			}

			if (flag)
				outfile << "Case #" << c << ": YES" << endl;
			else
				outfile << "Case #" << c << ": NO" << endl;
	}



	infile.close();
	outfile.close();

}