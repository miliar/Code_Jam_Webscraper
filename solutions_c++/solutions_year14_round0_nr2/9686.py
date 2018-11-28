#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, char *argv[]) {
	double x,c,f,t,rate,r, farms;
	double y, nuevo;
	
	cin >> t;
	
	for(int caso=1; caso <= t; caso++){
		rate = 2;
		farms = 0;
		cin >> c >> f >> x;
		
		nuevo = x/rate; 	//No compra ningun farm
		
		do{
			y = nuevo;
			//Compra un farm
			farms++;
			rate += f;
		
			nuevo = x/rate;
			//Aca se suma lo que le costo para comprar las farm
			r = 2.;
			for(int i=0; i < farms; i++){
				nuevo += c/r;
				r += f;
			}
			
		}while (x >= 0 && nuevo < y);
		
		cout << "Case #" << caso << ": ";
		printf("%.7f\n",y);
	}
	
	return 0;
}

