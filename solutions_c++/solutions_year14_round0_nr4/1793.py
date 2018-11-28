#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main()
{
	ifstream inf("D-large.in");
	ofstream outf("14q4.txt");
	//ifstream inf("test.in");
	//ofstream outf("test.txt");
	int T;
	inf >> T;
	int k;
	for (k = 1;k <= T;k++)
	{
		int n;
		inf >> n;
		double a[1001], b[1001];
		int i, j;
		for (i = 0;i < n;i++)
			inf >> a[i];
		for (i = 0;i < n;i++)
			inf >> b[i];
		sort(a, a + n);
		sort(b, b + n);
		bool used[1001] = {0};
		int cnt = 0;
		for (i = n-1;i >= 0;i--)
		{
			bool flag = false;
			for (j = 0;j < n;j++)
			{
				if (!used[j] && a[i] < b[j])
				{
					flag = true;
					used[j] = true;
					break;
				}
			}
			if (!flag)
			{
				for (j = 0;j < n;j++)
				{
					if (!used[j])
					{
						used[j] = true;
						break;
					}
				}
				cnt++;
			}
		}

		int sum = 0;
		bool u[1001] = {0};
		for (i = 0;i < n;i++)
		{
			for (j = 0;j < n;j++)
			{
				if (!u[j] && a[i] > b[j])
				{
					sum++;
					u[j] = true;
					break;
				}
			}
		}
		outf << "Case #" << k << ": ";
		outf << sum << " " << cnt;
		outf << endl;
	}
	return 0;
}
