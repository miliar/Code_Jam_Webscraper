#include <iostream>
#include <sstream> 
#include <string> 

using namespace std;

int main(){
	unsigned long long int num, a;
	short int casos;
	bool acabado, seguir;

	cin >> casos;
	bool numbers[10];

	for (int m = 1; m <= casos; ++m){
		cin >> num;
		if (num == 0)
			cout << "Case #" << m << ": INSOMNIA\n";
		else {
			acabado = false;
			for (int i = 0; i < 10; ++i)numbers[i] = false;
			for (int j = 1; !acabado; ++j){
				string palabra; seguir = true; stringstream stream;
				a = num*j;
				stream << a;
				palabra = stream.str();
				for (int k = 0; k < palabra.size(); ++k){
					numbers[int(palabra[k]) - int('0')] = true;
				}
				acabado = true;
				for (int l = 0; l < 10 && acabado; ++l){
					if (numbers[l] == false)acabado = false;
				}
			}
			cout << "Case #" << m << ": " << a << '\n';
		}

	}
	return 0;
}