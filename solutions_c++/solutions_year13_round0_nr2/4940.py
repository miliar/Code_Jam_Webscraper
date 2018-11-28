#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int main() {	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);	
		
	int T;
	cin >> T;
	cin.ignore();
	
	// T cases
	for (int i=1; i<=T; i++){
		string resultado;
		//dimensiones de cada rectangulo
		short filas, columnas;
		cin >> filas >> columnas;
			
		//datos de cada rectangulo
		vector < vector <short> > tablero;
		short aux;
			
		for (short f=0; f<filas; f++){
			vector <short> vaux;			
			for (short c=0; c<columnas; c++){
				cin >> aux;
				vaux.push_back(aux);
			}			
			tablero.push_back(vaux);
		}
			
		//proceso el tablero	
		while (resultado.empty()){
		
		//busco men1 y men2 
		short men1=101, men2=101;
		
		for (short f=0; f<filas; f++)
			for (short c=0; c<columnas; c++)
				if (tablero[f][c] < men1){
					men2=men1;
					men1=tablero[f][c];
				}
				else
					if (tablero[f][c] < men2 && tablero[f][c] != men1)
						men2=tablero[f][c];
		
		//todo el lawn con la misma altura
		if (men1<101 && men2==101) { 
			resultado="YES";
			continue;
			}
			
		//copio tablero completo
		vector < vector <short> > tableroaux=tablero;
		
		//recorro por filas tablero buscando filas con todos men1
		for (short f=0; f<filas; f++){
			bool todosmen=true;
			short c=0;
			while (c<columnas && todosmen){
				if (tablero[f][c] != men1) todosmen=false;
				else c++;
			}
			
			if (todosmen) //la fila tiene todos iguales a men1
						  //cambio la fila completa en tableroaux a men2
				for (short c=0; c<columnas; c++) tableroaux[f][c]=men2;				
		}
		
		//recorro por columnas tablero buscando columnas con todos men1
		for (short c=0; c<columnas; c++){
			bool todosmen=true;
			short f=0;
			while (f<filas && todosmen){
				if (tablero[f][c] != men1) todosmen=false;
				else f++;
			}
			
			if (todosmen) //la columna tiene todos iguales a men1
						  //cambio la columna completa en tableroaux a men2
				for (short f=0; f<filas; f++) tableroaux[f][c]=men2;				
		}
		
		// verifico que en tableroaux no queden elementos = men1
		bool bandera=false;
		for (short f=0; f<filas && !bandera; f++)
			for (short c=0; c<columnas && !bandera; c++)
				if (tableroaux[f][c]==men1) bandera=true;
		
		if (bandera) //quedo algún valor men1, no se puede cortar el cesped
			{ 
				resultado="NO";
				continue;
			}
		
		tablero=tableroaux;
			
		}
		cout << "Case #" << i << ": " << resultado << endl;
		resultado.clear();
	}
	
	return 0;
}
