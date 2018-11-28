/*
Programa creado por Alejandro Linarez Rangel.
Para la Google Code Jam
Problema D a resolver:
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
typedef vector<bool> omino_interno;
typedef vector<omino_interno> omino;

const bool Bloque = true;
const bool Vacio = false;

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

void ObtenerPar(mint X,mint& a,mint& b)
{
	mreal R = (X / 2.0);
	a = ceil(R);
	b = floor(R);
}

void OmiConstructor(mint X,mint& Al,mint& An)
{
	mint estado = 1;
	mint alto = 0,ancho = 1;
	for(mint bloques = 1;bloques <= X;bloques++)
	{
		if(estado == 0)
		{
			estado++;
			ancho++;
		}
		if(estado == 1)
		{
			estado--;
			alto++;
		}
	}
	Al = --alto;
	An = --ancho;
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
		mint X = 0,R = 0,C = 0;
		cin >> X >> R >> C;
		cout << "Case #" << cuenta << ": ";
		mreal Resultado = ((R * C) + 0.0)/ (X - 0.0);
		mint Techo = ceil(Resultado);
		mint Piso = floor(Resultado);
		if(Techo != Piso) // el area no se puede cubir con X-ominoes
		{
			cout << "RICHARD" << endl;
			continue;
		}
		// Para terminar, hay que buscar un X-omino que sea mayor que R y C
		mint alto = 0,ancho = 0;
		OmiConstructor(X,alto,ancho);
		if(((alto > R)||(ancho > C))||((ancho > R)||(alto > C))) // existe un X-omino que no entra en R*C
		{
			cout << "RICHARD" << endl;
			continue;
		}
		cout << "GABRIEL" << endl;
	}
	return 0;
}
