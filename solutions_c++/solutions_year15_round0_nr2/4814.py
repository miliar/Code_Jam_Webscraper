#include <iostream>
#include <stdio.h> 
#include <string.h> 
#include <algorithm>
#include <vector>       
using namespace std;
 
int reconstruccion(vector<int> myvector,int numcambios){
		vector <int> myvectoraux;
		myvectoraux=myvector;
 
		int comprobante;
		int comprobante2;
		int comprobante3;
		int comparador;
		int auxdiv;
		int divis;
		int comp;
		int auxcompr;
		int numcambiosaux;
		int numcambiado;
		comprobante=myvectoraux.back();
		auxcompr=comprobante-numcambios;
		divis=2;
		numcambiado=1;
		    if (comprobante%divis!=0){
			comp=(comprobante/divis)+1;
		    } else comp=comprobante/divis;
		while (auxcompr<comp){
			++divis;
			if (comprobante%divis!=0){
			comp=(comprobante/divis)+1;
		    } else comp=comprobante/divis;
			++numcambiado;
		}
		numcambiosaux=numcambios;
		myvectoraux.pop_back();
		comprobante2=myvectoraux.back();
		while((myvectoraux.size()>0) && (comprobante2>auxcompr)){
			auxdiv=1;
			comparador=comprobante2;
			while (comparador>auxcompr){
				++auxdiv;
				if (comprobante2%auxdiv!=0){
					if (((comprobante2/auxdiv)+1)<auxcompr) { 
						comprobante2=(comprobante2/auxdiv)+1;
						comparador=comprobante2;
					}
					else comparador=(comprobante2/auxdiv)+1;
				}
				else {
					if ((comprobante2/auxdiv)<auxcompr) {
						comprobante2=comprobante2/auxdiv;
						comparador=comprobante2;
					}
					else comparador=(comprobante2/auxdiv);
				}
			}
			numcambiado+=auxdiv-1;
			myvectoraux.pop_back();
			comprobante2=myvectoraux.back();
		}
	return numcambiado+auxcompr;
}	
 
int main() {
 
 
 
    int mydishes[1000];
	int casos;
	int platos;
	int numturnos;
	int mejorturnos;
	int mejorturnosant;
	int platosaux;
	int platoactual;
	int numcaso;
	int fuerceprimera;
	numcaso=1;
	cin >> casos;
	while (casos>0){
		cin >> platos;
		platosaux=platos;
		while(platosaux>0){
			cin >> platoactual;
			mydishes[platosaux-1]=platoactual;
			--platosaux;
		}
		std::vector<int> myvector (mydishes, mydishes+platos);
		std::sort (myvector.begin(), myvector.end());
		numturnos=0;
		fuerceprimera=myvector.back();
		mejorturnosant=myvector.back();
		while(numturnos<(fuerceprimera-1)){
			++numturnos;
			mejorturnos=reconstruccion(myvector,numturnos);
			if (mejorturnos<mejorturnosant){
				mejorturnosant=mejorturnos;
			}
		}
		if (mejorturnos==0){
			mejorturnosant==myvector.back();
		}
		printf("Case #%i: %i\n",numcaso,mejorturnosant);
		--casos;
		++numcaso;
	}
	return 0;
}