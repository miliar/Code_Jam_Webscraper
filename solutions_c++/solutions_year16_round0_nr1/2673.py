#include<bits/stdc++.h>
using namespace std;

map<int, int>valores;
int is_ok(){
    for (int i = 0; i < 10; ++i)
    {
        if(!valores[i])
            return 0;
    }
    return 1;
}

void atualiza_valores(int n){
    while(n){
        valores[n%10]++;
        n /= 10;
    }
}

int main(){
    int t, caso = 1, n, resposta, atual;
    cin >> t;
    while(caso <= t){
        cin >> n;

        if(!n)
            cout << "Case #" << caso << ": " << "INSOMNIA\n";
        else{
            atual = 1;
            resposta = n;
            valores.clear();

            while(!is_ok()){
                atualiza_valores(resposta);
                resposta = n * atual++;
                //cout << resposta<<endl;
            }

            cout << "Case #" << caso << ": " << n * (atual - 2)<< endl;
        }
        caso++;
    }
    return 0;
}