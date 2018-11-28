#include <iostream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

//#define Debug

typedef long long Bigint;

void refine(Bigint &p, Bigint &q) {
    Bigint a=q, b=p;
    while (b!=0) {
        Bigint r = a % b;
        a=b;
        b=r;
    }
    
    p/=a; q/=a;
}

int mostdigit(Bigint n) {
    int k=0;
    while (n>0) {
        n = n >> 1;
        k++;
    }
    
    return k-1;
}

int getAns(Bigint p, Bigint q) {
    int k = mostdigit(q);
    if (k > 40) return -1;
    
    Bigint mostpow = 1;
    mostpow = mostpow << k;
    if (mostpow != q)  return -1;
    
    int i = mostdigit(p);
    return k-i;
}

int main() {
    ifstream fin("A-large.in");
    assert(fin);
    ofstream fout("pa-large.out");
    assert(fout);
    
    int test;
    fin >> test;
    for (int count=1; count<=test; count++) {
        Bigint p, q;
        char c;
        fin >> p >> c >> q;
        
    #ifdef Debug
        cout << "p=" << p << " q=" << q << endl;
    #endif
    
        refine(p, q);
    
        int ans = getAns(p, q);
        fout << "Case #" << count << ": ";
        if (ans!=-1) fout << ans << endl;
        else fout << "impossible" << endl;
    }
    
    
    fin.close();
    fout.close();
    return 0;
}
