#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
	int i;
	int testcase;
	double total,C,F,X,W;
	ifstream infile("B-large.in");
	ofstream outfile("outfile.out");
	while(infile && outfile)
	{
		infile >> testcase;
		for(i = 0; i < testcase; i++)
		{
			total = 0;
			W = 2;
			infile >> C >> F >> X;
			while((X/W) > ((C/W)+(X/(W+F))))
			{
				total += C/W;
				W += F;
			}
			total += X/W;
			outfile << "Case #" << i+1 << ": " << fixed << setprecision(7) << total << endl;
		}
		infile.close();
		outfile.close();
	}
	return 0;
}