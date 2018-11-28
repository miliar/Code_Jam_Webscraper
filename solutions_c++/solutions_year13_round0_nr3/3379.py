#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

ifstream fin("entrada.in");
ofstream fout("salida.out");

int T,A,B,R;

int pal(int U){
    string F;
    while(U){
        F+='0'+(U%10);
        U/=10;
    }
    for(int i=0; i<F.length()/2; i++)
        if(F[i] != F[F.length()-1 - i])
            return false;
    return true;
}

int solve(){
    int i,r;
    fin>>A>>B;
    R=0;
    i=sqrt(A);
    if(i*i != A) i++;

    for(; i*i<=B; i++){
        if(pal(i) && pal(i*i)){
            R++;
        }
    }

    fout<<R<<endl;
}

int main(){
    int i;
    fin>>T;
    for(i=1; i<=T;i++){
        fout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
