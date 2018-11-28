#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int T,N; bool a[110];

void lift(int l){
    int i,aux[110];
    for (i=1; i<=l; i++)
        a[i]=!a[i];

    for (i=1; i<=l; i++) aux[i]=a[l-i+1];
    for (i=1; i<=l; i++) a[i]=aux[i];
}

int main(){
    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin >> T;

    int i,j,k,res;
    bool p;
    string s;
    for (k=1; k<=T; k++){
        fin >> s;
        fout << "Case #" << k <<": ";

        N=s.length();
        for (i=0; i<N; i++)
            if (s[i]=='-') a[i+1]=0;
            else a[i+1]=1;

        res=0,p=1;
        while (p){
            p=0;
            for (i=N; i>0; i--)
                if (a[i]==0){
                    for (j=1; a[j]!=0; j++) ;
                    j--;
                    if (j>0) lift(j),res++;
                    lift(i),res++;
                    p=1;
                    break;
                }
        }
        fout << res << "\n";
    }

    return 0;
}
