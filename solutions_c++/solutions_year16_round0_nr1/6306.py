//NOTA: demora de casi 1 hora por un bug en el metodo log10 de math.h en el que te da 999... en lugar de 1000 (se que es float, pero no debio arrojar decimales)
#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <math.h>

using namespace std;
int main()
{
    ifstream read("A-large.in");
    ofstream salida("salida.txt");
    int casos;
    string lee;
    getline(read,lee);
    casos=atoi(lee.c_str());
    int original;
    int actual;
    int modulo;
    int temporal;
    int tam;
    int res;
    int j;
    bool numeros[10];
    for(int i=0;i<casos;i++)
    {
        for(int h=0;h<10;h++) numeros[h]=false;
        getline(read,lee);
        tam=lee.size();
        original=atoi(lee.c_str());
        actual=0;
        if(original==0)
        {
            salida<<"Case #"<<i+1<<": "<<"INSOMNIA"<<"\n";
            continue;
        }
        while(!(numeros[0] and numeros[1] and numeros[2] and numeros[3] and numeros[4] and numeros[5] and numeros[6] and numeros[7] and numeros[8] and numeros[9]))
        {
            actual+=original;
            temporal=actual;
            tam=log10 (actual)+1; //tamaño de un entero by Alvaro Missael Delgado Castellanos (si alguien no se habia dado cuenta antes XD)
            //cout<<"tam: "<<tam;
            for(int j=tam-1;j>=0;j--)
            {
                modulo=pow(10,j);
                if(modulo%2==1 and modulo!=1) modulo++; //bug de c++ con los logaritmos
                res=temporal/modulo;
                numeros[res]=true;
                //cout<<"temp: "<<temporal<<"/modulo: "<<modulo<<" res: "<<res<<endl;
                temporal-=res*modulo;
            }
            //cout<<actual<<"/";
            //for(int i=0;i<10;i++) cout<<numeros[i];
            //cout<<endl;
        }
        salida<<"Case #"<<i+1<<": "<<actual<<"\n";
    }
    salida.close();
}
