#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main(){

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	string cadena;
	long long cont = 0;
	char ultimoSigno = '+';
	for(int caso = 1; caso<=T;caso++)
	{
		cont = 0;
		ultimoSigno = '+';
		cin >> cadena;

		for(int letra = cadena.size()-1;letra>=0;letra--)
		{
			if(cadena.at(letra) != ultimoSigno)
			{
				cont++;
				ultimoSigno = cadena.at(letra);
			}
		}
		cout << "Case #" << caso << ": " << cont << endl;
	}
	return 0;
}