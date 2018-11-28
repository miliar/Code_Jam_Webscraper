#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <boost/regex.hpp>

using namespace std;

typedef vector<string>::iterator vst;
typedef vector<int>::iterator vit;

int main(int argc, char** argv)
{
	if(argc<2)
		exit(0);

	//file input
	ifstream in;
	in.open(argv[1]);

	vector< vector<int> > v;


	int N = 0;
	in >> N;
	for(int _i=0; _i<N; _i++)
	{
		v.clear();
		cout << "Case #" << _i+1 << ": ";

		int n,m;
		in >> n >> m;
		vector<int> maxInRow(n), maxInCol(m);
		for(int i=0; i<n; i++)
		{
			vector<int> w;
			for(int j=0; j<m; j++)
			{
				int x;
				in >> x;

				maxInRow[i] = max( maxInRow[i], x );
				maxInCol[j] = max( maxInCol[j], x );

				w.push_back(x);
			}

			v.push_back(w);
		}

		if(n == 1 && m == 1)
		{
			cout << "YES" << endl;
			continue;
		}


		bool bC = false;
		//cout << "n: " << n << "\tm: " << m << endl;
		for(int i = 0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				int x = v[i][j];
				//cout << x << " " << i << " " << j << " " << maxInRow[i] << " " << maxInCol[j] << endl;
				if( x < maxInRow[i] && x < maxInCol[j] )
				{
					cout << "NO" << endl;
					bC = true;
					break;
				}
			}
			if(bC)
				break;
		}
		if(bC)
			continue;

		cout << "YES" << endl;
	}

	//cout << "Hello!" << endl;
	in.close();
	return 0;
}

