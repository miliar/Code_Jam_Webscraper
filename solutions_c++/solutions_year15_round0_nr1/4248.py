/*
Programa creado por Alejandro Linarez Rangel.
Para la Google Code Jam
Problema A a resolver:
En ISO C++11.
*/
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <functional>
#include <utility>
#include <complex>
#include <bitset>
#include <fstream>
#include <sstream>
#include <tuple>
#include <regex>

using namespace std;

// Valor para numeros enteros,(dependiendo del problema)
typedef long int mint;
// Valor para numeros reales
typedef long double mreal;

mint ANumero(string str)
{
	return stol(str); // si cambiase la definicion de mint, hay que cambian stol
	// por el valor adecuado(stoi,stol,stoll,stoull, ...)
}

mreal AReal(string str)
{
	return stold(str); //si cambiase la definicion de mreal, hay que cambian stold
	// por el valor adecuado(stod,stold, ...)
}

int main (int argc, char const* argv[])
{
	mint T;
	{
		string Tstr;
		cin >> Tstr;
		T = ANumero(Tstr);
		getline(cin,Tstr,'\n');
	}
	for(int cuenta = 1; cuenta <= T; cuenta++)
	{
		mint Smax;
		cin >> Smax;
		{
			char espacio;
			cin.get(espacio);
		}
		vector<mint> Personas;
		for(mint i = 0; i <= (Smax); i++)
		{
			char cantidad;
			cin.get(cantidad);
			string clave = "";
			clave += cantidad;
			Personas.push_back(ANumero(clave));
		}
		mint cantidadDeAmigos = 0;
		mint personasParadas = 0;
		for(mint i = 0;i <= Smax;i++)
		{
			if(Personas[i] == 0)
				continue;
			if(personasParadas < i)
			{
				mint restante = i - personasParadas;
				personasParadas += restante + Personas[i];
				cantidadDeAmigos += restante;
			}
			else
			{
				personasParadas += Personas[i];
			}
		}
		cout << "Case #" << cuenta << ": " << cantidadDeAmigos << endl;
	}
	return 0;
}
