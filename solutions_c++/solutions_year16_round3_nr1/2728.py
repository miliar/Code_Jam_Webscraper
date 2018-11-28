using namespace std;
#include <iostream>
#include <fstream>
#include <math.h>
#include <string>

char traducir(int num);

int main(){
	int numCasos, numPartidos, candPartido;
	int listado[30];
	int maximos[30];
	fstream infile("prueba.in");
	ofstream outfile("solu.out");
	infile >> numCasos;
	for (int n = 0; n < numCasos; n++)
	{
		infile >> numPartidos;
		for (int i = 0; i < numPartidos; i++){
			infile >> candPartido;
			listado[i] = candPartido;
		}
		//lista rellena
		outfile << "Case #" << n + 1 << ": ";
		//tomas el maximo
		int cont, maxi;
		maxi = listado[0];
		for (int i = 1; i < numPartidos; i++){
			if (listado[i] > maxi) maxi = listado[i];
		}
		while (maxi > 0)
		{		
			//cuentas el numero de máximos
			cont = 0;
			for (int i = 0; i < numPartidos; i++){
				if (listado[i] == maxi){
					maximos[cont] = i; //guarda la posicion de los máximos
					cont++;
				}
			}
			//si único o hay 3 iguales a 1
			if (cont == 1 || (maxi == 1 && cont == 3)) {
				outfile << traducir(maximos[0]) << " ";
				listado[maximos[0]]--;
			}
			//si mas de 2, quitas 2
			else if (cont > 1 ){
				outfile << traducir(maximos[0]) << traducir(maximos[1]) << " ";
				listado[maximos[0]]--;
				listado[maximos[1]]--;
			}
			//comprobamos
			maxi = listado[0];
			for (int i = 1; i < numPartidos; i++){
				if (listado[i] > maxi) maxi = listado[i];
			}
		}
		outfile << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}
char traducir(int num){
	if (num == 0) return 'A';
	else if (num == 1) return 'B';
	else if (num == 2) return 'C';
	else if (num == 3) return 'D';
	else if (num == 4) return 'E';
	else if (num == 5) return 'F';
	else if (num == 6) return 'G';
	else if (num == 7) return 'H';
	else if (num == 8) return 'I';
	else if (num == 9) return 'J';
	else if (num == 10) return 'K';
	else if (num == 11) return 'L';
	else if (num == 12) return 'M';
	else if (num == 13) return 'N';
	else if (num == 14) return 'O';
	else if (num == 15) return 'P';
	else if (num == 16) return 'Q';
	else if (num == 17) return 'R';
	else if (num == 18) return 'S';
	else if (num == 19) return 'T';
	else if (num == 20) return 'U';
	else if (num == 21) return 'V';
	else if (num == 22) return 'W';
	else if (num == 23) return 'X';
	else if (num == 24) return 'Y';
	else if (num == 25) return 'Z';
}