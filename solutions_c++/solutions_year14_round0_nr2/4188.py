#include<iostream>
#include<fstream>
#include<cstdio>
#define forn(a,b) for((a)=0; (a)<(b); ++(a))
#define forr(a,c,b) for((a)=(c); (a)<=(b); ++(a))
using namespace std;

typedef long double real;

ifstream fin("entrada.txt");
FILE *fout = fopen("salida.txt","w");

real C, F, X;
real Res, Better, Rate;
real Tenemos, Queda;

int main(){
    int _C, _T, i, e;

    fin>>_T;
    forr(_C,1,_T){
        fin>>C>>F>>X;

        Rate = 2.0L;
        Better = X / Rate;
        Tenemos = 0;

        do{
            Res = Better;
            Tenemos += C/Rate;
            Queda = X / (Rate + F);
            Better = Tenemos + Queda;
            Rate += F;
        }while( Better < Res );
        fprintf(fout,"Case #%i: %.7LF\n",_C,Res);
        printf("Case #%i: %.7LF\n",_C,Res);
    }

    return 0;
}
