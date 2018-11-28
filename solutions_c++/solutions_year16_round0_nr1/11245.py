#include <bits/stdc++.h>
using namespace std;
set <long int> setar;
int contar (long int n){
    int contador = 0;
    while(n > 0){
        n/=10;
        contador++;
    }
    return contador;
}

void botanumeros (long int n, int cont){
    long int k = 1;
    if (cont > 1){
        for (int i = cont-1; i >= 0; i--){
            k = (long int)n/pow(10, i);
            setar.insert(k);
            //cout << k <<"  s" << endl;
            n -= (long int)k*pow(10,i);
        }
    }
    else if (cont == 1){
        setar.insert(n);
    }
}

int main(){
    int n, i=1;
    long int k, j;
    cin >> n;
    while (n--){
        setar.clear();

        cin >> k;
        if (k == 0){
            printf("Case #%d: INSOMNIA\n", i);
        }
        else {
            for (j=1; setar.size() != 10; j++)
                botanumeros(j*k, contar(j*k));
            j--;
            printf("Case #%d: %li\n", i, j*k);
        }
        i++;
    }
    return 0;
}
