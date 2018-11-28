#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <utility>
#include <sstream>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <math.h>

using namespace std;

int i , j , k;

int main ()
{
	int ncases;
	int veces;
	double C, F, X;
	int galletas;
	double total;
	double costo;
	double menor;
	double incremento;
	int conta;
	double ant = 100000000;
	scanf ("%d", &ncases);
	
//	printf ("%d\n", ncases);
	for ( i =0; i < ncases;i++){
	
		scanf("%lf %lf %lf", &C, &F, &X);
		
		//C costo por granja
		//F incremendo
		//X total;
		total = 0.0;
		//de un doblar 1 hasta 50 veces		
	/*	for ( veces=1; veces<=50;veces++){
			total = 0.0;
			for ( i =1; i <=veces;i++){//estos son los doblobnes
				
				while ( )
			}
		}*/
	menor = 100000000;	
	for ( k =0; k <=2000;k++){
		
		
		veces = k;//son 4 el ultimo dejalo ser
		
	
		total =0.0;
		costo = 0.0;
		incremento = 2.0;	
		
		for ( j =0; j < veces;j++){
			
			costo = C / incremento;
			//printf ("** %f   %f  %f\n", costo, incremento, total);
			total += costo;
			incremento += F;
		}
		
		costo = X/incremento;
		total += costo;
	//	printf ("vceces %d %f \n", veces, total);
		if ( total < menor) menor = total;
		
		
	}// fin vedces
	
		printf("Case #%d: %.7lf\n", i+1, menor);
	}//fin ncases
	return 0;
	

}




