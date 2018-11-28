#include <iostream>
#include<algorithm>
#include<string>
#include<map>
#include<fstream>
using namespace std;

bool arr[10];

int main()
{
	ifstream inf;
	inf.open("A-large.in", std::ifstream::in);
	ofstream outf;
	outf.open("out.txt", std::ofstream::out);
	int t; inf >> t;
	for (int i = 1; i <= t; i++)
	{
		long long x,n; inf >> n; x = n;
		if (n == 0)
			outf << "Case #" << i << ": INSOMNIA" << endl;
		else
		{
			int cnt=0, j=1;
			for (j; cnt < 10;j++)
			{
				x = j*n;
				cnt = 0;
				while (x >= 10)
				{
					arr[x % 10] = true;
					x /= 10;
				}
				arr[x] = true;
				x = j*n;
				for (int k = 0; k < 10; k++)
					if (arr[k] == true)cnt++;
			}
			outf << "Case #" << i << ": " << x << endl;
			for (int k = 0; k < 10; k++)
				arr[k] = false;
		}
	}
	return 0;
}
