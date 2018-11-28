
#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <stdexcept>
#include <fstream>
#include <map>
#include <limits>
#include <math.h>
#include <iomanip>
#include <iomanip>
#include <algorithm>

typedef __int64 int64_t;

using namespace std;

bool Solve(const vector<vector<int>>& values, int n, int m)
{
	vector<vector<int>> heights(n, vector<int>(m, 100));

	for (int i = 0; i < n; ++i)
	{
		int max = 0;

		for (int j = 0; j < m; ++j)
		{
			int h = values[i][j];
			if (h > max )
				max = h;
		}
		for (int j = 0; j < m; ++j)
			heights[i][j] = min(heights[i][j], max);
	}


	for (int i = 0; i < m; ++i)
	{
		int max = 0;

		for (int j = 0; j < n; ++j)
		{
			int h = values[j][i];
			if (h > max )
				max = h;
		}
		for (int j = 0; j < n; ++j)
			heights[j][i] = min(heights[j][i], max);
	}

	return values == heights;
}

int main(int argc, char** argv)
{
	const string inputFilename = "B-large.in";
	const string outputFilename = inputFilename + ".out";
	ifstream ifs( inputFilename.c_str() );
	ofstream file( outputFilename.c_str());
	int nbTest = 0;

	ifs >> nbTest;
	string line;
	getline(ifs, line);

	for( int test = 1; test <= nbTest; ++test )
	{
		ostringstream ostr;
		int64_t n, m;

		ifs >> n >> m;
		vector<vector<int>> values;

		for (int i = 0; i < n; ++i)
		{
			values.push_back(vector<int>());
			for (int i = 0; i < m; ++i)
			{
				int h = 0;
				ifs >> h;
				values.back().push_back(h);
			}
			getline(ifs, line);
		}			
		
		ostr << "Case #" << test << ": ";
		ostr << (Solve(values, n, m) ? "YES" : "NO");
		ostr << endl;

		cout << ostr.str();
		file << ostr.str();
	}

	cout << "Finish" << endl;
	return 0;
}



