#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;
int n=16;
int j=50;
int J=0;
ofstream coins;
long long prime(long long s){
    for (long long i=2; i<=sqrt(s); ++i){
        if (s%i==0) return i;
    }
    return 0;
}

bool divide(long long s){
    vector<long> v;
    for (long long i=2; i<=10; ++i){
        long long c=0;
        for (long long b=0; b<16; ++b){
            if (s& (1<<b)) {
                c+=pow(i, b);
            }

        }
        long f=prime(c);
        if (f){
            v.push_back(f);
        }
        else{
            return 0;
        }
    }
    long long d=1;
    d<<=15;
    while(d>=1){
        coins <<  ( (s&d)>0?1:0);
        d/=2;
    }
    coins << " ";
    for (unsigned int i=0; i<v.size(); ++i) coins << v[i] << " ";
    coins << "\n";
    return 1;
}

int main(){

    coins.open("c++/code_jam/coins.txt");
    int J=0;
    long long k=1;
    k<<=15;
    coins << "Case #1:\n";
    for (long long i=k+1; i<=2*k; i+=2){
        bool f =divide(i);
        J+=f;
        if (J==50) return 0;
    }
}
