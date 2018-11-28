#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("Out.out", "w", stdout);
    std::ios_base::sync_with_stdio(false);
    int T, a, cont, aux, n, d;
    bool dig[10];
    cin >> T;
    for(int c = 0;c < T; c++){
        cout << "Case #" << c + 1 <<": ";
        cin >> a;
        aux = a;
        if(!a)
            cout << "INSOMNIA";
        else {
            n = 0;
            memset(dig, 0, sizeof dig);
            bool flag = false;
            cont = 0;
            while(!flag){
                n+=1;
                aux = a * n;
                while(aux > 0){
                    d = aux % 10;
                    aux /= 10;
                    if(!dig[d]) {
                        cont++;
                        dig[d] = true;
                    }
                }
                if(cont == 10)
                    flag = true;
            }
            cout << a * n;
        }
        cout << endl;
    }
    return 0;
}
