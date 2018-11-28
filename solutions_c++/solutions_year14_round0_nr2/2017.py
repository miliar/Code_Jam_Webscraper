#include <fstream>
#include <iomanip>
using namespace std;

int cards[5][5];
int firstround[5];
int secondround[5];

int main()
{
	ofstream fout("B-large.out");
	ifstream fin("B-large.in");

	int t, count = 0;
	fin >> t;
	while(count++ < t)
	{
		double C, F, X;
		fin >> C >> F >> X;

		double min = X / 2;
		int k = 1;
		
		while (true)
		{
			double b = X / ((double)2 + (double)k * F);
			for(int i = 0; i < k; i++)
				b += C / ((double)2 + (double)i * F);
			if(b < min)
			{
				min = b;
				k++;
			}
			else
				break;
		}

		fout << "Case #" << count << ": " << setprecision (7)  << min << endl;
	}
	return 0;
}
