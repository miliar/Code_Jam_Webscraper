//
//  main.cpp
//
//  Google Code Jam 2k16 - Round 1C - Problem A
//
//  I regret everything seen here, but maybe I'll (re)learn some things.

#include <iostream>
#include <vector>
// #include <string>
// #include <cmath>

using namespace std;
// hell of global variables goes here!
int p[26];

void paranoiacheck() {
    int total = 0;
    
    for (int q=0; q<26; q++)
        total += p[q];
    
    for (int q=0; q<26; q++)
        if (p[q] > total/2) {
           // break point!
        }
    return;
}


int main(int argc, const char * argv[]) {
    int cases, current;
    int n, total;
    
    cin >> cases;
    for (current=1; current<=cases; ++current) {
        cout << "Case #" << current << ": ";

        for (int q=0; q<26; q++) p[q] = 0;
        total = 0;
        
        cin >> n;
        
        for (int q=0; q<n; q++) {
            cin >> p[q];
            total += p[q];
        }
        
        // find top 2
        int max = 0;
        int maxidx = 0;
        int pen = 0;
        int penidx = 0;
        
        for (int q=0; q<n; q++) {
            if (p[q] >= max) {
                max = p[q];
                maxidx = q;
            }
        }
        
        for (int q=0; q<n; q++) {
            if (q != maxidx && p[q] >= pen) {
                pen = p[q];
                penidx = q;
            }
        }
        
        // woof
        
        
        // equalize top 2
        char c = 'A' + maxidx;
        for (int q=0; q<max-pen; q++) {
            cout << c << " ";
            p[maxidx]--;
            total--;
        }
        
        // clear out all but top 2
        for (int i=0; i<n; i++) {
            if (i != maxidx && i != penidx) {
                while (p[i] > 0) {
                    c = 'A' + i;
                    cout << c << " ";
                    p[i]--;
                    total--;
                }
            }
        }
        
        // pairwise clear out top 2
        while (p[penidx] > 0) {
            c = 'A' + penidx;
            cout << c;
            p[penidx]--;
            c = 'A' + maxidx;
            cout << c << " ";
            p[maxidx]--;
            total -= 2;
        }
        
        cout << endl;
    }
}

