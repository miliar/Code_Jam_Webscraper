#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int backtrack(vector<bool> v, int cantidad_maxima, int codeJams);
vector<int> divisores(vector<bool>& v);

int main(){
    int cantidad_de_digitos, codeJams;
    vector<bool> mi_vector = vector<bool>();
    mi_vector.push_back(true);

    unsigned long long int a = 0;

    cin >> cantidad_de_digitos;
    cin >> cantidad_de_digitos >> codeJams;

    cout << "Case #1:" << endl;
    backtrack(mi_vector, cantidad_de_digitos - 1, codeJams);

    return 0;
}

int backtrack(vector<bool> v, int cantidad_maxima, int codeJams){
    if((v.size() == cantidad_maxima) && (codeJams > 0)){
        long long int result = 0;
        v.push_back(true); // Agrego el ultimo valor a derecha
        vector<int> divs = divisores(v);

        if(divs.size() == 9){ // Es un Coin Jam
            for(int i = 0; i < v.size(); i++)
                cout << v[i];

            if(divs.size() == 9){
                for(int i = 0; i < divs.size(); i++){
                    cout << " " << divs[i];
                }
                cout << endl;
            }

            return (codeJams - 1);
        }

        return codeJams;

    }else if(codeJams > 0){
        int cout_intermedio;
        v.push_back(false);
        cout_intermedio = backtrack(v, cantidad_maxima, codeJams);
        if(cout_intermedio > 0){
            v[v.size() - 1] = true;
            cout_intermedio = backtrack(v, cantidad_maxima, cout_intermedio);
        }
        return cout_intermedio;
    }
    return codeJams;
}

vector<int> divisores(vector<bool>& v){ // Se fija si no es primo en ninguna base
    unsigned long long int representacion = 0;
    int exponente = v.size() - 1;
    vector<int> divs = vector<int>();

    for(int base = 2; base < 11; base++){
        for(vector<bool>::iterator it = v.begin(); it != v.end(); it++){
            if(*it) representacion += pow(base, exponente);
            exponente--;
        }
        for(int i = 2; i <= sqrt(representacion); i++){
            if((representacion % i) == 0){
                divs.push_back(i);
                break;
            }
        }
        representacion = 0;
        exponente = v.size() - 1;
    }
    return divs;
}
