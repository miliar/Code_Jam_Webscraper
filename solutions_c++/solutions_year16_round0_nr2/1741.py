#include <iostream>
#include <fstream>
#include <String>

using namespace std;

int main(){
    ifstream fin("pancakes.in");
    ofstream fout("pancakes.out");
    int T;
    fin>>T;
    string S;
    for(int t = 1; t <= T; t++){
        fin>>S;
        int num = 0;
        char prev = '+';
        for(int i = S.length() - 1; i >= 0; i--){
            if(S[i] != prev){
                prev = S[i];
                num++;
            }
        }
        fout<<"Case #"<<t<<": "<<num<<"\n";
    }
}
