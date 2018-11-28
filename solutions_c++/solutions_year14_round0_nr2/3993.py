#include <fstream>
#include <iomanip>
using namespace std;


int main()
{
	ifstream in("B-large (1).in");
	ofstream out("B.out");
	int t;
	in >> t;
	double x, c, f;
	
	for (int II = 1; II <= t; II++)
	{
		in >> c >> f >> x;
		double temp = 0;
		double hh = 0;
		double gg = 0;
		double aa = 0;
		double tt = 0;
		double z = 2;
		int k = 0;
		while (1)
		{
			tt = c / z;
			gg = x / z;
			if (gg <= tt)
			{
				temp += gg;
				break;
			}
			else if (gg <= (tt + x / (z + f)))
			{
				temp += gg;
				break;
			}
			else
			{
				temp += tt;
				z += f;
			}
		}
		out << "Case #" << II << ": ";
		out << fixed << setprecision(10) << temp;
		out << "\n";
	}
	out.close();
	in.close();
	return 0;
}