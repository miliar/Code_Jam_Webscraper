#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

double p[1001][1001];

int main()
{
	ifstream inf("B-small-attempt0.in");
	//ofstream outf("1.txt");
	//ifstream inf("data.txt");
	ofstream outf("test.txt"); //outf2("data.txt");
	int T;
	//inf >> T;
	int t;
	int i, j;
	inf >> T;
	for (t = 1;t <= T;t++)
	{
		int a, b, k;
		inf >> a >> b >> k;
		int cnt = 0;
		for (i = 0;i < a;i++)
		{
			for (j = 0;j < b;j++)
			{
				if ((i & j) < k)
					cnt++;
			}
		}
		

		outf << "Case #" << t << ": " << cnt;
		outf << endl;
	}
	return 0;
}
