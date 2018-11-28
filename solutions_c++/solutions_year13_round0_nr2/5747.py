#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define forn(i, n) for (int i = 0; i < n; i++)


int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");

	int tst, gt = 0, n, m, arr[101][101];
	string s;

	in >> tst;

	while (gt < tst)
	{
		in >> n >> m;
		forn(i, n)
			forn(j, m)
				in >> arr[i][j];

		forn(i, n)
			forn(j, m)
		{
			int i1 = i, j1 = j; bool l, r, u, d;
			l = r = u = d = 0;

			while (i1 < n && arr[i1][j] <= arr[i][j])
				i1++;
			if (i1 < n && arr[i1][j] > arr[i][j])
				d = 1;

			i1 = i;
			while (i1 >= 0 && arr[i1][j] <= arr[i][j])
				i1--;
			if (i1 >= 0 && arr[i1][j] > arr[i][j])
				u = 1;

			while (j1 < m && arr[i][j1] <= arr[i][j])
				j1++;
			if (j1 < m && arr[i][j1] > arr[i][j])
				r = 1;

			j1 = j;
			while (j1 >= 0 && arr[i][j1] <= arr[i][j])
				j1--;
			if (j1 >= 0 && arr[i][j1] > arr[i][j])
				l = 1;

			if ((l && u) || (l && d) || (r && u) || (r && d))
			{
				out << "Case #" << gt + 1 << ": NO" << endl;
				goto q;
			}
		}
		out << "Case #" << gt + 1 << ": YES" << endl;
q:		
		gt++;
	}
		

	return 0;
}