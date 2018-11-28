#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T; fin >> T;
	for (int t = 1; t <= T; t++)
	{
		double c, f, x;
		fin >> c >> f >> x;

		int farms = 0;
		double tim = 0.0;
		double rate = 2.0;

		while (true)
		{
			if (x / rate < c / rate + x / (rate + f))
			{
				tim += x / rate;
				break;
			}

			else
			{
				tim += c / rate;
				rate += f;
			}
		}
		printf("Case #%d: ", t);
		printf("%.8f\n", tim);

		// cout << "Case #" << t << ": " << tim << endl;
	}
}