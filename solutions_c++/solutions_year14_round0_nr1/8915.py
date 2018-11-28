#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	int i, n,m,ar1[4][4],ar2[4][4],k,l,cont=0,num,ii=0;

	ifstream inf("A-small-attempt1.in");
	ofstream outf("out.txt");
	inf >> i;

	while (ii<i)
	{
		cont = 0;
		inf >> m;

		for (k = 0; k < 4; k++)
		{
			for (l = 0; l < 4; l++)
			{
				inf >> ar1[k][l];
			}
		}


		inf >> n;

		for (k = 0; k < 4; k++)
		{
			for (l = 0; l < 4; l++)
			{
				inf >> ar2[k][l];
			}
		}
		


		for (k = 0; k < 4; k++)
		{
			for (l = 0; l < 4; l++)
			{
				if (ar1[m-1][k] == ar2[n-1][l])
				{
					cont++;
					num=ar1[m-1][k];
				}
			}
		}


		if (cont == 1)
			outf << "Case #" << ii + 1 << ": " << num << endl;
		else if (cont > 1)
			outf << "Case #" <<ii+1 << ": Bad magician!\n";
		else if (cont == 0)
			outf << "Case #" << ii+1 <<": Volunteer cheated!\n";
		

		ii++;
	}

	
	inf.close();
	outf.close();

	return 0;
}