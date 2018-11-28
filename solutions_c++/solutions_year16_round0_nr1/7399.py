#include<iostream>
#include<fstream>
#include <string>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){
	ifstream tEntrada;
	tEntrada.open("A-large.in");
	ofstream tSalida;
	tSalida.open("A-large.out");
	unsigned int numCasos;
	tEntrada >> numCasos;
	for (int z = 1; z <= numCasos; ++z){

		long long int n;
		tEntrada >> n;
		if (n != 0){
			vector<bool> num(10, false);
			bool ok = false;
			unsigned long long int h = 1;
			unsigned long long int m;
			while (!ok){
				m = n* h;
				int div = 1;
				while (m / div >= 10) div *= 10;
				for (int i = 1; i <= div; i *= 10){
					int j = (m / i) % 10;
					num[j] = true;
				}
				int a = 0;
					while (a < 10 && num[a] == true)++a;
					ok = !(a < 10);
				++h;
			}

			tSalida << "Case #" << z << ':' << ' ' << m <<'\n';
		}

		else tSalida << "Case #" << z << ':' << ' ' << "INSOMNIA" << '\n';

	}


	tEntrada.close();
	tSalida.close();
	return 0;
}