/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: cristhiancamilo
 *
 * Created on 8 de abril de 2016, 09:46 PM
 */

#include <cstdlib>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int t, count;
    count = 0;
    cin >> t;
    string ma[t];
    int final[t];
    for (int i = 0; i < t; i++) {
        cin >> ma[i];
    }

    for (int i = 0; i < t; i++, count= 0) {
        for (int j = 0; j < ma[i].length(); j++) {
            if (ma[i][j + 1] != '+' && ma[i][j + 1] != '-') {
                j = ma[i].length();
            } else if ((ma[i][j] != ma[i][j + 1]) && (ma[i][j + 1] == '+')) {
                for (int k = j; k >-1; k--) {
                    ma[i][k] = '+';
                }
                count++;
            } else if ((ma[i][j] != ma[i][j + 1]) && (ma[i][j + 1] == '-')) {
                for (int k = j; k >-1; k--) {
                    ma[i][k] = '-';
                }
                count++;
            }
        }
        if (ma[i][ma[i].length() - 1] == '-') {
            count++;
        }
        final[i] = count;
    }
    for(int i = 0; i < t - 1; i++){
        cout << "Case #" << i + 1 << ": " << final[i] << "\n";
    }
     cout << "Case #" << t << ": " << final[t - 1];
    return 0;
}

