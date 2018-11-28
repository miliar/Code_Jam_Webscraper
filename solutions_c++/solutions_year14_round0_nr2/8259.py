#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;


int main(int argc, char *argv[]){
	
	int cases, i;
	double produccion, produccion_extra, granja,
		
		tiempo, tiempo_actual, tiempo_mejor, objetivo;
	
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	
	
	cin >> cases;
	
	for(i=1; i<=cases; i++){
		
		tiempo=0.0; produccion=2.0;
		cin >> granja >> produccion_extra >> objetivo;
		
		
		tiempo_actual = (tiempo + objetivo/produccion);
		
		do{
			tiempo_mejor=tiempo_actual;
			
			tiempo += granja/produccion;
			produccion+=produccion_extra;
			
			tiempo_actual=(tiempo + objetivo/produccion);
			
			
		} while(tiempo_actual<tiempo_mejor);
		
		tiempo=0.0;
		produccion=0.0;
		
		cout << "Case #" << i << ": " << fixed << setprecision(7) << tiempo_mejor << endl;
	}
	
	return 0;
}

