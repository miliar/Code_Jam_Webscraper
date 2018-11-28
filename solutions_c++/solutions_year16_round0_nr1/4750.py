#include <iostream>
#include <sstream> 
#include <string> 
using namespace std;
int main(){
	unsigned long long int numero, a; short int casos; bool eano, seguir;
	cin >> casos; bool numbers[10];
	for (int m = 1; m <= casos; ++m){
		cin >> numero;
		if (numero == 0)cout << "Case #" << m << ": INSOMNIA\n";
		else{
			eano = false;
			for (int i = 0; i < 10; ++i)numbers[i] = false;
			for (int j = 1; !eano; ++j){
				string palabra; seguir = true; stringstream stream;
				a = numero*j;
				stream << a;
				palabra = stream.str();
				for (int k = 0; k < palabra.size(); ++k){
					numbers[int(palabra[k]) - int('0')] = true;
				}
				eano = true;
				for (int l = 0; l < 10 && eano; ++l){
					if (numbers[l] == false)eano = false;
				}
			}
			cout << "Case #" << m << ": " << a << '\n';
		}

	}
	return 0;
}