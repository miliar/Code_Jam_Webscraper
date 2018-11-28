#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <iomanip>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
#define cin fin
#define cout fout
typedef long double ld;

ld solucion(ld orig, ld A, ld C, ld F, ld X, ld acumulador)
{
    if(acumulador > 2400){
        return orig;
    }else{
        return min(X/A, C/A + solucion(orig, A+F, C, F, X, acumulador+1));
    }
}

int main()
{
    int numeroCasos = 0;
    int casoNro = 1;
    cin >> numeroCasos;
    while(numeroCasos--)
    {
        ld C, F, X;
        cin >> C >> F >> X;
        cout << setprecision(7) << fixed <<"Case #" << casoNro << ": " << solucion(X/2, 2, C, F, X, 0) << endl;
        casoNro++;
    }
}