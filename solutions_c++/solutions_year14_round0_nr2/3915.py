#include<iostream>
#include<iomanip>
#include <fstream>
using namespace std;
int main(){
    ofstream myfile;
    ifstream lectura;
    myfile.open("salida2.txt");
    lectura.open("B-large.in");
    int t;
    double c,f,x,cps=2.0;
    double ant=0, acum= 0;
    lectura >> t;
    for(int kase=0;kase<t;kase++) {
        lectura >> c >> f >> x;
        
        //el primero
        cps = 2.0;
        ant = x / cps;
        acum = c / cps;
        
        while(ant > (x / (cps+f)) + acum ){
            ant = (x / (cps+f)) + acum;
            cps += f;
            acum += c / cps;
        }
        myfile << fixed << setprecision(7) << "Case #" << kase+1 << ": " << ant << endl;
    }
}