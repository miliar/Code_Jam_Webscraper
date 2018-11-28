#include<iostream>
#include <cstdio>
#include <fstream>

using namespace std;

int main()
{
	int T, c=1;
	ofstream myfile;
	myfile.open ("A1.out");
	scanf("%d", &T);
	while(T--)
	{
		long double r, t;
		cin >> r >> t;
		unsigned long long a = 0, count = 0, x=1;
		a += x+2*r;
		while(a <= t)
		{
			x +=4;
			a += x+2*r;
			count++;
		}
		myfile << "Case #"<< c << ": " << count << endl;
		c++;
	}
	return 0;
}
