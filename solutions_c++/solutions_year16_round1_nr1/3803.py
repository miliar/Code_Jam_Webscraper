#include<bits/stdc++.h>
using namespace std;

int test, l, izq, der, evIzq, evDer;
string cad, res;

int mejor(){
    char maxi = cad[evDer];
    int donde = evDer;
    for(int checa = evDer - 1; checa >= evIzq; checa--){
        if(cad[checa] > maxi){
            maxi = cad[checa];
            donde = checa;
        }
    }
    return donde;
}

void solve(){
    cin >> cad;
    l = cad.length();
    res = cad;
    izq = 0;
    der = l - 1;
    evIzq = 0;
    evDer = l - 1;
    while(evIzq <= evDer){
        int best = mejor();
        res[izq++] = cad[best];
        for(int i = evDer; i > best; i--){
            res[der--] = cad[i];
        }
        evDer = best - 1;
    }
    cout << res << endl;
}

int main(){
    freopen("ALarge.out", "w", stdout);
    freopen("ALarge.in", "r", stdin);
    scanf("%d", &test);
    for(int testCase = 1; testCase <= test; testCase++){
        printf("Case #%d: ", testCase);
        solve();
    }
    fclose(stdout);
}
