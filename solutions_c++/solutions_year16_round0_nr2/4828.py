#include <iostream>
using namespace std;

int main(){
	bool positivo = true; int numcasos, cont;
	cin >> numcasos;
	char a, b;
	cin.get(a);
	for (int i = 1; i <= numcasos; ++i){
		cin.get(a); b = ' '; cont = 0;
		if (a == '+')positivo = true;
		else positivo = false;
		for (int j = 0; b != '\n'; ++j){
			cin.get(b);
			if (b != '\n'){
				if (b != a && positivo){
					positivo = false;
					++cont;
				}
				else if (b != a && !positivo){
					positivo = true;
					++cont;
				}
				a = b;
			}
		}
		if (!positivo)++cont;
		cout << "Case #" << i << ": " << cont << '\n';
	}
	return 0;
}