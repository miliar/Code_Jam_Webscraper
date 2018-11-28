#include<string>
#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>
using namespace std;

int main(void)
{
	ifstream file;
	file.open("D-small-attempt0.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;

	for (int t = 1; t <= caseNo; t++)
	{
		int k, c, s;
		file >> k >> c >> s;

		output << "Case #" << t << ": ";
		for (int tt = 1; tt <= k; tt++)
			output << tt << " ";
		output << endl;
	}
}