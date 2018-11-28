#include <iostream>
#include <fstream>
using namespace std;

int T,K,S,C;

int main(){
    ifstream fin("input.in");
    ofstream fout("output.txt");

    fin >> T;

    int i,j,k;
    for (k=1; k<=T; k++){
        fin >> K >> C >> S;
        fout << "Case #" << k << ": ";
        for (i=1; i<=S; i++) fout << i << " ";
        fout << "\n";
    }

    return 0;
}
