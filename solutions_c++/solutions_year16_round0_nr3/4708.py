// Errachete - C: Coin jam

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

using lint = unsigned long long int;

ifstream fin;
ofstream fout;
vector< lint > primos;

vector<lint> calcularPrimos()
{
	bool primo = true;
	lint num = 3;
	vector< lint > v(1, 2);

	while (num <= 10000)
	{
		lint i = 0;
		primo = true;
		while (i < v.size() && primo)
		{
			if (num % v[i] == 0)
				primo = false;
			++i;
		}
		if (primo)
		{
			v.push_back(num);
		}
		++num;
	}
	
	return v;
}

ostream & operator<<(ostream & fout, vector< lint > const& divisores)
{
	for (int i = 0; i < divisores.size() - 1; ++i)
		fout << divisores[i] << ' ';
	fout << divisores.back() << '\n';
	return fout;
}

bool base2(vector< lint > & divisores, string const& num)
{
	const int base = 2;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}
bool base3(vector< lint > & divisores, string const& num)
{
	const int base = 3;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}
bool base4(vector< lint > & divisores, string const& num)
{
	const int base = 4;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}
bool base5(vector< lint > & divisores, string const& num)
{
	const int base = 5;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}
bool base6(vector< lint > & divisores, string const& num)
{
	const int base = 6;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}
bool base7(vector< lint > & divisores, string const& num)
{
	const int base = 7;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}
bool base8(vector< lint > & divisores, string const& num)
{
	const int base = 8;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}
bool base9(vector< lint > & divisores, string const& num)
{
	const int base = 9;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}
bool base10(vector< lint > & divisores, string const& num)
{
	const int base = 10;
	int i = 0;
	lint numer = 0;

	lint potencia = 1;
	for (int j = num.size() - 1; j >= 0; --j)
	{
		if (num[j] == '1')
		{
			numer = numer + potencia;
		}
		potencia *= base;
		
	}

	while (i < primos.size() && divisores[base - 2] == 0)
	{
		if (numer % primos[i] == 0)
			divisores[base - 2] = primos[i];
		++i;
	}
	if (divisores[base - 2] == 0)
		return true;
	else
		return false;
}

void aumentar(string & num)
{
	bool cambio = false;

	int i = num.size() - 2;
	while (!cambio)
	{
		if (num[i] == '0')
		{
			num[i] = '1';
			cambio = true;
		}
		else
		{
			num[i] = '0';
			--i;
		}
	}
}

void resolucion()
{
	int longitud = 0, numeros = 0;
	bool primo = false;
	string num = "1";

	fin >> longitud >> numeros;

	for (int i = 0; i < longitud - 2; ++i)
		num.push_back('0');
	num.push_back('1');

	while (numeros > 0)
	{
		vector< lint > divisores(9, 0);
		primo = false;
		primo = base2(divisores, num);
		if (!primo)
			primo = base3(divisores, num);
		if (!primo)
			primo = base4(divisores, num);
		if (!primo)
			primo = base5(divisores, num);
		if (!primo)
			primo = base6(divisores, num);
		if (!primo)
			primo = base7(divisores, num);
		if (!primo)
			primo = base8(divisores, num);
		if (!primo)
			primo = base9(divisores, num);
		if (!primo)
			primo = base10(divisores, num);
		if (!primo)
		{
			fout << num << ' ' << divisores;
			--numeros;
		}

		aumentar(num);
	}
}

int main()
{
	fin.open("input.txt");
	fout.open("output.txt");
	primos = calcularPrimos();
	int numCasos = 0;
	fin >> numCasos;
	for (int i = 0; i < numCasos; ++i)
	{
		fout << "Case #" << i + 1 << ":\n";
		resolucion();
	}
	fin.close();
	fout.close();
	return 0;
}