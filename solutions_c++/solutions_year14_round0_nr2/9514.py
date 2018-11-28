#include <cmath>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

const char CDfv[] = "B-small-attempt0.in";
const char CRfv[] = "Output2.out";
const double CEps = 0.0000001;

void clear(const char fv[]);
void write(const char fv[], double a, int b);
double count(double rate, double x);

int main()
{
	clear(CRfv);
	double c;
	double f;
	double x;
	double s = 0.0000000;
	int t;
	double rate = 2.0000000;
	ifstream fd(CDfv);
	fd >> t;
	for (int i = 0; i < t; i++)
	{
		fd >> c;
		fd >> f;
		fd >> x;
		s = 0.0000000;
		rate = 2.0000000;
		while(i != -1)
		{
			if (count(rate, x) - (count(rate + f, x) + count(rate, c)) > CEps) 
			{
				s +=  count(rate, c);
				rate += f;
			}
			else 
			{
				s += count(rate, x);
				break;
			}
		}
		write(CRfv, s, i+1);
	}
	fd.close();
}

void clear(const char fv[])
{
	ofstream fr(fv);
	fr.close();
}

void write(const char fv[], double a, int b)
{
	ofstream fr(fv, ios::app);
	fr << "Case #" << b << ": " << setprecision(7) << fixed << a << endl;
	fr.close();
}

double count(double rate, double x)
{
	double a = x / rate;
	return a;
}