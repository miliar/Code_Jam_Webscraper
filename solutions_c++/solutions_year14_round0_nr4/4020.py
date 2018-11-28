#include<iostream>
#include<cstdio>
#include<fstream>
#include<set>
#include<algorithm>
#define forn(a,b) for((a)=0; (a)<(b); ++(a))
#define forr(a,c,b) for((a)=(c); (a)<=(b); ++(a))
#define printr(a) printf("%.5Lf",a)
using namespace std;
const int maxn = 300;
typedef long double real;

ifstream fin("entrada.txt");
ofstream fout("salida.txt");

int N;
set<real> A, B;

real WarKen(set<real> &S, real chosenNaomi ){
    set<real>::iterator it;
    it = S.upper_bound(chosenNaomi);
    if( it == S.end() ){
        chosenNaomi = *S.begin();
        S.erase(S.begin());
        return chosenNaomi;
    }
    chosenNaomi = *it;
    S.erase(it);
    return chosenNaomi;
}

real DeceitfulWarNaomi(set<real> &S, set<real> &SK, real ToldKen){
    real chosenNaomi = *S.rbegin();

    if( chosenNaomi > ToldKen ) S.erase(S.upper_bound(ToldKen));
    else S.erase(S.begin());

    return chosenNaomi;
}

real WarNaomi(set<real> &S){
    real chosenNaomi = *S.rbegin();
    S.erase(--S.end());
    return chosenNaomi;
}

void solve(){
    set<real> WarA, WarB;
    int i, NaomiScore = 0;
    real ToldNaomi, ToldKen;

    ///DECEITFUL WAR
    NaomiScore = 0;
    WarA = A;
    WarB = B;
    forn( i, N ){
        ToldKen = WarKen(WarB,*WarA.rbegin());
        ToldNaomi = DeceitfulWarNaomi(WarA, WarB, ToldKen);

        if( ToldNaomi > ToldKen ) NaomiScore++;
    }
    fout<<NaomiScore<<' ';

    ///WAR
    NaomiScore = 0;
    WarA = A;
    WarB = B;
    forn( i, N ){
        ToldNaomi = WarNaomi(WarA);
        ToldKen = WarKen(WarB,ToldNaomi);
        if( ToldNaomi > ToldKen ) NaomiScore++;
    }
    fout<<NaomiScore<<endl;
}

int main(){
    int _C, _T, i;
    real r;

    fin>>_T;
    forr(_C,1,_T){
        fin>>N; A.clear(); B.clear();
        forn( i, N ){ fin>>r; A.insert(r); }
        forn( i, N ){ fin>>r; B.insert(r); }
        fout<<"Case #"<<_C<<": ";
        solve();
    }

    return 0;
}
