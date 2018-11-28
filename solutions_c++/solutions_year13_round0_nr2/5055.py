#include <iostream>
#include <fstream>

using namespace std;

bool chkPos(int **a, int n, int m, int pi, int pj)
{
	for (int j = 0; j < m; ++j)
	{
		if (a[pi][j] > a[pi][pj]) goto nexttest;
	}
	return true;
nexttest:
	for (int i = 0; i < n; ++i)
	{
		if (a[i][pj] > a[pi][pj]) return false;
	}
	return true;
}

int main()
{
	int t;
	ifstream fi;
	ofstream fo;
	fi.open("F:\\t\\in");
	fo.open("F:\\t\\out", ios::trunc);
	fi >> t;
	for (int q = 1; q <= t; ++q)
	{
		fo << "Case #" << q << ": ";
		int n, m;
		fi >> n >> m;
		int **a = new int*[n];
		for (int i = 0; i < n; ++i)
		{
			a[i] = new int[m];
			for (int j = 0; j < m; ++j) fi >> a[i][j];
		}

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (!chkPos(a, n, m, i, j))
				{
					fo << "NO";
					goto next;
				}
			}
		}
		fo << "YES";
next:
		fo << endl;
	}
	fi.close();
	fo.close();
	return 0;
}