#include <bits/stdc++.h>
using namespace std;

const char FELIZ = '+';
const char BLANCO = '-';

const int MAXN = 100;

string S;

void elimina_sobrante(int &N){
    while(N > 0 && S[N - 1] == FELIZ){
        N--;
    }
}

int convierte(int N, char tipo){
    if(N == 0) return 0;
    int i = N - 1;
    while(i >= 0 && S[i] == tipo){
        i--;
        N--;
    }
    if(N == 0) return 0;
    tipo = (tipo == FELIZ) ? BLANCO : FELIZ;
    return convierte(N, tipo) + 1;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T, N;
    cin >> T;
    for(int caso = 1; caso <= T; caso++){
        cout << "Case #" << caso << ": ";
        S.clear();
        cin >> S;
        N = S.size();
        elimina_sobrante(N);
        cout << convierte(N, FELIZ) << "\n";
    }
    return 0;
}
