//
//  main.cpp
//
//  Google Code Jam 2k16 - Qualifying Round - Problem C
//
//  I regret everything seen here, but maybe I'll (re)learn some things.

#include <iostream>
#include <vector>
// #include <string>
#include <cmath>
#include <bitset>

using namespace std;

typedef unsigned long long nt;

// const nt modofhell = AAAAAARGH;

nt primeorfactor(nt testme) {
    nt d, s;
    if ((testme % 2) == 0) return 2;
    s = sqrt(testme)+1; // paranoia
    for (d=3; d <= s; d+=2) { // paranoia
        if ((testme % d) == 0) return d;
    }
    
    return 0; // prime, woof
}


int main(int argc, const char * argv[]) {
    int cases, current;
    int q, b, n, j, jc;
    
    nt candidate;
    nt bases[10+1];
    
    cin >> cases;
    for (current=1; current<=cases; ++current) {
        cout << "Case #" << current << ": ";
        cout << endl;
        
        cin >> n >> j;
        // THERE IS ONLY ONE CASE...  now generate stuff
        
        candidate = (((nt)1)<<(n-1)) + 1;
        
        jc = 0;
        while (jc < j) {
            for (b=2; b<=10; b++) bases[b]=0;
            
            for (q=0; q<n; q++) {
                if (candidate & (1 << q)) {
                    for (b=2; b<=10; b++) {
                        bases[b] += pow(b, q);
                    }
                }
            }
            
            for (b=2; b<=10; b++) {
                if ((bases[b] = primeorfactor(bases[b])) == 0) {
                    goto nope; // found a prime, dunno what it is anymore tho
                }
            }
            
            if (1) {
                
                jc++;
                switch(n) { // woof, const kludge...
                    case 6:
                        cout << bitset<6>(candidate);
                        break;
                    case 8:
                        cout << bitset<8>(candidate);
                        break;
                    case 16:
                        cout << bitset<16>(candidate);
                        break;
                    case 32:
                        cout << bitset<32>(candidate);
                        break;
                    default:
                        cout << bitset<(sizeof(nt) * 8)>(candidate);
                }
                
                for (b=2; b<=10; b++) cout << " " << bases[b];
                
                cout << endl;
            }
            
        nope:
            candidate += 2;
            if (candidate >= ((nt)1 << n)) break;
            
        } // number of jcoins loop
        
    } // pointless case loop
}

