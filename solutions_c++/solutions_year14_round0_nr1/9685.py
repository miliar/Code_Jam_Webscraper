#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <math.h>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <unistd.h>
#include <vector>

using namespace std;

bool compare(const int &a, const int &b){
    return a<b;
}

int main(){
    int t,r1,r2;
    int mat1[4][4];
    int mat2[4][4];

    fstream lectura;
    ofstream myfile;
    myfile.open("salida.txt");
    lectura.open("A-small-attempt5.in");
    lectura >> t;

    for(int xxx=0; xxx<t; xxx++){
        int cont=0,aux=0;

        lectura >> r1;
        //cout << r1 << endl;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                lectura >> mat1[i][j];
                //cout << mat1[i][j] << " ";
            }
            //cout << endl;
        }

        lectura >> r2;
        //cout << r2 << endl;

        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                lectura >> mat2[i][j];
                //cout << mat2[i][j] << " ";
            }
            //cout << endl;
        }
        //cout << endl;


        myfile << "Case #" << (xxx+1) <<": ";

        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if(mat1[r1-1][i]==mat2[r2-1][j]){
                    cont++; aux=mat1[r1-1][i];
                }
            }
        }
        //cout << cont << endl;

        if(cont>1){
            myfile << "Bad magician!" << endl;
        }else if(cont == 1){
            myfile << aux << endl;
        }else if(cont == 0){
            myfile << "Volunteer cheated!" << endl;
        }

    }
lectura.close();
        myfile.close();
    return 0;
}
