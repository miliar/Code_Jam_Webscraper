#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("B.txt");
	ofstream out("B_ans.txt");

	int testnum;
	in >> testnum;
	for (int t = 0; t < testnum; t++)
	{
		long double C, F, X, res = 0;
		long double now = 2;
		in >> C >> F >> X;

		long double res1 = 0;
		bool q = true;
		while (q)
		{
			res1 = res + X/now;
			res += C/now;
			now += F;
				
			if (res1 < res + X/now)
			{
				q = false;
				res = res1;
			}
		}
		
		out << "Case #" << t+1 << ": ";
		out << fixed << setprecision(7);
		out << res << endl;
	}
	return 0;
}


