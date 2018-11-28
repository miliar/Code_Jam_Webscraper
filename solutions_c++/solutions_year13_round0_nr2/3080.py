#include <iostream>
#include <fstream>
using namespace std;

int main()
{
ifstream fin("2013_lawn.txt");
ofstream fout("2013_lawn_out.txt");
int noCase;
fin >> noCase;
for (int i = 1; i <= noCase; i++)
	{
	int m,n;
	fin >> m >> n;
	int lawn[m][n];
	for (int j = 0; j < m; j++)
		for (int k = 0; k < n; k++)
			fin >> lawn[j][k];
	
	bool cannot = false;
	for (int j = 0; j < m; j++)
		{
		for (int k = 0; k < n; k++)
			{
			bool sidepass = true;
			//for each sq;
			//check leftright
			for (int a = 0; a < n; a++)
				if (lawn[j][k] < lawn[j][a])
					{
					sidepass = false;
					break;
					}
			if (!sidepass)
				{
				for (int a = 0; a < m; a++)
					if (lawn[j][k] < lawn[a][k])
					{
					fout << "Case #" << i << ": NO" << endl;
					j = m;
					k = n;
					cannot = true;	
					break;			
					}
				}
			}
		}
	
	if (!cannot)
		fout << "Case #" << i << ": YES" << endl;
	}
}
