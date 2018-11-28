#include <iostream>
#include <fstream>

using namespace std;

int main(int argc,char* argv[])
{
	std::ifstream infile(argv[1]);
	int T;
	infile >> T; //no of testcases
	long double C,F,X,F_present,time;
	for (int i=0;i<T;i++)
	{
		//variable intioalization for each testcase
		infile >> C;
		infile >> F;
		infile >> X;
		F_present=2;
		time=0;

		while(((C/F_present)+(X/(F+F_present))) < (X/F_present))
		{
			time += C/F_present;
			F_present=F+F_present;
		}
		time += X/F_present;
		std::cout.precision(7);
		std::cout << std::fixed;

		cout << "Case #" << i+1 << ": " <<time << endl;
		//                printf("%.15f\n", time);
	}
	return 0;
}



