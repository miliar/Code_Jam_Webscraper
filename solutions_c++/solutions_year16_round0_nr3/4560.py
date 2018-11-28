#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <fstream>
using namespace std;

struct tcomprobao{
	bool vabien;
	long int cual;
};


const long int TOPE = 104;

int main(){
	ifstream datos("entrada.txt");
	ofstream salida("salida.txt");
	bool noprimoh[TOPE] = { false }; int cont;unsigned long long int sumas[9],largo;
	int numcasos, N, J; vector<long int> primos; bool guay; tcomprobao estebien[9];
	datos >> numcasos;
	for (int i = 2; i < TOPE; ++i){
		if (!noprimoh[i])
			primos.push_back(i);
		for (int cont = 2; i * cont < TOPE; ++cont){
			noprimoh[i * cont] = true;
		}
	}
	long long int mod = 1;
	for (int y = 0; y < primos.size(); ++y)mod *= primos[y];
	for (int i = 1; i <= numcasos; ++i){
		datos >> N >> J; s << "Case #" << i << ":\n";
		string number = "", copia = "";
		number.push_back('1');
		for (int i = 1; i < N - 1; ++i){
			number.push_back('0');
		}
		number.push_back('1'); cont = 0;
		while (cont < J){
			for (short int j = 0; j < 9; ++j){
				sumas[j] = 0;
				estebien[j].vabien = false;
			}
			for (int k = 1; k <= N; ++k){
				if (number[k - 1] == '1')sumas[0] += pow(2, (N - k));
			}
			long long int a, b;
			for (int k = 3; k <11; ++k){
				a = pow(k, 16); a = a % mod;
				b = pow(k, 15); b = b % mod;
				sumas[k - 2] = (a*b) % mod;
			}


			for (int k = 17; k <= N; ++k){
				if (number[k - 1] == '1'){
					for (int l = 3; l < 11; ++l){
						sumas[l - 2] += pow((l), (N - k));
						sumas[l - 2] = sumas[l - 2] % mod;
					}
				}
			}
			guay = false;
			for (long int b = 0; b < primos.size() && !guay; ++b){
				for (int a = 0; a < 9; ++a){
					if (sumas[a] % primos[b] == 0){
						estebien[a].vabien = true;
						estebien[a].cual = primos[b];
					}
				}
				guay = true;
				for (int a = 0; a < 9; ++a){
					if (!estebien[a].vabien)guay = false;
				}
			}
			if (guay){
				++cont;
				cout << number;
				for (int z = 0; z < 9; ++z){ cout << " " << estebien[z].cual; }
				cout << '\n';
			}
			sumas[0] += 2; number = ""; copia = ""; int vueltas = 0;
			while (vueltas<N - 1){
				number.push_back(char(sumas[0] % 2 + int('0')));
				sumas[0] = sumas[0] / 2;
				++vueltas;
			}
			number.push_back(char(sumas[0] + int('0')));
			for (int v = number.size() - 1; v >= 0; --v){
				copia.push_back(number[v]);
			}
			number = copia;

		}
	}
	return 0;
}