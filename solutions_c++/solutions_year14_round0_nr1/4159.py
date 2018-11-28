#include<iostream>
#include<fstream>
#include<algorithm>
#define forn(a,b) for((a)=0; (a)<(b); ++(a))
#define forr(a,c,b) for((a)=(c); (a)<=(b); ++(a))
using namespace std;

ifstream fin("entrada.txt");
ofstream fout("salida.txt");


int main(){
    int C, T, i, e, c;

    int R, A[4], B[4], S, m;

    fin>>T;
    forr(C,1,T){
        fin>>R;
        R--;
        m = 0;
        forn(i, R)   forn(e,4)   fin>>c;
        forn(e,4) fin>>A[e];
        forn(i, 4-R-1)   forn(e,4)   fin>>c;
        fin>>R;
        R--;
        forn(i, R)   forn(e,4)   fin>>c;
        forn(e,4) fin>>B[e];
        forn(i, 4-R-1)   forn(e,4)   fin>>c;

        forn(i,4)
            if( find(B,B+4,A[i]) != (B+4) ){
                S = A[i];
                m++;
            }
        fout<<"Case #"<<C<<": ";
        if( m == 1 ) fout<<S<<endl;
        else if( m > 1 ) fout<<"Bad magician!"<<endl;
        else fout<<"Volunteer cheated!"<<endl;
    }

    return 0;
}
