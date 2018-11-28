#include <iostream>
#include <fstream>

using namespace std;


int main (){
int casos, i,win, noent;
char tablero[4][4], letra, ganador, colum, final;
fstream archivoin("A-small-attempt0.in");
fstream archivoout("output.out");

if((archivoin)&&(archivoout)){
    archivoin >> casos;
    letra = archivoin.get();
    for(i=0;i<casos;i++){
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                letra=archivoin.get();
                tablero[j][k] = letra;
            }
            //quitar salto linea
            letra=archivoin.get();
            //
        }
        win =0;
        //vertical
        for(int j=0;j<4;j++){
            if(tablero[0][j]=='T'&&tablero[1][j]!='.'){
                colum=tablero[1][j];
            }else if(tablero[0][j]!='T'&&tablero[0][j]!='.'){
                colum=tablero[0][j];
            }else if(tablero[0][j]=='.'){
                continue;
            }
                    for(int y=1;y<4;y++){
                        if(tablero[y][j]==colum||tablero[y][j]=='T'){
                            if(y==3){
                                win=1;
                                ganador=colum;
                            }
                        }else break;
                    }
        }
        //horizontal
        if(win!=1){
        for(int j=0;j<4;j++){
            if(tablero[j][0]=='T'&&tablero[j][1]!='.'){
                colum=tablero[j][1];
            }else if(tablero[j][0]!='T'&&tablero[j][0]!='.'){
                colum=tablero[j][0];
            }else if(tablero[j][0]=='.'){
                continue;
            }
                    for(int y=1;y<4;y++){
                        if(tablero[j][y]==colum||tablero[j][y]=='T'){
                            if(y==3){
                                win=1;
                                ganador=colum;
                            }
                        }else break;
                    }
        }
        }
        //diagonal1
        if(win!=1){
        noent=0;
             if(tablero[0][0]=='T'&&tablero[1][1]!='.'){
                colum=tablero[1][1];
            }else if(tablero[0][0]!='T'&&tablero[0][0]!='.'){
                colum=tablero[0][0];
            }else if(tablero[0][0]=='.'){
                noent=1;
            }
        if(noent==0){
        for(int j=0;j<3;j++){
            if(colum==tablero[j+1][j+1]||tablero[j+1][j+1]=='T'){
                if(j==2){
                    win=1;
                    ganador=colum;
                }
            }else break;
        }
        }
        }

        //diagonal2
        if(win!=1){
        noent=0;
        if(tablero[0][3]=='T'&&tablero[1][1]!='.'){
            colum=tablero[1][2];
        }else if(tablero[0][3]!='T'&&tablero[0][3]!='.'){
            colum=tablero[0][3];
        }else if(tablero[0][3]=='.'){
            noent=1;
        }
        if(noent==0){
            for(int j=0;j<3;j++){
                if(colum==tablero[1+j][2-j]||tablero[1+j][2-j]=='T'){
                    if(j==2){
                        win=1;
                        ganador=colum;
                    }
                }else break;
            }
        }
        }
        
        if(win!=1){
            final=0;
            for(int j=0;j<4;j++){
                if(final==1) break;
                for(int y=0;y<4;y++){
                    if(tablero[j][y]=='.'){
                        final=1;
                        break;
                    }
                }
            }
        }
        //quitar espacio entre casos
        letra=archivoin.get();
        //
        if(win==1){
            archivoout << "Case #"<< i+1 << ": "<< ganador << " won";
        }
        if(win!=1&&final==1){
            archivoout << "Case #"<< i+1 << ": "<< "Game has not completed";
        }
        if(win!=1&&final==0){
            archivoout << "Case #"<< i+1 << ": "<< "Draw";
        }

        if(i!=casos-1) archivoout << endl;
    }
    archivoin.close();
    archivoout.close();
} else cout << "No se pudo abrir el archivo" << endl;

system("PAUSE");
return 0;
}
