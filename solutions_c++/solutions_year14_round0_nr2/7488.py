#include <fstream>

using namespace std;

ifstream in("B-large.in");
ofstream out("output.txt");

int main()
{
	int t;
	in >> t;
	for (int tt = 0; tt < t; tt++)
	{
		long double c, f, x, tim = 0, currV = 2;
		in >> c >> f >> x;
		bool ans = false;
		while (!ans)
		{
			if (x / currV < (c / currV) + (x / (currV + f)))
			{
				ans = true;
				tim += x / currV;
			}
			else
			{
				tim += c / currV;
				currV += f;
			}
		}
		out.precision(10);
		out << "Case #" << tt + 1 << ": " << tim << endl;
	}
	in.close();
	out.close();
	return 0;
}