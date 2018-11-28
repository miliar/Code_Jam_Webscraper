#include <iostream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

typedef long long bigint;

const char *infile = "B-small-attempt0.in";
const char *outfile = "pb-small.out";

bigint getans(bigint A, bigint B, bigint K) {
    bigint ans=0;
    for (int i=0; i<=A; i++) 
        for (int j=0; j<=B; j++)
            if ((i & j) <= K) ans++;
    return ans;
}

int main() {
    ifstream fin(infile);
    assert(fin);
    ofstream fout(outfile);
    assert(fout);
    
    int test;
    fin >> test;
    for (int count=1; count<=test; count++) {
        int A, B, K;
        fin >> A >> B >> K;
        A--; 
        B--;
        K--;
        fout << "Case #" << count << ": " << getans(A, B, K) << endl;
    }

    
    fin.close();
    fout.close();
    
    return 0;
}
