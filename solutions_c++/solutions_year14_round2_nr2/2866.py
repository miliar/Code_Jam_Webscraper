#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <cmath>

using namespace std;

const char inputFile[] = "B-small-attempt0.in";
//const char inputFile[] = "A-big.in";
const char outputFile[] = "results.out";


int calculate(int a, int b, int k)
{
	int result = 0;
	
	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < b; j++)
		{
			int _and = i&j;
			//cout << _and << endl;
			if (_and < k)
				result++;
		}
	}
	
	return result;
}

int main()
{
	ifstream input;
	input.open(inputFile);
	
	ofstream output;
	output.open(outputFile);
	
	int N = 0;
	input >> N;
	
	for (int i = 0; i < N; i ++)
	{
		int a = 0;
		int b = 0;
		int k = 0;
		
		input >> a;
		input >> b;
		input >> k;
		
		int result = calculate(a, b, k);
		
		output << "Case #" << i + 1 << ": " << result << endl;

	}

	input.close();
	output.close();
	return 0;
}












