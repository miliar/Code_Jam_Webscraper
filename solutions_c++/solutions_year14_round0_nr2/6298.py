#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;
int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("out.out");
	int totalCase;
	
	infile>> totalCase;
	int myCase = 1;

	while(myCase <= totalCase)
	{
		double C, F, X, time;
		time = 0.00;
		infile >> C >> F >> X;
		int n = X/C - 2/F;
		if(n < 0) n = 0;

		for(int i = 1; i <= n; i++)
		{
			time += C / (2 + (i - 1) * F);
		}
		time += X / (2 + n * F);
		printf("Case #%d: %.7f\n",myCase, time);
		//String s = new 
		//outfile << "Case #" << myCase << ": " << time  << endl;
		myCase++;
	}
	infile.close();
	outfile.close();
	return 0;
}
