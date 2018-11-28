#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int main (){
int casos, i;
fstream archivoin("B-small-attempt0.in");
fstream archivoout("B-small-practice.out");

if((archivoin)&&(archivoout)){
   archivoin >> casos;
    for(i=0;i<casos;i++){
        long int A,B,K;
        archivoin >> A;
        archivoin >> B;
        archivoin >> K;
        
        long int solu=0;
        for(int j=0;j<A;j++){
        	for(int k=0;k<B;k++){
        		if((j & k)<K){
        			solu++;
        		}
        	}
        }
        cout << solu << endl;
        archivoout << "Case #"<< i+1 << ": ";
        archivoout << solu;
        if(i!=casos-1) archivoout << endl;
    }
    archivoin.close();
    archivoout.close();
} else cout << "No se pudo abrir el archivo" << endl;

//int hola =0 & 0;
//cout << hola;
return 0;
}
