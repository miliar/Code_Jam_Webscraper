#include <iostream>
#include <fstream>
#include <string>
#pragma warning(disable:4996)
using namespace std;
int People[1010];
int MAXTIME;
int answer[100];
int ans(int num)
{
	int r = 1000000000;
	for (int i = 1; i <= MAXTIME; ++i)
	{
		int fendeshijian = 0;
		for (int k = 0; k < num; ++k)
		{
			if (People[k]>i)
			{
				fendeshijian += People[k] / i;
				if (People[k] % i == 0)
				{
					fendeshijian--;
				}
			}
		}
		int zongshijian = fendeshijian + i;
		if (zongshijian < r)
			r = zongshijian;
	}
	return r;
}
int main()
{
	int n;
	ifstream f1;
	f1.open("C:\\Users\\ty\\Desktop\\codejam2015\\A.in");
	f1 >> n;
	for (int i = 0; i < n; ++i)
	{
		int num;
		f1 >> num;
		for (int k = 0; k < num; ++k)
		{
			f1 >> People[k];
			if (People[k]>MAXTIME)
				MAXTIME = People[k];
		}
		answer[i] = ans(num);
	}
	ofstream f;
	f.open("C:\\Users\\ty\\Desktop\\codejam2015\\B.txt");
	for (int i = 0; i < n; ++i)
	{
		f << "case #" << i + 1 << ": " << answer[i] << endl;
	}
	f.close();
	return 0;
}