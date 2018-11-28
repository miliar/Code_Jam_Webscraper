#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
	int T;
	double C,F,X,prev,next,rate;
	ifstream infile;
	infile.open("B-large.in");
	ofstream outfile;
	outfile.open("out2.txt");
	infile >> T;
	for (int i=0;i<T;i++)
	{
		rate=2;
		infile>>C>>F>>X;
		prev = X/2;
		next = C/2 + X/(2+F);
		while (prev>next)
		{
			prev = next;
			next = next - X/(rate+F) + C/(rate+F) + X/(rate+F+F);
			rate=rate+F;
		}
		outfile<<"Case #"<<i+1<<": "<<fixed<<setprecision(12)<<prev<<endl;

	}

	return 0;
}
