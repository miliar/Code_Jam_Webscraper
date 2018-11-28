#include <iostream>
#include <fstream>
using namespace std;

int T,X,R,C;

int main(){
    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin >> T;

    int k,aux;
    for (k=1; k<=T; k++){
        fout << "Case #" << k << ": ";
        fin >> X >> R >> C;
        if (X==1) fout << "GABRIEL\n";
        else if (X==2) { if ((R*C)%2!=0) fout << "RICHARD\n"; else fout << "GABRIEL\n"; }
        else if (X==3) {
            if ((R*C)%3!=0) { fout << "RICHARD\n"; continue; }
            if (R==3) aux=C;
            else aux=R;
            if (aux==1) fout << "RICHARD\n";
            else fout << "GABRIEL\n";        }
        else{
            if ((R*C)%4!=0) { fout << "RICHARD\n"; continue; }
            if (R==4) aux=C;
            else aux=R;
            if (aux<3) fout << "RICHARD\n";
            else fout << "GABRIEL\n";
        }
    }
    return 0;
}
