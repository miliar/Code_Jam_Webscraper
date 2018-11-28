#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <vector>

#define prueba "C:/Users/user/My Documents/Concursos/Code Jam 2014/prueba.txt"
#define archivo1 "C:/Users/user/Downloads/A-small-attempt0.in"//Ruta depende
#define archivo2 "C:/Users/user/Desktop/respuesta.txt"

using namespace std;
//Jorge Leon-Mexico

int main(){
    int a, b, c=0, d=0, casos, respuesta[2], cartas[2][4], condicion=-1;
    string linea="";
    char aux[3];
    ifstream leer(archivo1);
    ofstream salida(archivo2);
    if(!leer){
        cout << "No se ha podido abrir el archivo";
    }
    else{
        leer >> linea;
        casos=atoi(linea.c_str());
        linea.clear();
        for(a=1;a<=casos;a++){
            leer >> linea;
            respuesta[0]=atoi(linea.c_str());
            linea.clear();
            for(b=1;b<respuesta[0];b++){
                for(c=0;c<4;c++){
                    leer >> linea;
                }
                linea.clear();
            }
            /*while(linea[c]!='\0'){
                if(linea[c]!=' '){
                    if(linea[c+1]!=' '){
                        aux[0]=linea[c];
                        aux[1]=linea[c+1];
                        aux[2]='\0';
                        //cout << aux;
                        cartas[0][d]=atoi(aux);
                        //printf(" %d ", cartas[0][0]);
                        c++;
                        d++;
                    }
                    else{
                        aux[0]=linea[c];
                        aux[1]='\0';
                        cartas[0][d]=atoi(aux);
                        d++;
                    }
                }
                c++;
            }*/
            for(b=0;b<4;b++){
                leer >> linea;
                cartas[0][b]=atoi(linea.c_str());
                linea.clear();
            }
            for(b=4;b>respuesta[0];b--){
                for(c=0;c<4;c++){
                    leer >> linea;
                }
                linea.clear();
            }
            leer >> linea;
            respuesta[1]=atoi(linea.c_str());
            linea.clear();
            for(b=1;b<respuesta[1];b++){
                for(c=0;c<4;c++){
                    leer >> linea;
                }
                linea.clear();
            }
            /*while(linea[c]!='\0'){
                if(linea[c]!=' '){
                    if(linea[c+1]!=' '){
                        aux[0]=linea[c];
                        aux[1]=linea[c+1];
                        aux[2]='\0';
                        cartas[1][d]=atoi(aux);
                        c++;
                        d++;
                    }
                    else{
                        aux[0]=linea[c];
                        aux[1]='\0';
                        cartas[0][d]=atoi(aux);
                        d++;
                    }
                }
                c++;
            }*/
            for(b=0;b<4;b++){
                leer >> linea;
                cartas[1][b]=atoi(linea.c_str());
                linea.clear();
            }
            for(b=4;b>respuesta[1];b--){
                for(c=0;c<4;c++){
                    leer >> linea;
                }
                linea.clear();
            }
            //printf("%d %d %d %d\n%d %d %d %d\n\n", cartas[0][0], cartas[0][1], cartas[0][2], cartas[0][3], cartas[1][0], cartas[1][1], cartas[1][2], cartas[1][3]);
            for(b=0;b<4;b++){
                for(c=0;c<4;c++){
                    if(cartas[0][b]==cartas[1][c]){
                        if((condicion<0)&&(condicion!=-2)){
                            condicion=cartas[0][b];
                        }
                        else{
                            condicion=-2;
                        }
                    }
                }
            }
            salida << "Case #";
            salida << a;
            if(condicion==-1){
                salida << ": Volunteer cheated!";
            }
            else{
                if(condicion==-2){
                    salida << ": Bad Magician!";
                }
                else{
                    salida << ": ";
                    salida << condicion;
                }
            }
            salida << "\n";
            condicion=-1;
        }
        leer.close();
        salida.close();
    }
}
