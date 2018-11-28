#include<string>
#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

int main(void)
{
	ifstream file;
	file.open("1A-small-attempt0.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;

	for(int n=1; n<= caseNo; n++)
	{
		long long int r, t;
		file >> r >> t;

		long long int result = 0;

		while(t>0){
			t -= 2*r+1;
			r += 2;
			if(t>=0) result += 1;
		}

		output << "Case #" << n << ": ";
		output <<  result << endl;

	}
}