#include <fstream>
#include <math.h>
using namespace std;

int main ()
{
	fstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");

	int T;
	in >> T;

	for (int c = 1; c <= T; c++)
	{
		int r, t;
		in >> r;
		in >> t;

		int rings = 0;

		int imagined = r;

		while (t > 0)
		{
			r = imagined+1;

			int area = r*r - imagined*imagined;

			if (area <= t)
			{
				t -= area;
				++rings;
			}
			else
				break;

			imagined +=2;
		}

		out << "Case #" << c << ": " << rings;

		if (c != T)
			out << endl;
	}
}