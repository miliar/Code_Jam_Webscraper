
#include <math.h>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

double solve(double c, double f, double x)
{
	double n = ceil(x/c - (2+f)/f);
	
	if(n < 0)
		n = 0.f;

	double res = 0;
	for(int i = 0; i < n; ++i)
	{
		res += c/(2+i*f);
	}
	res += x/(2+n*f);
	return res;
}

struct InputData 
{
	double c, f, x;
};

int main()
{
	ifstream inFile ("input.txt");

	if (!inFile.is_open())
		return 1;

	int numCases;
	inFile>>numCases;

	vector<InputData> inputDataVec;
	inputDataVec.resize(numCases);

	for (int i = 0; i < numCases; ++i)
	{
		InputData& id = inputDataVec[i];
		inFile >> id.c >> id.f >> id.x;
	}

	ofstream outFile;
	outFile.open("output.txt");

	outFile.setf( std::ios::fixed, std:: ios::floatfield );
	outFile.precision(7);

	for (int i = 0; i < numCases; ++i)
	{
		const InputData& id = inputDataVec[i];
		double res = solve(id.c, id.f, id.x);
		outFile << "Case #" << i+1 << ": " << res << endl;
	}

	outFile.close();

	return 0;
}