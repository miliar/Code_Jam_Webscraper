
#include <iostream>
#include<fstream>
#include<string.h>
#include<sstream>
#include <stdio.h> 
#include <stdlib.h>
#include <iomanip>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

double calcularTiempo(double tiempoHastaAhora, double valorALlegar, double produccionActual){



	return (double)tiempoHastaAhora+(double)(valorALlegar/produccionActual);
}
double segundos(    double costoGranja, double aumentoGranja, double valorALlegar, double actualProduccionGranjas, double tiempoHastaAhora){
	

	double a=calcularTiempo(tiempoHastaAhora,valorALlegar,actualProduccionGranjas);
	double b=calcularTiempo((tiempoHastaAhora+calcularTiempo(0.0,costoGranja,actualProduccionGranjas)),valorALlegar,(actualProduccionGranjas+aumentoGranja));

	if(a>b){
	
	
		tiempoHastaAhora+=calcularTiempo(0.0,costoGranja,actualProduccionGranjas);
		actualProduccionGranjas+=aumentoGranja;

		
		return segundos(     costoGranja,  aumentoGranja,  valorALlegar, actualProduccionGranjas,  tiempoHastaAhora);
	}else{

	return	 (calcularTiempo( tiempoHastaAhora, valorALlegar,  actualProduccionGranjas));
	}
}


int main(int argc, char** argv) {
	
	 ofstream cout("Ejercicio.txt"); 
	 cout.setf(ios::fixed,ios::floatfield);
    cout.precision(7);
	 std::cout << std::setprecision(7) << std::fixed;
	 int op;
	 cin>>op;
	 cin.ignore();
	 int g=1;
	 while(g<=op){
	 
	 
	 
	 	 double matriz[3];
	

 
 	 string s;
	getline(cin,s);

	stringstream ss; 
    string var; 
    ss<<s;
    int contador=0;
 while(ss>>var){
 
 matriz[contador]=atof(var.c_str());

 contador++;
  
}



cout<<"Case #"<<g<<": "<<segundos(matriz[0],matriz[1],matriz[2],2,0)<<endl;
g++;
}
cout.close(); 
	
	return 0;

}




