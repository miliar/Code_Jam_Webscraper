#include <iostream>
#include <string>
#include <math.h>
#include <memory.h> 
#include <fstream>
#include <sstream>
#include <vector>
#include<iomanip> 
#include<algorithm> 
#include <iomanip>
using namespace std; 

struct MyStruct
{
	float num;
	char belongs;
};
//#define   inFile infile
//#define   outFile cout
float a[1000];
float b[1000];
MyStruct c[2000];

int cmp(const MyStruct &a, const MyStruct &b)
{
	return a.num > b.num;
}

int war(int n)
{
	int token = 0;
	int point = 0;
	for (int i = 0; i != 2*n; ++i)
	{
		if (c[i].belongs == 'K')
		{
			token++;
		}
		else
		{
			if (token > 0)
			{
				point++;
				token--;
			}
		}
	}
	return n - point;
}

int dewar(int n)
{
	int token = 0;
	int point = 0;
	for (int i = 0; i != 2*n; ++i)
	{
		if (c[i].belongs == 'N')
		{
			token++;
		}
		else
		{
			if (token > 0)
			{
				point++;
				token--;
			}
		}
	}
	return point;
}

int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("A-small-attempt0.in");
	outfile.open("c-large-1.out");

	int num_cases;
	infile>>num_cases;


	for (int j = 1; j <= num_cases; j++)
	{
		int n;
		infile>>n;
		memset(a, 0.0, 1000);
		memset(b, 0.0, 1000);
		memset(c, 0, 2000);
		for (int i = 0; i != n; ++i)
		{
			infile>>a[i];
		}
		for (int i = 0; i != n; ++i)
		{
			infile>>b[i];
		}
		for (int i = 0; i != n; ++i)
		{
			c[i].num = a[i];
			c[i].belongs = 'N';
			c[i + n].num = b[i];
			c[i + n].belongs = 'K';
		}
		sort(c, c + 2*n, cmp);
		outfile<<"Case #"<<j<<": "<<dewar(n)<<" "<<war(n);

		outfile<<endl;

	}
	return 0;
}

