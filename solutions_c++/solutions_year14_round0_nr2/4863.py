#include <fstream>

using namespace std;

int main()
{
	int T = 0;
	double C = 0.0, X = 0.0, F = 0.0;
	double current = 0.0;
	double min = 0.0;
	ifstream fi("B-small-attempt0.in");
	ofstream fo("Output.txt");
	fi>>T;
	for (int t = 1; t <= T; ++t)
	{
		fi>>C>>F>>X;
		min = X / 2.0;
		int n = 1;
		current = C / 2.0;
		while (min - (current + X / (2.0 + n * F)) > 1e-7)
		{
			min = current + X / (2.0 + n * F);
			++n;
			current += C / (2 + (n - 1) * F);
		}
		fo.precision(10);
		fo<<"Case #"<<t<<": "<<min<<endl;
	}
	fi.close();
	fo.close();
	return 0;
}