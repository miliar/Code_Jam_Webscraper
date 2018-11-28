#include <iostream>
#include <fstream>
# include <iomanip>

using namespace std;


int main()
{
	int i = 0, n, ii = 0;
	long double cont = 0, c, f, x, num = 0, num1 = 0, num2 = 0;


	ifstream inf("B-large.in");
	ofstream outf("out_B.txt");
	inf >> n;

	while (ii < n)
	{
		num = 0.0;
		num1 = 0.0;
		cont = 2;
		inf >> c >> f >> x;

		num1 = x / cont;
		num = c / cont;

		while (true)
		{

			cont += f;
			num += x / cont;

			if (num > num1)
			{
				break;
			}
			else
			{
				num1 = num;
				num -= x / cont;
				num += c / cont;

			}
		}

		outf << "Case #" << ii + 1 << ": " << fixed << setprecision(7) << num1 << endl;


		ii++;
	}


	inf.close();
	outf.close();

	return 0;
}