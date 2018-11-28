#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        int S;
        cin >> S;
        int p = 0;
        char c = ' ';
        c = getc(stdin);
        int contador = 0;
        for(int j = 0; j < S+1; j++){
            c = getc(stdin);
            contador += c-48;
            if(contador <= j){
                p++;
                contador++;
            }
        }
        cout << "Case #" << i+1 << ": " << p << endl;
    }

    return 0;
}
