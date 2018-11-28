// fstream::open
#include <fstream>
#include <string>

using namespace std;

int main()
{

	fstream filestrIn, filestrOut;
	int cases;
	filestrIn.open("in.txt", fstream::in);
	filestrOut.open("out.txt", fstream::out);

	int currentCases = 1;
	filestrIn >> cases;
	// >> i/o operations here <<
	int data[101][101];
	while (currentCases <= cases) {
		int n,m;
		filestrIn >> n >> m;
		for(int j = 0; j < n; j++)
			for(int i = 0; i < m; i++)
				filestrIn >> data[i][j];

		for(int i = 0; i < m; i++)
			for(int j = 0; j < n; j++)
			{
				int maxthan1 = true;
				for(int i2 = 0; i2 < m; i2++)
					if(data[i2][j] > data[i][j])
					{
						maxthan1 = false;
						break;
					}

				int maxthan2 = true;
				for(int j2 = 0; j2 < n; j2++)
					if(data[i][j2] > data[i][j])
					{
						maxthan2 = false;
						break;
					}

				if(maxthan2 == false && maxthan1 == false)
				{

					filestrOut << "Case #" << currentCases <<": NO\n";
					goto OUT;
				}

			}

		filestrOut << "Case #" << currentCases <<": YES\n";
		OUT:

		currentCases++;
	}
	filestrIn.close();
	filestrOut.close();

	return 0;
}