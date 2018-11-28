#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;


double f0(double c, double f, double x)
{
	return x / 2.0;
}

double f1(double c, double f, double x)
{
	return c / 2.0 + x / (2.0 + f);
}


int getn(double c, double f, double x)
{
		int n = int((x*f - 2.0 * c - c*f) / (c * f));
		if (n < 0)
		{
			n = 0;
		}
		return n;
}

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");


	int T = 0;
	in >> T;
	for (int i = 1; i <= T; i++)
	{
		double c = 0, f = 0, x = 0;
		in >> c >> f >> x;
		double sum = 0.0;
		int n = getn(c, f, x);
		for (int j = 0; j <= n; j++)
		{
			sum += (c / (2.0 + j*f));
		}
		sum += (x / (2 + (n + 1)*f));
		if (sum > (x / 2.0))
		{
			sum = x/2.0;
		}
		out << "Case #" << i << ": " << setprecision(10) << sum << endl;
		//cout << setprecision(10)<<sum << endl;
	}


	in.close();
	out.close();

	return 0;
}