#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ofstream out("A-large.out");
	ifstream in("A-large.in");
	int t;
	in >> t;
	for (int i = 0; i< t;i++)
	{
		int smax;
		in >> smax;
		int a[1005];
		char s[1005];
		in >> s;
		for (int j = 0; j <= smax; j++)
		{
			a[j] = s[j] - '0';
		}
		int min = 0;
		int sum = 0;
		for (int k = 0; k < smax; k++)
		{
			sum += a[k];
			if (k + 1 - sum>min)
				min = k + 1 - sum;
		}
		out << "Case #" << (i + 1) << ": " << min << endl;
		
	}
	return 0;
}