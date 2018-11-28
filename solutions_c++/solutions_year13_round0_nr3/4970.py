#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <fstream>

using namespace std;

int main() {

  ofstream file;
  file.open ("Output3.txt");

  int t;
  cin >> t;

  for(int k=1; k<=t; k++){

    int cont=0;

    long long int a, b;
    cin >> a >> b;

    for(long long int i=a; i<=b; i++){
        int aux=sqrt(i);

        if((int)pow(aux,2)==i){
            char cuadrado[sizeof(long long int)*8+1];
            char raiz[sizeof(long long int)*8+1];
            itoa(i,cuadrado,10);
            itoa(aux,raiz,10);

            string cuadradoS=cuadrado;
            string auxS=raiz;

            if(cuadradoS.size()==1&&auxS.size()==1){
                cont++;
            } else {

                bool cuadradoBool=true;
                for(int j=0; j<cuadradoS.size()/2+1; j++){
                    if(cuadradoS.at(j)!=cuadradoS.at(cuadradoS.size()-1-j)){
                        cuadradoBool=false;
                        break;
                    }
                }

                bool raizBool=true;

                if(auxS.size()!=1){
                    for(int j=0; j<auxS.size()/2+1; j++){
                        if(auxS.at(j)!=auxS.at(auxS.size()-1-j)){
                            raizBool=false;
                            break;
                        }
                    }
                }

                if(raizBool==true&&cuadradoBool==true){
                    cont++;
                }

            }

        }
    }

    file << "Case #" << k << ": " << cont << endl;

  }

  //cout << cont;

  file.close();

  return 0;
}
