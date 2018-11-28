/*
Programa creado por Alejandro Linarez Rangel.
Para la Google Code Jam
Problema C a resolver:
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
typedef string quaternion;

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

string CrearLaCadena(string str, mint m)
{
	string s = "";
	for(mint i = 0;i < m;i++)
	{
		s += str;
	}
	return s;
}

quaternion Negar(quaternion a)
{
	if(a[0] == '+')
		return quaternion("-") + a[1];
	else
		return quaternion("+") + a[1];
}

quaternion APositivo(quaternion a)
{
	return quaternion("+") + a[1];
}

quaternion Multiplicar(quaternion a, quaternion b)
{
	if((a[0] == b[0])&&(a[0] == '-'))
		return Multiplicar(APositivo(a),APositivo(b));
	if(a[0] != b[0])
		return Negar(Multiplicar(APositivo(a),APositivo(b)));
	if(a == "+1")
		return b;
	if(b == "+1")
		return a;
	if((a == b)&&(a != "+1"))
		return "-1";
	if((a == b)&&(a == "+1"))
		return "+1";
	if((a == "+j")&&(b == "+i"))
		return "-k";
	if((a == "+i")&&(b == "+j"))
		return "+k";
	if((a == "+i")&&(b == "+k"))
		return "-j";
	if((a == "+k")&&(b == "+i"))
		return "+j";
	if((a == "+k")&&(b == "+j"))
		return "-i";
	if((a == "+j")&&(b == "+k"))
		return "+i";
	return "+1";
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
	for(mint cuenta = 1; cuenta <= T; cuenta++)
	{
		string S = "",ijk = "";
		quaternion B = "";
		mint L = 0, X = 0, Puntero = 0;
		cin >> L >> X;
		getline(cin,S,'\n'); // Lee el final de linea de la segunda linea
		getline(cin,S,'\n'); // lee el verdadero mensaje
		cout << "Case #" << cuenta << ": ";
		if(L == 1)
		{
			cout << "NO" << endl;
			continue;
		}
		S = CrearLaCadena(S,X);
		if(S.size() < 3)
		{
			cout << "NO" << endl;
			continue;
		}
		
		B = quaternion("+") + S[0];
/*		if(B == "+i")
		{
			ijk += "i";
		}
		else
		{
			B = Multiplicar(B,quaternion("+") + S[Puntero+1]);
		}
*/		
		for(mint i = 0;i < S.size();i++)
		{
			if((B == "+i")&&(ijk == ""))
			{
				ijk += "i";
				Puntero++;
				if(Puntero >= S.size())
				{
					cout << "NO" << endl;
					break;
				}
				B = quaternion("+") + S[Puntero];
			}
			
			if((B == "+j")&&(ijk == "i"))
			{
				ijk += "j";
				Puntero++;
				if(Puntero >= S.size())
				{
					cout << "NO" << endl;
					break;
				}
				B = quaternion("+") + S[Puntero];
			}
			
			if((B == "+k")&&(ijk == "ij")&&((Puntero+1)==S.size()))
			{
				ijk += "k";
				break;
			}
			else
			{
				B = Multiplicar(B,quaternion("+") + S[Puntero+1]);
			}
			if(Puntero >= S.size())
			{
				break;
			}
			Puntero++;
		}
		if(ijk == "ijk")
		{
			cout << "YES" << endl;
		}
		else
		{
			cout << "NO" << endl;
		}
	}
	return 0;
}
