#include <fstream>
#include <algorithm>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

int main()
{
	int t, n, m;
	int a[105][105];
	int rows[105];
	int cols[105];
	int i, j, k;

	cin >> t;
	
	for(k = 1 ; k <= t; k++)
	{
		cin >> n >> m;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				cin >> a[i][j];

		for(i=0;i<n;i++)
		{
			rows[i] = a[i][0];
			for(j=1;j<m;j++)
				if(a[i][j] > rows[i])
					rows[i] = a[i][j];
		}

		for(i=0;i<m;i++)
		{
			cols[i] = a[0][i];
			for(j=1;j<n;j++)
				if(a[j][i] > cols[i])
					cols[i] = a[j][i];
		}

		bool is_max = true;

		for(i=0;i<n && is_max;i++)
			for(j=0;j<m;j++)
				if(a[i][j] != rows[i] && a[i][j] != cols[j])
				{
					is_max = false;
					break;
				}

		if(is_max)
			cout << "Case #" << k <<": YES" << endl;
		else
			cout << "Case #" << k <<": NO" << endl;
	}
	return 0;
}