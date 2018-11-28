/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: cristhiancamilo
 *
 * Created on 9 de abril de 2016, 09:23 AM
 */

#include <cstdlib>
#include <iostream>
using namespace std;

/*
 * 
 */
int valDiv[9];

int esPrimo(long int a, int b) {

    long int x = 2;
    
    while (a % x && x <= 101) {
        x++;
    }
    valDiv[b] = x;
    if (x == a || x ==102) {
        return 0;
    } else
        return 1;
}

int main(int argc, char** argv) {
    int T, N, J, count, max, countI, countMax;
    long int countV3, countV4, countV5, countV6, countV7, countV8, countV9, countV10,
            countP, v2, v3, v4, v5, v6, v7, v8, v9, v10, countV;

    count = 0;
    cin >> T;
    cin >> N;
    cin >> J;
    v2 = 3;
    char jam[N];
    max = 1;
    countMax = 1;
    for (int i = 0; i < N - 1; i++) {
        countMax *= 2;
        max += countMax;
    }
    cout << "Case #1:" << "\n";
    while (count != J && v2 <= max) {


        countP = 0;
        v3 = 0;
        v4 = 0;
        v5 = 0;
        v6 = 0;
        v7 = 0;
        v8 = 0;
        v9 = 0;
        v10 = 0;
        countI = N - 1;
        countV = v2;


        while (countV) {
            if (countV % 2 == 1) {
                jam[countI] = '1';
                countI--;
            } else {
                jam[countI] = '0';
                countI--;
            }
            countV /= 2;
        }
        countV3 = 1;
        countV4 = 1;
        countV5 = 1;
        countV6 = 1;
        countV7 = 1;
        countV8 = 1;
        countV9 = 1;
        countV10 = 1;

        if ((jam[N - 1] == '1' && jam[0] == '1')) {
            for (int i = N - 1; i >= 0; i--, countV3 *= 3, countV4 *= 4,
                    countV5 *= 5, countV6 *= 6, countV7 *= 7, countV8 *= 8, countV9 *= 9, countV10 *= 10) {
                if (jam[i] == '1') {
                    v3 += countV3;
                    v4 += countV4;
                    v5 += countV5;
                    v6 += countV6;
                    v7 += countV7;
                    v8 += countV8;
                    v9 += countV9;
                    v10 += countV10;
                }
            }
            if (esPrimo(v2, 0) == 0) {
            } else if (esPrimo(v3, 1) == 0) {
            } else if (esPrimo(v4, 2) == 0) {
            } else if (esPrimo(v5, 3) == 0) {
            } else if (esPrimo(v6, 4) == 0) {
            } else if (esPrimo(v7, 5) == 0) {
            } else if (esPrimo(v8, 6) == 0) {
            } else if (esPrimo(v9, 7) == 0) {
            } else if (esPrimo(v10, 8) == 0) {
            } else {
                for (int i = 0; i < N; i++)
                    cout << jam[i];
                count++;
                for (int i = 0; i < 9; i++) {
                    cout << " " << valDiv[i];
                }
                if (count != J) {
                    cout << "\n";
                }
            }
        }


        v2++;
    }


    return 0;
}

