#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <functional>
#include <algorithm>
using namespace std;

typedef long long ll;
#define MOD 1000000007

int main(void)
{
	std::ios_base::sync_with_stdio(false);
	fstream input("B-large.in", fstream::in);
	fstream output("output.txt", fstream::out | fstream::trunc);

	bool possible;
	int t, n, m, i, j, k, l, f[101][101];
	string line;
	stringstream stream;
	map<int, map<int, int> > row, col;

	getline(input, line);
	stream << line;
	stream >> t;

	for(i=1; i<=t; ++i)
	{
		row.clear();
		col.clear();
		getline(input, line);
		stream.clear();
		stream << line;
		stream >> n >> m;

		for(j=1; j<=n; ++j)
		{
			getline(input, line);
			stream.clear();
			stream << line;
			for(k=1; k<=m; ++k)
			{
				stream >> f[j][k];
				++row[j][f[j][k]];
				++col[k][f[j][k]];
			}
		}
		possible = true;

		for(l=1; l<100 && possible; ++l)
		{
			for(j=1; j<=n; ++j)
			{
				if(row[j][l] == m)
				{
					for(k=1; k<=m; ++k)
					{
						if(col[k][l] != n){
							++row[j][l+1];
							++col[k][l+1];
							--col[k][l];
							--row[j][l];
						}

					}
				}
			}

			for(k=1; k<=m; ++k)
			{
				if(col[k][l] == n){
					col[k][l] = 0;
					col[k][l+1] += n;
					for(j=1; j<=n; ++j){
						--row[j][l];
						++row[j][l+1];
					}
				}
			}

			for(j=1; j<=n && possible; ++j)
			{
				if(row[j][l] != 0)
					possible = false;
			}

			for(k=1; k<=m && possible; ++k)
			{
				if(col[k][l] != 0)
					possible = false;
			}
		}

		if(possible)
			output << "Case #" << i << ": YES\n";
		else
			output << "Case #" << i << ": NO\n";

	}

	return 0;
}