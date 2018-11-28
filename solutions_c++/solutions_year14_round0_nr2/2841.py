#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

long double producion(long double, long double, long double );

int main()
{
	
	ifstream abre("B-large.in");
	ofstream output("output.txt");
	int numCase;

/*	cout.setf(ios:fixed);
	cout.setf(ios:showpoint);
	cout.precision(7);*/

	abre >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		long double c, f, x;

		abre >> c;
		abre >> f;
		abre >> x;

		output << "Case #" << (i + 1) << ": " << setprecision(7) << fixed << producion(c, f, x) << endl;
	}


	output.close();
	system("pause");
	return 0;
}

long double producion(long double c, long double f, long double x)
{

	long double acum = 0.0;
	long double resultado = x/2;
	long double res = 0.0;
	long double acumF = 2.0;
	bool centinela = true;



	while (centinela)
	{
		//cout << "KSAJDASD" << endl;

		res = c / acumF + x / (acumF + f) + acum;
		
		if (resultado > res)
		{
			resultado = res;
			acum += c / acumF;
			acumF += f;
		}
		else
			centinela = false;
	}

	return resultado;
}