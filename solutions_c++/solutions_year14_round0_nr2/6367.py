#include <iostream>
#include <fstream>
#include <limits>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	double C;
	double F;
	double X;
	ifstream input(argv[1]);
	ofstream output(argv[2]);
	output.setf(ios::fixed);
	output.precision(7);
	input >> T;
	for (int i = 1; i <= T; i++)
	{
		input >> C;
		input >> F;
		input >> X;
		double previousResult;
		double currentResult;
		double finalResult;
		int iteration = 1;
		previousResult = X / 2;
		while (true)
		{		
			currentResult = previousResult - X/(2+(iteration-1)*F)+C/(2+(iteration-1)*F)+X/(2+iteration*F);
			if (currentResult <= previousResult)
			{
				iteration++;
				previousResult = currentResult;
				continue;
			}
			else
			{
				finalResult = previousResult;
				break;
			}
		}
		output << "Case #" << i << ": " << finalResult << endl;
	}
	input.close();
	output.flush();
	output.close();
	return 0;
}