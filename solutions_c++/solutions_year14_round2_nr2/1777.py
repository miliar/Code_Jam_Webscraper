#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#define forn(a,b) for((a)=0; (a)<(b); ++(a))
#define forr(a,c,b) for((a)=(c); (a)<=(b); ++(a))
using namespace std;
const int maxn = 1005;

ifstream fin("input.txt");
ofstream fout("salida.txt");

unsigned int A, B, K, R;

int main(){
    int C, T, i, e;

    fin>>T;
    forr(C,1,T){
        fin>>A>>B>>K;
        R = 0;
        for(i=0; i<A; i++)
            for(e=0; e<B; e++)
                if( (i&e) < K ) R++;

         fout<<"Case #"<<C<<": "<<R<<endl;

    }

    return 0;
}
