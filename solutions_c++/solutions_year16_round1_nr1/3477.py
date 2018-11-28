#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;
int main()
{
    ifstream read("A-large (1).in");
    ofstream salida("salida.txt");
    int casos;
    string lee;
    string lastcaso;
    string respuesta;
    getline(read,lee);
    casos=atoi(lee.c_str());
    for(int i=0;i<casos;i++)
    {
        getline(read,lastcaso);
        respuesta=lastcaso[0];

        for(int j=1;j<lastcaso.size();j++)
        {
            //cout<<lastcaso[j]<<"/"<<respuesta[0]<<endl;
            if(lastcaso[j]>=respuesta[0])
            {
                respuesta=lastcaso[j]+respuesta;
            }else respuesta+=lastcaso[j];
        }
        salida<<"Case #"<<i+1<<": "<<respuesta<<"\n";
    }
    read.close();
    salida.close();
}
