#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	
	int cantidadCasos, casoNumero = 1, cantMas;
	int i, k;
	int respuesta = 0;
	string entrada;
	freopen("B-large.in","r",stdin);
	freopen("salidaLarge.out","w",stdout);
	cin >> cantidadCasos;
	while(cantidadCasos>0){
		cin >> entrada;
		cantMas = 0;
		respuesta = 0;
		if(entrada.length() == 1){
			if(entrada.substr(0,1) == "+") cout << "Case #" << casoNumero << ": " << 0 << endl;
			else cout << "Case #" << casoNumero << ": " << 1 << endl;
		}
		else{
			while(entrada.length() != cantMas){
				i = 0;
				while(entrada.at(i) == entrada.at(i+1)){
					i++;
					if(i+2 > entrada.length()){
						cantMas = entrada.length();
						break;
					}
				}
				if(entrada.substr(0,1) == "+" && cantMas != entrada.length()){
					for(k = 0; k <= i; k++){
						entrada[k] = '-';
					}
					respuesta++;
				}
				else if(entrada.substr(0,1) == "-"){
					for(k = 0; k <= i; k++){
						entrada[k] = '+';
					}
					respuesta++;
				}
			}
			cout << "Case #" << casoNumero << ": " << respuesta << endl;
		}
		casoNumero++;
		cantidadCasos--;
	}
	return 0;
}
