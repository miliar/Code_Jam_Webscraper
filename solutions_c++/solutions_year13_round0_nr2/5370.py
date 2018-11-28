#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char** argv)
{
	int cases;
	int i,j,k,l,c;
	ofstream ofs("result.txt");
	string filename = argv[1];
	ifstream ifs(filename.c_str());
	ifs >> cases;
	int a[100][100];
	int w,h;
	int curvalue = 0;
	int hpossible;
	int vpossible;
	int possible;

	for (c=0;c<cases;c++)
	{
		ifs >> h >> w;
		for (i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				ifs >> a[i][j];
			}
		}

		possible = true;

		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				vpossible = true;
				hpossible = true;
				curvalue = a[i][j];
				for (k=0;k<h;k++)
				{
					if (a[k][j] > curvalue) vpossible = false;
				}
				for (k=0;k<w;k++)
				{
					if (a[i][k] > curvalue) hpossible = false;
				}

				if (!vpossible && !hpossible) {possible = false; break;}
			}
			if (!possible) break;
		}

		ofs << "Case #" << c+1 << ": ";

		if (possible)
		{
			ofs <<"YES";
		}
		else
		{
			ofs << "NO";
		}
		ofs << endl;
	}
	return 0;
}
