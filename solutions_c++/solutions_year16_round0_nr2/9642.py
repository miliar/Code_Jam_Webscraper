#include<stdio.h>
#include<string>
#include<iostream>
#include<string.h>

using namespace std;

int main(){
    int T, mult;
    string S;
    cin >> T;

    for(int i = 0; i < T; i++){
        cin >> S;
        int tam = S.length();
        int cont = 0;
        mult = 1;
        if(S[0] == '-')
            cont++;
        for(int j = 1; j < tam; j++){
            if(S[j] == '-' && S[j-1] == '+')
                cont += 2;
        }
        cout << "Case #" << i+1 << ": " << cont <<  endl;
    }
}
