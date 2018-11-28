#include <bits/stdc++.h>
#define IMPOSIBLE " IMPOSSIBLE"
using namespace std;

const int MAXC = 100;

long long int K_a_la[MAXC + 2];
int necesito;
int K, S;

void init(int C){
    long long int mult = K;
    K_a_la[0] = 1;
    for(int i = 1; i <= C; i++){
        K_a_la[i] = K_a_la[i - 1];
        K_a_la[i] *= mult;
    }
}

long long int encuentra(long long int ini, int num, int C){
    if(C == 0) return ini;
    if(num > K) return ini;
    long long int i = K_a_la[C - 1] * (num - 1);
    ini += i;
    return encuentra(ini, num + 1, C - 1);
}

void muestra_solucion(int C){
    for(int i = 1; i <= K; i += C){
        cout << " " << encuentra(1, i, C);
    }
}

int main(){
    //freopen("D-large.in", "r", stdin);
    //freopen("salida_grande.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    int C;
    for(int caso = 1; caso <= T; caso++){
        cout << "Case #" << caso << ":";
        cin >> K >> C >> S;
        necesito = (K + C - 1) / C;
        if(necesito > S){
            cout << IMPOSIBLE;
        }else{
            init(C);
            muestra_solucion(C);
        }
        cout << "\n";
    }
    return 0;
}
