#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	int T;
	ifstream ifs("input.txt");
	ofstream ofs("out.txt");
	ifs >> T;
	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		double a = 2.0;
		double time = 0.0;
		ifs >> C >> F >> X;
		if (a >= X)
		{
			ofs << "Case #" << (i + 1) << fixed << setprecision(7) << ": " << X / a << endl;
		}
		else
		{
			while (X / a > (C / a) + X / (a + F)) {
				time += C / a;
				a += F;
			}
			time += X / a;
			ofs << "Case #" << (i + 1) << fixed << setprecision(7) << ": " << time << endl;
			
		}
	}
}
