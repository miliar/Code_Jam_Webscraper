#include<bits/stdc++.h>
using namespace std;

int main(){
    int t, caso = 1, n, resposta, tamanho;
    string entrada;
    char atual;
    stack<char>pilha;
    cin >> t;
    while(caso <= t){
        cin >> entrada;
        tamanho = entrada.length();
        atual = '+';
        resposta = 0;
        for (int i = 0; i < tamanho; ++i){
            pilha.push(entrada[i]);
        }

        while(!pilha.empty()){
            if(pilha.top() != atual){
                atual = pilha.top();
                resposta++;
            }

            pilha.pop();
        }

        cout << "Case #" << caso << ": " << resposta << endl;
        caso++;
    }
    return 0;
}