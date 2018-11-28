#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("output.txt");

	long T;
	in >> T;


	for (long caseN = 0; caseN < T; caseN++)
	{
		long long r, t;
		in >> r >> t;

		long long dec = (r + 1) * (r + 1) - r * r;
		long long count = 0;

		while (t - dec >= 0)
		{
			t -= dec;
			r += 2;
			count++;
			dec = (r + 1) * (r + 1) - r * r;
		}

		out << "Case #" << caseN + 1 << ": " << count << endl;
	}

	return 0;
}