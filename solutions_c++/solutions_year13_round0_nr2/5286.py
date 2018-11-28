#include <iostream>
#include <fstream>

using namespace std;


bool vcheck (int dat[100][100], int vlen, int hidx, int height)
{
	int i;
	for (i = 0; i < vlen; ++i)
	{
		if (dat[i][hidx] > height)
		{
			//cout << "vcheck false " << i << " " << hidx << " " << height << endl;
			return false;
		}
	}
	return true;
}

bool hcheck (int dat[100][100], int hlen, int vidx, int height)
{
	int j;
	for (j = 0; j < hlen; ++j)
	{
		if (dat[vidx][j] > height)
		{
			//cout << "hcheck false " << vidx << " " << j << " " << height << endl;
			return false;
		}
	}
	return true;
}

void acase (ofstream *fout, int dat[100][100], int m, int n, int Cn)
{
	int i, j;
	for (i = 0; i < n; ++i)
	{
		for (j = 0; j < m; ++j)
		{
			if (!vcheck(dat, n, j, dat[i][j]) && !hcheck(dat, m, i, dat[i][j]))
			{
				//cout << "no at " << i << " " << j << endl;
				*fout << "Case #" << Cn << ": NO" << endl;
				return;
			}
		}
	}
	if ((i == n) && (j == m))
	{
		*fout << "Case #" << Cn << ": YES" << endl;
	}
	return;
}

void pdat (int dat[100][100], int n, int m)
{
	for (int v = 0; v < n; ++v)
	{
		for (int h = 0; h < m; ++h)
		{
			cout << dat[v][h] << " ";
		}
		cout << endl;
	}
}

int main ()
{
	int tn;
	int dat[100][100];
	int m, n;
	ifstream fin("testcase.txt");
	ofstream fout("result.txt");

	fin >> tn;
	for (int i = 0; i < tn; ++i)
	{
		fin >> n;
		fin >> m;
		for (int v = 0; v < n; ++v)
		{
			for (int h = 0; h < m; ++h)
			{
				fin >> dat[v][h];
			}
		}
		//pdat (dat, n, m);
		acase (&fout, dat, m, n, i+1);
	}

	fin.close();
	fout.close();
	getchar ();
	return 0;
}
