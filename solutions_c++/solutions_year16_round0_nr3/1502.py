#include <iostream>
#include <fstream>
#define LL long long
using namespace std;


ofstream fout("output1.txt");

LL N,a[50],p[10010],K,d[20],tot;

LL fpow(LL b, LL p, LL mod){
    LL res=1;
    while (p){
        if (p&1)
            res=(res*b)%mod;

        b=(b*b)%mod;
        p>>=1;
    }
    return res;
}

LL cmod(LL b, LL mod){
    LL res=0,i;
    for (i=N; i>0; i--)
        if (a[i]==1)
            res=(res+fpow(b,N-i,mod))%mod;

    return res;
}

void gen(int k){
    if (tot==500) return;

    if (k==N){
        cout << tot << "\n";
        LL i,j;
        if (tot==500) return;
        for (i=2; i<=10; i++){
            for (j=1; j<=1000; j++)
                if (cmod(i,p[j])==0) break;

            if (j>1000) break;
            d[i]=p[j];
        }

        if (i>10){
            tot++;
            for (i=1; i<=N; i++) fout << a[i];
            fout << " ";
            for (i=2; i<=10; i++) fout << d[i] << " ";
            fout << "\n";
        }

        return;

    }

    gen(k+1);
    a[k]=1;
    gen(k+1);
    a[k]=0;
}

int main(){
    ifstream fin("primes.txt");
    cin >> N;
    a[1]=a[N]=1;

    fout << "Case #1:\n";

    int i;
    for (i=1; i<=1000; i++) fin >> p[i];

    gen(2);


    return 0;
}
