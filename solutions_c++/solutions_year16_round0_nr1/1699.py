#include <iostream>
#include <fstream>
#define LL long long
using namespace std;

LL T,N; bool v[20];

LL cnt(LL N){
    LL res=0;
    while (N){
        if (!v[N%10]) v[N%10]=1,res++;
        N/=10;
    }

    return res;
}

LL gets(LL N){
    LL i=1,t=0,j;
    for (j=0; j<10; j++) v[j]=0;

    t=cnt(N);

    while (t<10){
        i++;
        t+=cnt(i*N);
    }

    return i*N;
}

int main(){
    ifstream fin("input.in");
    ofstream fout("output.out");

    fin >> T;
    int i;
    for (i=1; i<=T; i++){
        fin >> N;
        fout << "Case #" << i << ": ";
        if (N==0) fout << "INSOMNIA\n";
        else fout << gets(N) << "\n";
    }

    return 0;
}
