#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
#include<cmath>
#include<fstream>
#include<string>
#include<sstream>
#include<cstdlib>
using namespace std;

long long numCycle(long long r, long long t)
{
	// not ready for really large number
	long double temp = (2*r-1.0)*(2*r-1.0)+8*t;
	long double resultTemp = (-2*r+1 + sqrt(temp))/4;
	return (long long)floor(resultTemp);
}

int main(int argv, char*argc)
{
	ifstream infile("test.txt");
	ofstream outfile("result.txt");
	if (!infile || !outfile)
	{
		cout << "wrong" << endl;
		return -1;
	}

	int numCase;
	infile >> numCase;
		
	for (int i = 0; i < numCase; i++)
	{
		long long r,t;
		infile >> r >> t;
		outfile << "Case #" << i+1 << ": " << numCycle(r,t) << endl;
	}
	infile.close();
	outfile.close();
}