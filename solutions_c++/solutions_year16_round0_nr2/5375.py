#include <bits/stdc++.h>

#define forn(i,n) for(int i = 0; i < n; i++)

using namespace std;

int flip(string p){

    int plen = p.length();
    int blocks = 0;
    char current = '+';

    for(int i = 0; i < plen; i++){
        if(p[i] != current){
            if(current == '+'){
                if(i == 0) blocks ++;
                else blocks += 2;
            }
            current = p[i];
        } 
    }

    return blocks;

}


int main(){

    int testCases;
    string pancakes;

    cin >> testCases;
    forn(tt, testCases){

        cin >> pancakes;

        cout << "Case #" << tt + 1 << ": " << flip(pancakes) << endl;
    }

    return 0;
}