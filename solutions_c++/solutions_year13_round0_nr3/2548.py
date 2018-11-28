#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
using namespace std;

unsigned long long reverseNum(unsigned long long num)
{
	unsigned long long rev=0;

	while(num)
	{
		rev = rev*10 + num%10;
		num = num/10;
	}
	return rev;
}

int main()
{
	ofstream myfile;
	myfile.open ("fair2.out");
	int t, c=1;
	vector<unsigned long long> fs;
	for(unsigned long long i=1; i < 10000001; i++)
	{
		if(i == reverseNum(i))
		{
			unsigned long long x = i*i;

			if(x == reverseNum(x))
			{
				fs.push_back(x);
			}
		}

	}

	scanf("%d", &t);
	while(t--)
	{
		unsigned long long a, b, count=0;

		scanf("%llu %llu", &a, &b);

		for(int i=0; i<fs.size(); i++)
		{
			if(fs[i] >= a && fs[i] <= b)
				count++;
			//cout << count << ". " << fs[i] << endl;
		}
		myfile << "Case #"<< c << ": " << count << endl;
		c++;
	}
	return 0;
}
