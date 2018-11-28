#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{

    int T;
    cin >> T;

    freopen("B.txt", "w", stdout);

    for(int i = 1; i <= T; i++){
        string pila;
        cin >> pila;
        pila = pila + "+";

        int c = 0;
        for(int j = 0; j < pila.size()-1; j++){
            if(pila[j] != pila[j+1]) c++;
        }

        cout << "Case #"<< i <<": "<< c << endl;
    }

    return 0;
}
