#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int** crear_matriz_int(int n, int m){
    int** X = new int*[n];
    for(int i = 0; i < n; i++){
        X[i] = new int[m];
    };
    return X;
};

void liberar_matriz_int(int** X, int n, int m){
    for(int i = 0; i < n; i++){
        delete[] X[i];
    };
    delete[] X;
    return;
};


int leer_int(istream& is){
    int y;
    is >> y;
    return y;
};

int** leer_matriz_int(istream& is, int** X, int n, int m){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            X[i][j] = leer_int(is);
        };
    };
    return X;
};


ostream& escribir_int(int y, ostream& os){
    os << y;
};

ostream& escribir_matriz_int(ostream& os, int** X, int n, int m){
    os << "\n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            escribir_int(X[i][j], os);
            if(j < m - 1){
                os << "\t";
            };
        };
        os << "\n";
    };
    return os;
};


int** cuadrado_matriz(int** X, int n, int m){
    int** Y = crear_matriz_int(n, m);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            Y[i][j] = X[i][j] * X[i][j];
        };
    };
    return Y;
};

int** tablas(int** X, int n, int m){
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
             X[i-1][j-1] = i*j;
        };
    };
    return X;
};

int** identidad(int** X, int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(i == j){
                X[i][j] = 1;
            }else{
                X[i][j] = 0;
            };
        };
    };
    return X;
};


int suma_n(int n){
    int x;
    return x*(x+1)/2;
};

bool suma_filas(int **x, int n, int res){
    int sumaf;
    int suma_fan = 0;
    int sumac = 0;
    int suma_can = 0;
    bool rs = true;

    for(int k = 0; k < n; k++){
        suma_fan+=x[0][k];
        suma_can+=x[k][0];
    };

    if(suma_fan != res){
        //cout << suma_fan << endl;
        return false;
    };

    if(suma_can != res){
        //cout << suma_can << endl;
        return false;
    };

    for(int i = 1; i < n; i++){
        sumaf = 0;
        sumac = 0;
        for(int j = 0; j < n; j++){
            sumaf+=x[i][j];
            sumac+=x[j][i];
        };

        if((sumaf == suma_fan) && (sumaf == res) && (sumac == res) && (suma_can == res)){
            //cout << "ss";
            continue;
        }else{
            return false;
        };
    };
    //cout << "s";
    return rs;
};

bool sudoku_ok(int** x, int n){
    int res = suma_n(n);
    return suma_filas(x, n, res);
};

int magic_trick(int **x, int **y, int fr, int sr){
    int pos = 0;
    int count = 0;
    fr--;
    sr--;
    //cout << fr;
    //cout << sr;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
                
            //cout << x[fr][i] << "vs" << y[sr][j] << "\n"; 
            if(x[fr][i] == y[sr][j]){
                count ++;
                pos = x[fr][i];
                //cout << "pasa" << pos;
            };
        };
    };
    //cout << "sale";
    if(count == 0){
        return -1; // cheated
    };
    if(count == 1){
        return pos; // pos
    };
    if(count > 1){
        return -2; //bad magician;
    };
};

int main(){
    int i=0, n;
    int fr;
    int sr, res;
    ifstream ifs("A-small-attempt2.in");
    ofstream ofs("outsmall.txt");
    ifs >> n;
    char* sal;
    while(i < n){
            ifs >> fr;
            //cout << fr;
            int** I = crear_matriz_int(4, 4);
            I = leer_matriz_int(ifs, I, 4, 4);
            //escribir_matriz_int(cout, I, 4,4);
            
            ifs >> sr;
            //cout << sr;
            int** J = crear_matriz_int(4, 4);
            J = leer_matriz_int(ifs, J, 4, 4);
            //escribir_matriz_int(cout, J, 4,4);
            
            res = magic_trick(I, J, fr, sr);
            if(res == -1){
                ofs << "Case #" << i+1 <<": Volunteer cheated!\n";
            }else if(res == -2){
                ofs << "Case #" << i+1 <<": Bad magician!\n";
            }else{
                ofs << "Case #" << i+1 <<": " << res << "\n";
            };
            i++;
            
    };
    ofs.close();
    ifs.close();
    
    system("pause");
    return EXIT_SUCCESS;
};
