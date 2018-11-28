#include <fstream>
#include <iostream>
using namespace std;

int main(){
	ifstream datos("datos.txt");
	ofstream salida("salida.txt");
	int n, cont; char x, y;
	datos >> n; datos.get(x);
	for (int i = 0; i < n; ++i){
		cont = 0; 
		datos.get(x); y = x;
		while (x != '\n'){
			if (y != x)	++cont;
			y = x;
			datos.get(x);
		}
		if (y == '-') ++cont;
		salida << "Case #" << i+1 << ": " << cont << '\n';
	}
	return 0;
}