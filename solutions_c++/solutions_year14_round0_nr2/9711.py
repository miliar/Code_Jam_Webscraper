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

double tiempo=999999999,c=0,f=0,x=0;


int recu(double g, double p, double t){
    double aux1=t+c/g;
    double aux2=t+x/g;
    bool ii=(p>aux2)&& aux1<aux2;
    //cout << aux1 << " " << aux2 << " " << p << " " << ii << endl;
    //char yu;

    if(ii){
        recu(g+f,aux2,aux1);
    }


    if(tiempo>aux2){
        tiempo=aux2;
    }
}

int main(){
    int t;
    fstream lectura;
    ofstream myfile;
    myfile.open("salida.txt");
    lectura.open("B-small-attempt0.in");

    lectura >> t;

    for(int xxx=0; xxx<t; xxx++){
        lectura >> c >> f >> x;
        //cout << c << " " << f << " " << x << endl;
        recu(2,tiempo,0);
        myfile << "Case #" << (xxx+1) << ": ";
        myfile << fixed << setprecision(7) << tiempo << endl;

        tiempo=999999999;
    }
    myfile.close();
    lectura.close();

    return 0;
}
