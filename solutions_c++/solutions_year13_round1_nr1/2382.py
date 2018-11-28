#include <iostream>
#include <fstream>
#include <stdint.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <list>

using namespace std;

const double PI = atan((double)1.0)*4;

uint64_t datasetSize, tmp, n, radius, millilitres;
ifstream inFile;
ofstream outFile;

uint64_t result(uint64_t r, uint64_t t)
{
	n = ceil(((double)1/2-r)/2+sqrt( ((r-(double)1/2)/2)*((r-(double)1/2)/2) + (double)t/2 ));
	while( n*(2*(n+r)-1) > t)
		n--;	
	return n;
}

int main(int argc, char* argv[])
{
	if(argc < 3)
	{
		cout << "No input/output file passed as argument\n";
		return 1;
	}
	cout << PI << "\n";
	
	inFile.open(argv[1]);
	outFile.open(argv[2]);
	inFile >> datasetSize;
	for (uint64_t i = 1; i <= datasetSize; ++i)
	{
		inFile >> radius >> millilitres;
		outFile << "Case #" << i << ": " << result(radius,millilitres) << "\n";
		cout << "Case #" << i << ": " << result(radius,millilitres) << "\n";
	}
	inFile.close();
	outFile.close();
	
	return 0;
}