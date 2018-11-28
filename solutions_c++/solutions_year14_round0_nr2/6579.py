
#include <iostream>
#include <string>
#include <fstream>

#define MAX_INPUT_SIZE 40

using namespace std;

int main()
{
	char inputValues[MAX_INPUT_SIZE] = {'\0'};
	int numOfTestCases = 0;

	ifstream reader; reader.open("B-large.in");
	ofstream writer; writer.open("result.out");

	reader.getline(inputValues, MAX_INPUT_SIZE, '\n');
	numOfTestCases = atoi(inputValues);

	double threshold = 0.0, rateInr = 0.0, finalVal = 0.0;
	for(int testNo = 1; testNo <= numOfTestCases; testNo++)
	{
		memset(inputValues, MAX_INPUT_SIZE, '\0');
		reader.getline(inputValues, MAX_INPUT_SIZE, ' ');
		threshold = atof(inputValues);
		memset(inputValues, MAX_INPUT_SIZE, '\0');
		reader.getline(inputValues, MAX_INPUT_SIZE, ' ');
		rateInr = atof(inputValues);
		memset(inputValues, MAX_INPUT_SIZE, '\0');
		reader.getline(inputValues, MAX_INPUT_SIZE, '\n');
		finalVal = atof(inputValues);

		
		double t1 = 0.0, t2 = 1.0, curr_rate = 2.0, timeTaken = 0.0;
		while(t2 > t1)
		{
			t1 = finalVal/(curr_rate + rateInr);
			t2 = (finalVal-threshold)/curr_rate;
			if(t1<t2)
			{
				timeTaken += threshold/curr_rate;
				curr_rate += rateInr;
			}
			else
			{
				timeTaken += finalVal/curr_rate;
				break;
			}
		}

		string outString("Case #");
		memset(inputValues, MAX_INPUT_SIZE, '\0');
		itoa(testNo, inputValues,10);
		outString.append(inputValues);
		outString.append(": ");

		memset(inputValues, MAX_INPUT_SIZE, '\0');
		sprintf(inputValues, "%f", timeTaken);
		outString.append(inputValues);
		outString.append("\n");

		writer.write(outString.c_str(), outString.length());
	}

	return 1;
}