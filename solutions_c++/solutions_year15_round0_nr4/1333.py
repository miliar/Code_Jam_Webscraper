#include <iostream>
#include <fstream>
#include <string>
#pragma warning(disable:4996)
using namespace std;
int answer[100];
int main()
{
	int n;
	ifstream f1;
	f1.open("C:\\Users\\ty\\Desktop\\codejam2015\\A.in");
	f1 >> n;
	for (int i = 0; i < n; ++i)
	{
		int x, r, c;
		f1 >> x >> r >> c;
		if (r*c%x == 0 && r > x - 2 && c > x - 2)
		{
			answer[i] = 1;
		}
		else
			answer[i] = 0;
	}
	ofstream f;
	f.open("C:\\Users\\ty\\Desktop\\codejam2015\\B.txt");
	for (int i = 0; i < n; ++i)
	{
		if (answer[i] == 1)
		{
			f << "case #" << i + 1 << ": GABRIEL" << endl;
		}
		else if (answer[i] == 0)
		{
			f << "case #" << i + 1 << ": RICHARD" << endl;
		}
	}
	f.close();
	return 0;
}