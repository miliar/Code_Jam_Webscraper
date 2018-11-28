#include <fstream>
using namespace std;

int main()
{
	ifstream fin ("B-large.in");
	ofstream fout ("b.out");
	int t;
	fin >> t;
	for (int k = 1; k <= t; ++k) {
		int n, m;
		fin >> n >> m;
		int a[n][m], maxrow[n], maxcol[m];
		for (int i = 0; i < n; ++i)
			maxrow[i] = 0;
		for (int j = 0; j < m; ++j)
			maxcol[j] = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				fin >> a[i][j];
				if (maxrow[i] < a[i][j]) maxrow[i] = a[i][j];
				if (maxcol[j] < a[i][j]) maxcol[j] = a[i][j];
			}
		}
		bool possible = true;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (a[i][j] != maxrow[i] && a[i][j] != maxcol[j])
					possible = false;
		fout << "Case #" << k << ": ";
		fout << (possible? "YES" : "NO");
		fout << '\n';
	}
	return 0;
}
