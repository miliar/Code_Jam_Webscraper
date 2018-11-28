#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

double calculate(double C, double F, double X, int n)
{
	double secs = 0;
	int cookies = 0;
	int f = 0;
	double gen = 2;
	while (f < n)
	{
		secs += C/gen;
		gen+=F;
		f++;
	}
	return secs+(X/gen);
}

double power(int n)
{
	double ret = 1;
	for (int i = 0; i < n; i++)
		ret *= 10;
	return ret;
}

double rnd(double num, int prec)
{
	double tmp = num*power(prec);
	tmp += 0.5;
	tmp = floor(tmp);
	tmp /= power(prec);
	return tmp;
}

int main(int argc, char **argv)
{
	int f = 0;
	FILE *outPtr = fopen("output1.txt", "w");
	ifstream ifstr;
	ifstr.open("input.txt", ios::in);
	int T;
	ifstr >> T;
	for (int a = 1; a <= T; a++)
	{
		string Cstr, Fstr, Xstr;
		long double C, F, X;
		char *v = 0;
		ifstr >> C >> F >> X;
		double min = 100000000;
		int f = 0;
		double ret = 0;
		min = calculate(C, F, X, f);
		f++;
		// cout << ret << endl;
		while (min > (ret = calculate(C, F, X, f)))
		{
			// cout << ret << endl;
			min = ret;
			f++;
		}
		//cout << ret << endl;
		fprintf(outPtr, "Case #%d: %0.7lf\n", a, min);
	}
	ifstr.close();
	fclose(outPtr);
	return 0;
}