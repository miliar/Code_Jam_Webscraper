    #include <stdio.h>
    #include <string.h>
    #include <iostream>
    #include <fstream>
    using namespace std;

    int casos;

    struct campo{
        //Variable que dice un numero para saber si el caso es correcto, empate, etc
        // -1, empate 0 sin terminar, 1 x gano, 2 o gano
        int status = -2;
        char mapa [6][6] = {{'q','q','q','q','q','q'},{'q','q','q','q','q','q'}};
    };

    campo mapi[1006];

    void leer(){
        ifstream archivo;
        archivo.open("A-small-attempt2.in");
        //archivo.open ("A-small-attempt0.in", ios::in);
        //cin >> casos;
        //getline (archivo,casos);
        archivo >> casos;
        //getline(archivo,linea);
        string linea;
        for(int i = 0; i < casos; i++){
            for(int e = 0; e < 4; e++){
                //cin >> linea;
                archivo >> linea;
                //getline(archivo,linea);
                strcpy(mapi[i].mapa[e], linea.c_str());
            }
        }
        //Que los imprima para ver si leyo bien
        /*
        cout << '\n'<< '\n'<< "Casos de prueba" <<'\n';
        for(int i = 0; i < casos; i++){
                cout << "Caso " <<i<< '\n';
            for(int e = 0; e < 4; e++){
                for(int d = 0; d < 4; d++){
                    cout << mapi[i].mapa[e][d];
                }
                cout << '\n';
            }
            cout << '\n' << '\n';
        }
        */
        archivo.close();
    }

    void buscar(int i){
        //Si solucion es solucion
        int cont=0;
        bool stats = false;
        bool haypuntos = false;
        if(!stats){
            for(int e=0; e<4; e++){
                //Comparar una fila
                for(int d=0; d<4; d++){
                    if(mapi[i].mapa[e][d]=='.')
                        haypuntos = true;
                    if((mapi[i].mapa[e][d]=='X' || mapi[i].mapa[e][d]=='T') && mapi[i].mapa[e][d]!='O' && mapi[i].mapa[e][d]!='q')
                            cont++;
                    else
                        d = 4;
                }
                if(cont>=4){
                    //Ya esta bien
                    mapi[i].status = 1;
                    e = 4;
                    stats = true;
                }
                else
                    cont = 0;
            }
        }
        if(!stats){
            //Comparar una columna
                for(int e=0; e<4; e++){
                    for(int d=0; d<4; d++){
                        if((mapi[i].mapa[d][e]=='X' || mapi[i].mapa[d][e]=='T') && mapi[i].mapa[d][e]!='O' && mapi[i].mapa[d][e]!='q')
                                cont++;
                        else
                            d = 4;
                    }
                    if(cont>=4){
                        //Ya esta bien
                        mapi[i].status = 1;
                        e = 4;
                        stats = true;
                    }
                    else
                        cont = 0;
            }
        }
        if(!stats){
            //Comparar en diagonal
            int otra=0;
            for(int d=0; d<4; d++){
                if((mapi[i].mapa[otra][d]=='X' || mapi[i].mapa[otra][d]=='T') && mapi[i].mapa[otra][d]!='O' && mapi[i].mapa[otra][d]!='q')
                    cont++;
                else
                    d = 4;
                otra++;
            }
            if(cont >= 4){
                //Ya esta bien
                mapi[i].status = 1;
                stats = true;
            }
            else
                cont = 0;
            otra = 3;
            for(int d=0; d < 4; d++){
                if((mapi[i].mapa[otra][d]=='X' || mapi[i].mapa[otra][d]=='T') && mapi[i].mapa[otra][d]!='O' && mapi[i].mapa[otra][d]!='q')
                    cont++;
                else
                    d = 4;
                otra--;
            }
            if(cont >= 4){
                //Ya esta bien
                mapi[i].status = 1;
                stats = true;
            }
            else
                cont = 0;
        }


        if(!stats){
            for(int e=0; e<4; e++){
                //Comparar una fila
                for(int d=0; d<4; d++){
                    if((mapi[i].mapa[e][d]=='O' || mapi[i].mapa[e][d]=='T') && mapi[i].mapa[e][d]!='X' && mapi[i].mapa[e][d]!='q')
                            cont++;
                    else
                        d = 4;
                }
                if(cont>=4){
                    //Ya esta bien
                    mapi[i].status = 2;
                    e = 4;
                    stats = true;
                }
                else
                    cont = 0;
            }
        }
        if(!stats){
            //Comparar una columna
                for(int e=0; e<4; e++){
                    for(int d=0; d<4; d++){
                        if((mapi[i].mapa[d][e]=='O' || mapi[i].mapa[d][e]=='T') && mapi[i].mapa[d][e]!='X' && mapi[i].mapa[d][e]!='q')
                                cont++;
                        else
                            d = 4;
                    }
                    if(cont>=4){
                        //Ya esta bien
                        mapi[i].status = 2;
                        e = 4;
                        stats = true;
                    }
                    else
                        cont = 0;
            }
        }
        if(!stats){
            //Comparar en diagonal
            int otra=0;
            for(int d=0; d<4; d++){
                if((mapi[i].mapa[otra][d]=='O' || mapi[i].mapa[otra][d]=='T') && mapi[i].mapa[otra][d]!='X' && mapi[i].mapa[otra][d]!='q')
                    cont++;
                else
                    d = 4;
                otra++;
            }
            if(cont >= 4){
                //Ya esta bien
                mapi[i].status = 2;
                stats = true;
            }
            else
                cont = 0;
            otra = 3;
            for(int d=0; d < 4; d++){
                if((mapi[i].mapa[otra][d]=='O' || mapi[i].mapa[otra][d]=='T') && mapi[i].mapa[otra][d]!='X' && mapi[i].mapa[otra][d]!='q')
                    cont++;
                else
                    d = 4;
                otra--;
            }
            if(cont >= 4){
                //Ya esta bien
                mapi[i].status = 2;
                stats = true;
            }
            else
                cont = 0;
        }
        //Determinar si es un empate o sin terminar
        if(!stats){
            if(haypuntos){
                //Sin terminar
                mapi[i].status = 0;
                stats = true;
            }
            else{
                mapi[i].status = -1;
                stats = true;
            }
        }
    }

    void imprimir(int n){
        ofstream archivoi;
        archivoi.open("outputTic.out", std::ios::out | std::ios::app);
        cout << "Case #" << n+1 <<": ";
        archivoi << "Case #" << n+1 <<": ";
        if(mapi[n].status == -1){
            //Es un empate
            cout << "Draw";
            archivoi << "Draw";
        }
        else if(mapi[n].status == 0){
            //Juego sin terminar
            cout << "Game has not completed";
            archivoi << "Game has not completed";
        }
        else if(mapi[n].status == 1){
            //X gano
            cout << "X won";
            archivoi << "X won";
        }
        else if(mapi[n].status == 2){
            //O gano
            cout << "O won";
            archivoi << "O won";
        }
        cout << '\n';
        archivoi << '\n';
        archivoi.close();
    }



int main(){
    //ofstream archivoi;
    //archivoi.open("outputTic.out");
    leer(); // Bien
    for(int r = 0; r<casos; r++){
        buscar(r);
        imprimir(r);
    }
    //archivo.close();
    return 0;
}
