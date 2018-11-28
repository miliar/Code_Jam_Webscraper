//
//  pan.cpp
//
//
//  Created by Pedro Abraham Moreno Vazquez on 09/04/16.
//
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;


bool check(int i,int distancia, string cadena){//funcion para verificar que un indice se puede manipular a cierta distancia en una cadena
    if (i<=int(cadena.length())-distancia-1) {
        return true;
    }
    else{
        return false;
    }
}

int main(int argc, const char * argv[]) {
    
    int t=0;
    cin>>t;
    if (t<1 || t>100) {
        return 0;
    }
    vector<string>lhots;
    string aux;
    
    
    for (int i=0; i<t; i++) {
        
        cin>>aux;
        lhots.push_back(aux);
        
    }
    
    for (int i = 0; i < t; i++) {
        
        //char aux;
        int flips=0;
        if (lhots[i].length()<1 || lhots[i].length()>100 ) {
            continue;
        }
        for (int cake=0; cake<lhots[i].length(); cake++) {
            if (check(cake, 1, lhots[i]) && lhots[i][cake]!=lhots[i][cake+1] && (lhots[i][cake]=='+' || lhots[i][cake]=='-' ) ) {
                flips++;
            }
        }
        if (lhots[i][lhots[i].length()-1]=='-') {
            flips=flips+1;
        }
        cout <<"Case #"<<i+1<<": "<< flips<< std::endl;
        
    }
    
    return 0;
    
    
    
}


