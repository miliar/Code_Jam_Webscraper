#include <iostream>
#include <fstream>
using namespace std;
#define MAXN 101
#define max(a,b) ( (a) < (b) ? (a) : (b) )

ifstream fin("entrada.txt");
ofstream fout("salida.out");

int T,N,M;

int L[MAXN][MAXN];

bool bad(int x,int y){
    int i;
    bool A=true;

    for(i=0; i<M; i++)
        if( L[i][y] > L[x][y]){
            A=false;
            break;
        }

    if(A) return false;
    A=true;
    for(i=0; i<N; i++)
        if( L[x][i] > L[x][y]){
            A=false;
            break;
        }
    if(A) return false;
    return true;

}

bool norm(){
    int i,e;

    for(i=0; i<N; i++)
        for(e=0; e<M; e++)
            if(bad(e,i))
                return false;
    return true;
}

int solve(){
    int i,e;
    fin>>N>>M;

    for(i=0; i<N; i++)
        for(e=0; e<M; e++)
            fin>>L[e][i];

    if(norm())  fout<<"YES"<<endl;
    else fout<<"NO"<<endl;

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
