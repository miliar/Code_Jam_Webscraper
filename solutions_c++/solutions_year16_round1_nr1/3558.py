#include <string>
#include <cstdio>
#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("A-large.out", "w", stdout);
    int cases;
    cin >> cases;
    for (int n = 0; n < cases; n++){
        string given;
        cin >> given;
        string lastWord = "";
        lastWord = lastWord + given[0];
        for (int i = 1; i < given.length(); i++){
            if (lastWord[0] <= given[i]){
                lastWord = given[i] + lastWord;
            }else{
                lastWord = lastWord + given[i];
            }


    }
     cout << "Case #" << n+1 << ": " << lastWord << endl;
    }
}
