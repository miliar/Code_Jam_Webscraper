#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;


void main (void){
	int t,T;
	int listo;

	double C, F, X,p;
	double t_sin_comprar, t_comprando, t_acum;

	string temp;

	getline(std::cin,temp);
	istringstream(temp) >> T;

	for (t =0; t < T ; t++){
		//cerr << t;

		getline(std::cin,temp);
		istringstream(temp) >> C >> F >> X;

		listo=0;
		t_acum=0;
		p=2;
		
		
		while (!listo){

			t_sin_comprar=(X)/p;	//tiempo que tardo a esta tasa 

			t_comprando = C/p+(X)/(p+F);	//tiempo que tardaria si mejoro la producción

			if (t_sin_comprar<t_comprando){
				t_acum +=(X)/p;
				listo=1;
			}else{
				t_acum+=C/p;
				p+=F;
			}
		}
		
		cout.precision(7);
		cout << "Case #" << t+1 << ": " << fixed << t_acum << endl  ;	
	}

}