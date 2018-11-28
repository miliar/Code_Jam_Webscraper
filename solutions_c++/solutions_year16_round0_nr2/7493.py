#include<iostream>
#include<fstream>
#include <string>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

char opuesto(char c){
	if (c == '+')return '-';
	else return '+';
}

bool check(const string& pan){
	int i = 0;
	while (i < pan.size() && pan[i] == '+')++i;
	return !(i < pan.size());
}

void girar(string & pan){
	char a = pan[0];
	int i = 0;
	while (i < pan.size() && pan[i] == a){
		pan[i] = opuesto(pan[i]);
		++i;
	}
}

int main(){
	ifstream tEntrada;
	tEntrada.open("B-large.in");
	ofstream tSalida;
	tSalida.open("B-large.out");
	unsigned int numCasos;
	tEntrada >> numCasos;
	for (int z = 1; z <= numCasos; ++z){
		unsigned long long int cont = 0;
		string pan;
		tEntrada >> pan;
		bool ok = check(pan);
		while (!ok){
			girar(pan);
			ok = check(pan);
			++cont;
		}
		tSalida << "Case #" << z << ": " << cont << '\n';
	}


	tEntrada.close();
	tSalida.close();
	return 0;
}