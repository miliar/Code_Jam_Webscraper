#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int T, k=1;
    cin >> T;
    string linea;
    char tablero[4][4];
    int t,x,o;
    bool hayGanador, hayPunto;
    char ganador;
    while(T--){
        hayGanador = false;
        hayPunto = false;
        ganador = '-';
        for(int i=0;i<4;i++){
            cin >> linea;
            for(int j=0;j<4;j++){
                tablero[i][j] = linea[j];
            }
        }
        //Horizontal
        for(int i=0;i<4;i++){
            t = 0;
            x = 0;
            o = 0;
            for(int j=0;j<4;j++){
                if(tablero[i][j]=='T')
                    t++;
                if(tablero[i][j]=='.')
                    hayPunto = true;
                if(tablero[i][j]=='X')
                    x++;
                if(tablero[i][j]=='O')
                    o++;
            }
            if(o+t==4)
                ganador = 'O';
            if(x+t==4)
                ganador = 'X';
        }
        //Vertical
        for(int j=0;j<4;j++){
            t = 0;
            x = 0;
            o = 0;
            for(int i=0;i<4;i++){
                if(tablero[i][j]=='T')
                    t++;
                if(tablero[i][j]=='.')
                    hayPunto = true;
                if(tablero[i][j]=='X')
                    x++;
                if(tablero[i][j]=='O')
                    o++;
            }
            if(o+t==4)
                ganador = 'O';
            if(x+t==4)
                ganador = 'X';
        }
        t = 0;
        x = 0;
        o = 0;
        //Diagonal
        for(int j=0;j<4;j++){
            if(tablero[j][j]=='T')
                t++;
            if(tablero[j][j]=='.')
                hayPunto = true;
            if(tablero[j][j]=='X')
                x++;
            if(tablero[j][j]=='O')
                o++;
            if(o+t==4)
                ganador = 'O';
            if(x+t==4)
                ganador = 'X';
        }
        t = 0;
        x = 0;
        o = 0;
        //Diagonal
        for(int j=0;j<4;j++){
            if(tablero[3-j][j]=='T')
                t++;
            if(tablero[3-j][j]=='.')
                hayPunto = true;
            if(tablero[3-j][j]=='X')
                x++;
            if(tablero[3-j][j]=='O')
                o++;
            if(o+t==4)
                ganador = 'O';
            if(x+t==4)
                ganador = 'X';
        }
        cout << "Case #" << k++ << ": ";
        if(ganador!='-'){
            cout << ganador << " won";
        }else{
            if(hayPunto)
                cout << "Game has not completed";
            else
                cout << "Draw";
        }
        cout << endl;
    }
    return 0;
}
