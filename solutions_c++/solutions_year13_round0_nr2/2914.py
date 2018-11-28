#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	string name("B-large");
	ifstream in;
	ofstream out;
	int nbCases = 0; // size of the sets loaded

	int N, M;
	vector<vector<int> > lawn;
	vector<int> maxN, maxM;

	// Variables end -------------------------------------------------------------------------

	in.open((name + ".in").c_str());
	out.open((name + ".out").c_str()); // flux opening

	if(!(in.is_open() && out.is_open()))
	{
		cerr << "> one of the file could not be loaded" << endl;
	}

	in >> nbCases; // getting case number

	for(int c=1;c<=nbCases;c++)
	{
		bool ok=true;
		in >> N >> M;

		lawn.resize(N);
		maxN.resize(N);
		maxM.resize(M);

		for(int i=0;i<M;i++) // a bit artificial
			maxM[i]=0;

		for(int i=0;i<N;i++)
		{
			lawn[i].resize(M);
			maxN[i]=0;
			for(int j=0;j<M;j++)
			{
				in >> lawn[i][j];
				if(lawn[i][j]>maxN[i])
					maxN[i]=lawn[i][j]; // getting the higher value of the line
				if(lawn[i][j]>maxM[j])
					maxM[j]=lawn[i][j]; // getting the higher value of the column
			}
		}
		// end of data recuperation

		for(int i=0;i<N && ok;i++) // horizontaly
		{
			for(int j=0;j<M && ok;j++)
			{
				ok = (lawn[i][j]==maxN[i] || lawn[i][j]==maxM[j]); // each tile must be accessible (the max of the line or column associated).
				//cout << (ok?"O":"N");
			}
			//cout << endl;
		}

		out << "Case #" << c << ": " << (ok?"YES":"NO") << endl; // starts at 1
	}

    in.close();
    out.close();
    cout << "Appuyez sur ENTER pour continuer" << endl;
    cin.get();
    return 0;
}
