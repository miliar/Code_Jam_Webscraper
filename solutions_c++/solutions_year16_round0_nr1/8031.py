#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

int main() {
	
	int cantidadCasos, digito, ultimo;
	int i = 1, j;
	long long int entrada, temp, fin;
	long long int numero;
	freopen("A-large.in","r",stdin);
	freopen("salidaLarge.out","w",stdout);
	
	cin >> cantidadCasos;
	while(cantidadCasos>0){
		cin >> entrada;
		j = 1;
		numero = 0;
		if(entrada == 0) cout << "Case #" << i << ": INSOMNIA" << endl;
		else{
			while(numero != 1111111111){
				temp =  j * entrada;
				fin = temp;
				while(temp > 0){
					digito = temp - (temp/10) * 10;
					ultimo = numero / (1 * pow(10,digito));
					if(ultimo - (ultimo/10) * 10 == 0) numero = numero + 1 * pow(10,digito);
					temp = temp / 10;
				} 
				j++;
			}
			cout << "Case #" << i << ": " << fin << endl;
		}
		i++;
		cantidadCasos--;
	}
	return 0;
}
