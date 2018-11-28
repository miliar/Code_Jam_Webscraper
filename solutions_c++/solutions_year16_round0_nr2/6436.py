#include <bits/stdc++.h>
using namespace std;

main() {
    int nCases, k, cont;
    string pile;
    
    cin >> nCases;
    for(int i=0; i<nCases; i++) {
        cont = 0;
        cin >> pile;
        
        k = pile.find_last_of('-');
        while(k != string::npos) {
            for(int j=0; j<=k; j++) {
                if(pile[j] == '-')
                    pile[j] = '+';
                else
                    pile[j] = '-';
            }
            k = pile.find_last_of('-');
            cont++;           
        }
        cout << "Case #" << i+1 << ": " << cont << '\n';
    }    
}