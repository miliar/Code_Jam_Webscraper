#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int cantidadRepetidos(int primerIntento[],int segundoIntento[],int &elNumero);
void cargoDatos(int array[]);

void cargoDatos(int array[]){
	int fila,basura;
	cin >> fila;
		for(int j = 1; j <= 4; ++j){
			for(int h = 0; h <=3; ++h){
				if(j == fila){
					cin >> array[h];
				}
				else{cin >> basura;}
			}
		}


}

int cantidadRepetidos(int primerIntento[],int segundoIntento[],int &elNumero){
	int res = 0;

	for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j){
			if(primerIntento[i] == segundoIntento[j]){
				res++;
				elNumero = primerIntento[i];
			}
		}
	}

	return res;
}

int main(){
	
	int t,elNumero;
	int primerIntento[4];
	int segundoIntento[4];
	cin >> t;
	for(int i = 1; i <= t; ++i){
		cout << "Case #" << i << ": ";
		cargoDatos(primerIntento);
		cargoDatos(segundoIntento);

		switch (cantidadRepetidos(primerIntento,segundoIntento,elNumero)){
			case 0:
			cout << "Volunteer cheated!" ;
			break;
			case 1:
			cout << elNumero;
			break;
			default:
			cout << "Bad magician!";
			break;
		}
		cout << endl;
	}




	return 0;
}

