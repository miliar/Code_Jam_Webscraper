/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: cristhiancamilo
 *
 * Created on 8 de abril de 2016, 06:10 PM
 */

#include <cstdlib>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int t, count, count2, tamano, countEx, varita;
    bool z = 1;
    cin >> t;
    int arreglo[t];
    int arreglo2[10];
    for (int i = 0; i < t; i++) {
        cin >> arreglo[i];
    }

    for (int i = 0, z = 1, count = 0, count2 = 2; i < t; i++, count = 0, count2 = 2) {
        if (arreglo[i] != 0) {
            varita = arreglo[i];
            for (int k = 0; k < 10; k++) {
                arreglo2[k] = 100;
            }
            while (count < 10) {
                countEx = 0;
                for (int j = arreglo[i]; j > 0; j /= 10) {
                    countEx++;
                }
                for (int j = 0, tamano = arreglo[i]; j < countEx; j++) {
                    if (arreglo2[tamano % 10] == 100) {
                        arreglo2[tamano % 10] = tamano % 10;
                        count++;
                    }
                    tamano /= 10;
                }

                arreglo[i] = varita * count2;
                count2++;
            }
            arreglo[i] -= varita;
        }

    }
    for (int i = 0; i < t - 1; i++) {
        if(arreglo[i] != 0){
            cout << "case #" << i + 1 << ":" << " " << arreglo[i] << "\n";
        }else
            cout << "case #" << i + 1 << ":" << " INSOMNIA" << "\n";
    }
    if(arreglo[t - 1] != 0){
            cout << "case #" << t << ":" << " " << arreglo[t - 1];
        }else
            cout << "case #" << t << ":" << " INSOMNIA";
    return 0;
}

