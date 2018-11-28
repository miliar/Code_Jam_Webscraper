#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
	ifstream fin("B-small-attempt2.in", ios::in);
	ofstream fout("B-small-attempt2.out", ios::out);

	fout.precision(7);
	fout.setf(ios::fixed, ios::floatfield);

	int T;

	fin >> T;

	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		double cps = 2;

		fin >> C >> F >> X;

		double fin = X / cps;
		double time = (C / cps);

		while (time + (X / (cps + F)) <= fin)
		{
			fin = time + (X / (cps + F));
			cps += F;
			time += (C / cps);
		}

		time -= (C / cps);
		time += X / cps;

		fout << "Case #" << i + 1 << ": " << time << endl;
	}

	fout.close();
	return 0;
}