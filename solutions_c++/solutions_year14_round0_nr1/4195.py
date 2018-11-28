/* 
 * File:   main.cpp
 * Author: Proprietario
 *
 * Created on 12 aprile 2014, 19.03
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    ifstream in ("input.in");
    ofstream out("output.out");
    int matrice[4][4];
    int vett1 [4], vett2[4];
    int cont=0, numero;
    int T;
    in>>T;
    for(int i=0; i<T; i++){
        int n;
        in>>n;
        for(int j=0; j<4; j++){
            for(int y=0; y<4; y++){
                int temp;
                in>>temp;
                if(j==n-1){
                    vett1[y]=temp;
                }
            }
            
        }
        in>>n;
      
        for(int j=0; j<4; j++){
            for(int y=0; y<4; y++){
                int temp;
                in>>temp;
                if(j==n-1){
                    vett2[y]=temp;

                }
            }
        }
        cont=0;
        for (int b=0; b<4; b++){
            for(int h=0; h<4; h++){
                if(vett1[b]==vett2[h]){
                    cont++;
                    numero=vett1[b];
                }
            }
        }
        out<<"Case #"<<i+1<<": ";
        if(cont==1){
            out<<numero;
        }
        if(cont==0){
            out<<"Volunteer cheated!";
        }
        if(cont!=0 && cont!=1){
            out<<"Bad Magician!";
        }
        out<<endl;
    }
    
    return 0;
}

