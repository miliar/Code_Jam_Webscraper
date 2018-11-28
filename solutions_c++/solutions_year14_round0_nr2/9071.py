#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <vector>

#define prueba "C:/Users/user/My Documents/Concursos/Code Jam 2014/prueba.txt"
#define archivo1 "C:/Users/user/Downloads/B-large.in"//Ruta depende
#define archivo2 "C:/Users/user/Desktop/respuesta.txt"

using namespace std;
//Jorge Leon-Mexico

int main(){
    int a, b, casos, bandera=0;
    double granja, aumento[3], total, produccion=2.0, primerizo, granjatime[2], tiempo[2], diferencial[2];
    string linea="";
    ifstream leer(archivo1);
    ofstream salida(archivo2);
    leer >> linea;
    casos=atoi(linea.c_str());
    for(a=1;a<=casos;a++){
        salida << "Case #";
        salida << a;
        salida << ": ";
        linea.clear();
        leer >> linea;
        granja=atof(linea.c_str());
        linea.clear();
        leer >> linea;
        aumento[0]=atof(linea.c_str());
        linea.clear();
        leer >> linea;
        total=atof(linea.c_str());
        linea.clear();
        if(a==10)   cout << total;
        primerizo=total/produccion;
        granjatime[0]=granja/produccion;
        if(primerizo<granjatime[0]){
            cout.precision(7);
            salida << setprecision(7) << fixed << primerizo;
            salida << "\n";
        }
        else{
            aumento[1]=aumento[0]+produccion;
            tiempo[0]=granjatime[0];
            diferencial[0]=(total/produccion);
            do{
                granjatime[1]=granja/aumento[1];
                aumento[2]=aumento[1]+aumento[0];
                tiempo[1]=tiempo[0]+granjatime[1];
                diferencial[1]=(total/aumento[1])+tiempo[0];
                if(a==10) cout << setprecision(7) << fixed << diferencial[1] << "    ";
                if(diferencial[1]>diferencial[0]){
                    salida << setprecision(7) << fixed << diferencial[0];
                    salida << "\n";
                    bandera=1;
                }
                else{
                    granjatime[0]=granjatime[1];
                    granjatime[1]=0.0;
                    aumento[1]=aumento[2];
                    aumento[2]=0.0;
                    tiempo[0]=tiempo[1];
                    tiempo[1]=0.0;
                    diferencial[0]=diferencial[1];
                    diferencial[1]=0.0;
                }
            }while(bandera==0);
            bandera=0;
        }
    }
    leer.close();
    salida.close();
}
