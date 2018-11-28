#include <iostream>
using namespace std;


static const char* testInCase = 
    "C:\\CodeJam\\Cookie\\Data\\B-large.in";
static const char* testOutCase = 
    "C:\\CodeJam\\Cookie\\Data\\B-large.out";

static const char* multipleCardsOutput = 
    "Bad magician!";
static const char* noCardsOutput = 
    "Volunteer cheated!";

double cookie(double C, double F, double X)
{
	double currentValue[4];
	double nextValue[4];

	nextValue[0] = 0;
	nextValue[1] = 2;
	nextValue[2] = X / nextValue[1];
	nextValue[3] = C / nextValue[1];


	do
	{
		for(int i=0; i<4; i++)
			currentValue[i] = nextValue[i];

		nextValue[0] = currentValue[0] + currentValue[3];
		nextValue[1] += F;
		nextValue[2] = nextValue[0] + X / nextValue[1];
		nextValue[3] = C / nextValue[1];
		
	} while (nextValue[2] < currentValue[2] );

	return currentValue[2];
}

int main(int argc, char* argv[])
{
	string inputFile(testInCase);
	string outputFile(testOutCase);

	freopen(inputFile.c_str(), "r", stdin);
	freopen(outputFile.c_str(), "w", stdout);

	int T;
	cin >> T;

	double C, F, X;
	for (int i = 0; i<T; i++)
	{
		char outputStr[15];
		cin >> C >> F >> X;
		sprintf(outputStr, "%.8g", cookie(C, F, X) );
		cout << "Case #" << i+1 << ": " << outputStr << endl;
	}


	return 0;
}
