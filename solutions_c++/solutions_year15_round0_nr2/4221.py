#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

ifstream ein;
FILE * aus;
int TestCase;

void start()
{
	printf("%d\n", TestCase);
	int result;
	// read test case
	int D;
	ein >> D;
	vector<int> P(D);
	int d;
	for (d=0;d<D;d++)
		ein >> P[d];

	int m;
	int s;
	result = 1000;
	for (m=1;m<=1000;m++)
	{
		s = m;
		for (d=0;d<D;d++)
		{
			s += ((P[d] - 1) / m);
		}
		result = min(result, s);
	}

	// output result
    fprintf(aus, "Case #%d: %d\n", TestCase, result);     // %llu , %ll
}

void main()
{
	int NumTestCases;	
	ein.open("B-large.in");
	aus = fopen("ausgabe.txt","w");
	
	ein >> NumTestCases;
	for (TestCase = 1; TestCase <= NumTestCases; TestCase++)
		start();

	fclose(aus);
	ein.close();
}
