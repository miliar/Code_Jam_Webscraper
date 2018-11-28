#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main()
{
	fstream plik;
	fstream out;
	out.open("out.txt");
	plik.open("plik.txt");
	long n;
	plik >> n;
	for (int i = 0; i < n; i++)
	{
		long double C, F, X;
		plik >> C >> F >> X;
		long double w = 0;
		long double z = 2;
		while (X / z > C / z + X / (z + F))
		{
			w += C / z;
			z += F;
		}
		w += X / z;
		out << "Case #" << i + 1 << ": ";
		out << setprecision(7);
		out << fixed;
		out<< w << endl;
		
	}
}