
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char lawn[100][100];
bool b[100][100];
int main(void)
{
	ifstream infile("d:\\in.txt");
	ofstream outfile("d:\\o.out");
	int nDataCount;
	infile >> nDataCount;
	int i,j,k;
	for (i = 0; i < nDataCount; i++)
	{
		int n,m;
		infile >> n >> m;
		for (j = 0; j < n; j++)
		{
			for (k = 0; k < m; k++)
			{
				infile >> lawn[j][k];
				b[j][k] = false;
			}
		}

		char maxh;
		for (j = 0; j < n; j++)
		{
			maxh = 0;
			for (k = 0; k < m; k++)
			{
				if (lawn[j][k] > maxh)
				{
					maxh = lawn[j][k];
				}
			}
			for (k = 0; k < m; k++)
			{
				if (lawn[j][k] >= maxh)
				{
					b[j][k] = true;
				}
			}
		}
		for (k = 0; k < m; k++)
		{
			maxh = 0;
			for (j = 0; j < n; j++)
			{
				if (lawn[j][k] > maxh)
				{
					maxh = lawn[j][k];
				}
			}
			for (j = 0; j < n; j++)
			{
				if (lawn[j][k] >= maxh)
				{
					b[j][k] = true;
				}
			}
		}

		string outp = "YES";
		bool bb = true;
		for (j = 0; j < n; j++)
		{
			for (k = 0; k < m; k++)
			{
				if (b[j][k] == false)
				{
					outp = "NO";
					bb = false;
					break;
				}
			}
			if (bb == false)
			{
				break;
			}
		}
		outfile << "Case #"<<i+1<<": "<<outp<<endl;
	}
	return 0;
}
