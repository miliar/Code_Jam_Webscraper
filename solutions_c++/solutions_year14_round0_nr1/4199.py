#include <iostream>
#include <fstream>

using namespace std;


int main (){
int casos, i, Respuesta1, Respuesta2, Tablero1[4][4], Tablero2[4][4];
fstream archivoin("A-small-attempt0.in");
fstream archivoout("A-small-practice.out");

if((archivoin)&&(archivoout)){
    archivoin >> casos;
    for(i=0;i<casos;i++){
        
        archivoin >> Respuesta1;
        for (int m=0;m<4;m++){
            for (int n=0;n<4;n++){
                archivoin >> Tablero1[m][n];
            }   
        }
        
        archivoin >> Respuesta2;
        for (int m=0;m<4;m++){
            for (int n=0;n<4;n++){
                archivoin >> Tablero2[m][n];
            }   
        }
        //cout << Tablero2[2][2] << endl;
        
        int fila[4];
        
        for(int j=0;j<4;j++){
        	fila[j]=Tablero1[Respuesta1-1][j];
        }
        
        int cont=0, solu=0;
        bool resuelto=false;
        
        for(int j=0;j<4;j++){
        	for(int m=0;m<4;m++){
        		if(!resuelto && Tablero2[0][j]==fila[m]){
        			cont =0;
        			for(int n=0;n<4;n++){
        				for(int b=0;b<4;b++){
        					if(Tablero2[n][j]==fila[b])cont++;
        				}
        			}
        			if(cont==4){
        				resuelto=true;
        				solu=Tablero2[Respuesta2-1][j];
        			}
        		}
        	}
        }
		cont=0;
        if(solu==0){
        	for(int j=0;j<4;j++){
        		for(int m=0;m<4;m++){
        			if(Tablero2[Respuesta2-1][j]==fila[m]){
        				cont++;
        				solu=Tablero2[Respuesta2-1][j];
        			}
        		}
        	}
        }
        
        archivoout << "Case #"<< i+1 << ": ";
        if(cont==1)archivoout << solu;
        else if(resuelto)archivoout << solu;
        else if(cont>1)archivoout << "Bad magician!";
        else if(cont==0)archivoout << "Volunteer cheated!";
        
        //cout << solu << endl;
        //archivoout << "";
        if(i!=casos-1) archivoout << endl;
    }
    archivoin.close();
    archivoout.close();
} else cout << "No se pudo abrir el archivo" << endl;

//system("PAUSE");
return 0;
}
