#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <cmath>

using namespace std;

#define PI 3.1415927

int main()
{
	ifstream inData;
	ofstream outData;
	inData.open("A-small-attempt0.in.txt");
	outData.open("output.txt");
	
	long double T, r, t;
	int k;
	inData >> T;
	for (int i = 0; i < T; i++)
	{
		k = 0;
		inData >> r >> t;
		k = floor(0.25*(1-2*r+sqrt(pow((2*r-1), 2)+8*t)));
		
		
		outData << "Case #" << i + 1 << ": " << k << endl;
	}
	
	inData.close();
	outData.close();
}



