#include<iostream>
#include<cstdint>
#include "ttmath/ttmath.h"
#define LL ttmath::Int<4>
#define bits 32
#define count 500
using namespace std;

LL powers[11][bits];

int main() {
 //   cout<<"Case #1:\n";
    for(int base=2;base<=10;base++) {
        LL num = 1;
        for(int a=0;a<bits;a++) {
            powers[base][a]=num;
            num*=base;
        }
    }
    int l=0;
    for(int i=0;i<(1<<(bits-2));i++) {
        bool ok=true;
        vector<int> divisors(11);
        LL num;
        for(int base=2;base<=10;base++) {
            num = 0;
            for(int a=0;a<bits;a++) {
                int bit = (a==0||a==(bits-1)) ? 1 : ((i>>(a-1))&1);
                if(bit) num += powers[base][a];
            }
            bool prime = true;
            
            for(int i=2;i<=13;i++) if(num % i == 0) { prime = false; divisors[base]=i;}
            if(prime) {ok=false;break;}
     //       cout<<base<<": "<<num<<endl;
        }
        if(ok) {
            cout<<num<<" ";
            l++;
            string l="";
            for(int b=2;b<=10;b++) {cout<<l<<divisors[b];l=" ";}
            cout<<endl;

        }
        if(l==count) break;
    }
    
}
